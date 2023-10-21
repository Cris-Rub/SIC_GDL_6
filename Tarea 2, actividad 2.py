from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor(echo=17, trigger=4, max_distance=2)
red_led = LED(27) 
yellow_led = LED(22) 
green_led = LED(18)

while True:
    distance = sensor.distance * 100 

    if distance < 20:
        red_led.on()
        yellow_led.off()
        green_led.off()
    elif distance > 80:
        red_led.off()
        yellow_led.off()
        green_led.on()
    else:
        red_led.off()
        yellow_led.on()
        green_led.off()

    print(f"Distancia: {distance} cm")
    sleep(1)
