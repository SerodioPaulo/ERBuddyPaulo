import matplotlib.pyplot as plt
import math
import random

signal = []

for count in range (1,5000):
  #signal.extend([0.9 * math.sin(0.333*count) + 1.3 * math.cos(0.4*count) + 0.7 * math.cos(0.6*count) +  10 * math.log(200 + count) + 0.02*random.randint(0,100) + 50])
  signal.extend([0.9 * math.sin(0.02*count) + 1.3 * math.cos(0.02*1.33*count) + 0.7 * math.cos(0.02*2*count) +  10 * math.log(200 + count) + 0.002*random.randint(0,100) + 50])

plt.plot(signal)
plt.ylabel('Signal')
plt.show()

alpha = 0.9
wo = 0
wi = 0
DCFiltered = []

for count in range(1, len(signal) - 1 ):
  wo = signal[count] + alpha * wi
  DCFiltered.extend([wo - wi])
  wi = wo

#print(wo)
DCFiltered = DCFiltered[50:]
plt.plot(DCFiltered)
plt.ylabel('DCFiltered')
plt.show()

MeanFiltered = []
filtersize = 100

sum = 0
values = []
for count in range(0, filtersize):
  values.extend([DCFiltered[count]])
  sum += DCFiltered[count]
starter = 0

print(values[0])

index = 0
for count in range(0, len(DCFiltered) - 1 ):
  sum = sum - values[index]
  values[index] = DCFiltered[count]
  sum += values[index]

  index += 1
  index = index % filtersize

  if(starter < filtersize):
    starter += 1
  avg = sum / starter
  MeanFiltered.extend([avg - DCFiltered[count]])

#for count in range(0,9):
#  sum += DCFiltered[count]

#for count in range(10, len(DCFiltered) - 1 ):
#  sum -= DCFiltered[count-10]
#  sum += DCFiltered[count]
#  MeanFiltered.extend([(sum / filtersize) - DCFiltered[count]])

plt.plot(MeanFiltered[50:])
plt.ylabel('MeanFiltered')
plt.show()



 

