import RPi.GPIO as GPIO
import time
import sys

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
last_pulse_time = time.time()
low_pressure_threshold = 5  # Umbral de 5 segundos sin pulsos para considerar la presión baja

def countPulse(channel):
    global count, last_pulse_time
    count += 1
    last_pulse_time = time.time()

def checkPressure():
    global last_pulse_time
    if time.time() - last_pulse_time > low_pressure_threshold:
        print("¡Presión baja!")

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

try:
    while True:
        checkPressure()
        print(f"Contador actual: {count}")
        time.sleep(1)

except KeyboardInterrupt:
    print('\n¡Interrupción por teclado detectada! Saliendo...')
    GPIO.cleanup()
    sys.exit()
