import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#ask = input("pin   ")

pinOuts = [31,11,37,15,29,13] #The pins on the Raspberry Pi that the six wires in the LED array are connected to

combos = [0,4,0,5,0,3,0,1,2,1,4,1,5,1,4,0,5,0,3,0,1,0,1,2,1,4,1,5,0,2,4,2,5,2,3,2,3,4,3,5,3,1,2,0,2,4,2,5,2,3,4,3,5,3,1,3] #Pairs of VCC/GND wires for each LED

outLEDs = [5,11,24,17] #Which LEDs you want to turn on

outTime = time.time() + 60

try:
    while True:
        for outLED in outLEDs:
            GPIO.setup(pinOuts, GPIO.IN)
            GPIO.setup(pinOuts[combos[outLED*2]], GPIO.OUT)
            GPIO.setup(pinOuts[combos[outLED*2+1]], GPIO.OUT)
            GPIO.output(pinOuts[combos[outLED*2]], GPIO.HIGH)
            GPIO.output(pinOuts[combos[outLED*2+1]], GPIO.LOW)
            time.sleep(0.002 / len(outLEDs)) #The total time it takes to cycle through the outLEDs array should always be ~2 milliseconds
            GPIO.output(pinOuts[combos[outLED*2]], GPIO.LOW) #Prevents voltage spikes from causing unintentional activations
            tally += 1
        if time.time() > outTime: break
except KeyboardInterrupt:
    print("Stopped by User")

GPIO.cleanup()


