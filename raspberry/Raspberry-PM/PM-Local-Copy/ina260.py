import time
import board
import adafruit_ina260

i2c = board.I2C()
ina260 = adafruit_ina260.INA260(i2c)
f=open('test.csv','w')
while True:
    t=0
    #print(time.clock_gettime_ns(t))
    
    f.write(str(time.clock_gettime_ns(0))+'\n')
    f.write(str(ina260.current)+','+str(ina260.voltage)+'\n')
    #print("Current: %.2f Voltage: %.2f Power:%.2f"
    #    %(ina260.current, ina260.voltage, ina260.power))
    #time.sleep(.01)
