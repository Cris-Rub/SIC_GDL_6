import RPi.GPIO as GPIO
from pirc522 import RFID
import time

# Configuración de pines
TRIGGER_PIN = 23
ECHO_PIN = 24
RED_LED_PIN = 17
YELLOW_LED_PIN = 27
GREEN_LED_PIN = 22

# Configuración de los GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

# Funciones para controlar el sensor ultrasónico
def read_ultrasonic_sensor():
    # Necesitamos que funcione el sensor
    pass

# Funciones para controlar el sensor RFID
def read_rfid():
    # Necesitamos que funcione el sensor
    pass

def write_user_data(uid, word, user):
    with open('datos.txt', 'a') as file:
        file.write(f"UID: {uid}, Palabra: {word}, Usuario: {user}\n")
    print("Datos guardados exitosamente.")

def read_user_data():
    try:
        with open('datos.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No hay datos disponibles.")

# Funciones para el modo escritura y lectura
def modo_escritura():
    while True:
        if read_ultrasonic_sensor():
            uid = read_rfid()
            if uid:
                word = input("Ingresa una palabra: ")
                user = input("Ingresa el nombre de usuario: ")
                write_user_data(uid, word, user)
                print("Datos guardados exitosamente.")
            else:
                print("No se detectó una tarjeta RFID válida.")

def modo_lectura():
    while True:
        if read_ultrasonic_sensor():
            uid = read_rfid()
            if uid:
                user_data = read_user_data()
                if user_data:
                    print("Palabra y usuarios asignados:")
                    for data in user_data:
                        print(f"UID: {data[0]}, Palabra: {data[1]}, Usuario: {data[2]}")
                    GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
                    time.sleep(5)
                    GPIO.output(GREEN_LED_PIN, GPIO.LOW)
                else:
                    print("No hay datos disponibles.")
            else:
                print("No se detectó una tarjeta RFID válida.")
                GPIO.output(RED_LED_PIN, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(RED_LED_PIN, GPIO.LOW)

try:
    # Inicio
    while True:
        opcion = input("Ingresa 'E' para modo escritura, 'L' para modo lectura, o 'exit' para salir: ")
        if opcion == 'E' or opcion == 'e':
            modo_escritura()
        elif opcion == 'L' or opcion == 'l':
            modo_lectura()
        elif opcion == 'exit':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
except KeyboardInterrupt:
    print("\nInterrupción del teclado. Saliendo del programa...")
finally:
    GPIO.cleanup()
