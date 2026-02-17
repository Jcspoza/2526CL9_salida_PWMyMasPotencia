# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 2 - 17
# Goal : Blink external LED in GPIO16
# Ref : https://www.coderdojotc.org/micropython/basics/03-blink/

# import machine, no hace falta solo para Pin

from machine import Pin # Get the Pin function from the machine module.
from utime import sleep # Get the sleep library from the time module.

# Informative block - start
p_ucontroler = "Pico W"
p_keyOhw = "Led + resistor on GPIO15"
p_project = "External LED toggle 2sec"
p_version = "1.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# -> 1.2 uso de toggle
# Informative block - end

EXTERNAL_LED_PIN = 15
ext_led = Pin(EXTERNAL_LED_PIN, Pin.OUT)

while (True):
    ext_led.toggle()
    print("External LED - gpio15 = ",ext_led.value())
    sleep(2)