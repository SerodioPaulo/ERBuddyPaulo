#from max30100  import *
from time import sleep

import max30100
mx30 = max30100.MAX30100()
mx30.disable_spo2()
mx30.reset()
mx30 = max30100.MAX30100()

rawdata = []
dupes = []
indexlist = []
data = []

f = open('pulsedata.dat', 'w')
d = open('dcfilter.dat', 'w')
index = 0
#for index in range (0,1000):)
try:
    mx30.read_sensor()
    sleep(0.009)
    mx30.read_sensor()
    sleep(0.009)
    mx30.read_sensor()
    sleep(0.009)
    while mx30.buffer_ir[index] == 0 or mx30.buffer_ir[index+1] == 0 or mx30.buffer_ir[index+2] == 0:
        index += 1
        if mx30.buffer_ir[index] != 0:
            dupes.append(mx30.buffer_ir[index])
            data.append(mx30.buffer_ir[index])
            indexlist.append(index)
        mx30.read_sensor()
        sleep(0.009)
    index += 1
    while True:
        if mx30.buffer_ir[index] == dupes[0]:
                dupes.append(mx30.buffer_ir[index+1])
                data.append(mx30.buffer_ir[index+1])
                indexlist.append(index+1)
                del dupes[0]
                mx30.read_sensor()
                sleep(0.009)
                mx30.read_sensor()
                sleep(0.009)
                index += 2
        else:
            #if rawdata[index+1] == dupes[0]: Implied
            if mx30.buffer_ir[index+1] == dupes[1]:
                dupes.append(mx30.buffer_ir[index])
                data.append(mx30.buffer_ir[index])
                indexlist.append(index)
                del dupes[0]
            mx30.read_sensor()
            sleep(0.009)
            index += 1
except KeyboardInterrupt:
    try:
        index = 0
        while True:
            f.write("{} {}\n".format(indexlist[index],data[index]))
            index += 1
    except IndexError:
        alpha = 0.85
        wo = 0
        wi = 0
        state = 0 # 0 when steady no pulse, 1 then 2 when first held spike below threshold, then must count to 10 all above threshold to return to 0 
        beats = []
        min = -10
        threshold = min/2 
        #DCFiltered = []
        for count in range(1, len(data) - 1 ):
            wo = data[count] + alpha * wi
            #DCFiltered.extend([wo - wi])
            if count > 35: d.write("{} {}\n".format(indexlist[count],wo-wi))
            if wo-wi < min: min = wo-wi ; threshold = min/3
            if state == 0 and wo-wi < threshold and count > 45:
                state = 1
            elif state == 1 and count > 45:
                if wo-wi >= threshold: state = 0
                if wo-wi < threshold:
                    state = 2
                    beats.append(indexlist[count])
            elif state > 1 and wo-wi >= threshold and count > 45:
                state += 1
                if state == 10: state = 0
            wi = wo
        f.close()
        d.close()
        print(len(data))
        print(len(mx30.buffer_ir))
        print(beats)