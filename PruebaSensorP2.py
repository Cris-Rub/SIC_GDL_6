import RPi.GPIO as GPIO
import time
import sys

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
last_active_time = time.time()  # Registro del tiempo del último pulso

def countPulse(channel):
    global count, last_active_time
    count += 1
    last_active_time = time.time()

def resetCounter():
    global count
    count = 0
    print("Flujo detenido. Reiniciando contador a 0.")

GPIO.add_event_detect(FLOW_SENSOR, GPIO.BOTH, callback=countPulse)

try:
    while True:
        if time.time() - last_active_time > 2:  # Si no hay actividad durante más de 2 segundos, reinicia el contador
            resetCounter()
            
        print(f"Estado del flujo: {GPIO.input(FLOW_SENSOR)}")
        print(f"Contador actual: {count}")
        time.sleep(1)

except KeyboardInterrupt:
    print('\n¡Interrupción por teclado detectada! Saliendo...')
    GPIO.cleanup()
    sys.exit()
