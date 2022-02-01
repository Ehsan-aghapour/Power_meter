import time
import board
import adafruit_ina260

import signal

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
last_value=GPIO.input(18)

i2c = board.I2C()
ina260 = adafruit_ina260.INA260(i2c)
f=open('test.csv','a')
Data={'V':[],'I':[],'P':[],'Pin':[]}
    
def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    f.close()
    exit(1)
    
signal.signal(signal.SIGINT, handler)

c=0
t1=time.clock_gettime_ns(0)
while True:
    Data['V'].append(ina260.voltage)
    Data['I'].append(ina260.current)
    Data['P'].append(ina260.power)
    Data['Pin'].append(last_value)
    if GPIO.input(18) != last_value: 
        t=time.clock_gettime_ns(0)-t1
        t1=time.clock_gettime_ns(0)
        last_value=GPIO.input(18)
        f=open('test.csv','a')
        f.write(str(t)+'\n')
        for k in range(c,len(Data['V'])):
            f.write(str(Data['Pin'][k])+','+str(Data['V'][k])+','+str(Data['I'][k])+','+str(Data['P'][k])+'\n')
        c=len(Data['V'])
        f.close()   

