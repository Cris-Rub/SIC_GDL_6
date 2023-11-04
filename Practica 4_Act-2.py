import RPi.GPIO as GPIO
import time
from hcsr04sensor import sensor
#ocupa este paquete pip install hc-sr04



GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Pin para el LED
GPIO.setup(22, GPIO.IN)   # Pin para el botón


log_file = open('/home/pi/Unit_Practice/distance_log.txt', 'a')

try:
   
    sr04 = sensor.Measurement(17, 18)

    while True:
        
        while not GPIO.input(22):
            time.sleep(0.1)

       
        distance = sr04.raw_distance()

        
        intervalo_deseado = 10  # en centímetros

        if distance < intervalo_deseado:
            # Enciende el LED
            GPIO.output(17, True)

        
        log_file.write(f"Distance: {distance} cm\n")
        log_file.flush()

except KeyboardInterrupt:
    pass

finally:
    # Cierra el archivo de registro y realiza una limpieza de los pines GPIO
    log_file.close()
    GPIO.cleanup()
