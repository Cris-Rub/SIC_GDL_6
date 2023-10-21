import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
<<<<<<< HEAD
GPIO.setp(17,GPIO.IN)
=======
GPIO.setup(18,GPIO.IN)
>>>>>>> 96e0ae25f393f7c6c82c4ae55b423c80191d27ab
try:
    stop = 0
    while True:
        GPIO.output(17, False)
        time.sleep(0.5)

        GPIO.output(17, True)
        time.sleep(0.00001)
        GPIO.output(17, False)

        while GPIO.input(18) == 0:
            start = time.time()

        while GPIO.input(18) == 1:
            stop = time.time()
    
        time_interval = stop - start
        distance = time_interval * 17000
        distance = round(distance, 2)
        print(f"Distance: {distance}")

except KeyboardInterrupt:
    GPIO.cleanup()
