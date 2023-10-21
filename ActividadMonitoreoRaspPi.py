from gpiozero import LED
import psutilfrom time import sleep
from datetime import datetime
led_yellow = LED(20)
led_red = LED(21)
file=open("log.txt","Y")