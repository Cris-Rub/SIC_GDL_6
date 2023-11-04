import RPi.GPIO as GPIO
import time
from hcsr04sensor import sensor

# Configura los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # Pin para el LED
GPIO.setup(22, GPIO.IN)   # Pin para el botón

# Abre el archivo de registro
log_file = open('/home/pi/Unit_Practice/distance_log.txt', 'a')

try:
    # Crea un objeto del sensor ultrasónico
    sr04 = sensor.Measurement(17, 18)

    while True:
        # Espera hasta que se presione el botón
        while not GPIO.input(22):
            time.sleep(0.1)

        # Realiza la medición de distancia
        distance = sr04.raw_distance()

        # Define el intervalo deseado (ajusta este valor según tus necesidades)
        intervalo_deseado = 10  # en centímetros

        if distance < intervalo_deseado:
            # Enciende el LED
            GPIO.output(17, True)

        # Registra la distancia en el archivo de registro
        log_file.write(f"Distance: {distance} cm\n")
        log_file.flush()

except KeyboardInterrupt:
    pass

finally:
    # Cierra el archivo de registro y realiza una limpieza de los pines GPIO
    log_file.close()
    GPIO.cleanup()
