import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

last_value=GPIO.input(18)
v=[]
i=10
t1=time.clock_gettime_ns(0)
while i:
    #t1=time.clock_gettime_ns(0)
    #t1 = time.process_time()
    #t1=time.monotonic()
    if GPIO.input(18) != last_value:
        #t2=time.clock_gettime_ns(1)
        #t2=time.process_time()
        #t2=time.monotonic()
        v.append(time.clock_gettime_ns(0)-t1)
        print(v[-1])
        t1=time.clock_gettime_ns(0)
        last_value=GPIO.input(18)
        #print(t2-t1)
        #v.append(t2-t1)
        i=i-1

print(v)
