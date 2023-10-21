from gpiozero import LED, Button
from signal import pause

leds = {
    'verde': LED(17),
    'ambar': LED(18),
    'rojo': LED(19)
}

boton = Button(4)

indice_led_actual = 0
led_actual = leds['verde']
led_actual.on()

def boton_presionado():
    global indice_led_actual, led_actual

    led_actual.off()

    indice_led_actual = (indice_led_actual + 1) % len(leds)
    led_actual = list(leds.values())[indice_led_actual]

    led_actual.on()

boton.when_pressed = boton_presionado

pause()