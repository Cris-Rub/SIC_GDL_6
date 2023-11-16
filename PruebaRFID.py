#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO  # Importa la biblioteca para controlar los GPIOs
from pirc522 import RFID
import time

GPIO.setmode(GPIO.BOARD)  # Define el modo de numeración (Board)
GPIO.setwarnings(False)  # Desactiva los mensajes de alerta

rc522 = RFID()  # Instancia la lib

print("En attente d'un badge (pour quitter, Ctrl + c): ")  # Muestra un mensaje pidiendo al usuario que pase su tarjeta

# Bucle infinito para leer continuamente
while True:
    rc522.wait_for_tag()  # Espera a que una tarjeta RFID esté dentro del rango
    (error, tag_type) = rc522.request()  # Cuando se ha leído una tarjeta, se recuperan sus datos

    if not error:  # Si no hay errores
        (error, uid) = rc522.anticoll()  # Se manejan las posibles colisiones, que ocurren si varias tarjetas pasan al mismo tiempo

        if not error:  # Si se ha limpiado correctamente
            print("Vous avez passé le badge avec l'id : {}".format(uid))  # Muestra el identificador único de la tarjeta RFID
            time.sleep(1)  # Espera 1 segundo para no leer la tarjeta cientos de veces en milisegundos
