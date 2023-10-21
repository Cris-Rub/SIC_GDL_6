import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setp(17,GPIO.IN)\
try:
    stop = 0
    while True:
        GPIO.output(17, False)
        time.sleep(0.5)

        GPIO.output(17, True)
        time.sleep(0.00001)
        GPIO.output(17, False)

        while GPIO.input(17) == 0:
            start = time.time()

        while GPIO.input(17) == 1:
            stop = time.time()
    
    time_interval = stop - start
    distance = time_interval * 17000
    distance = round(distance, 2)
    print(f"Distance: {distance} cm")

except KeyboardInterrupt:
    GPIO.cleanup()