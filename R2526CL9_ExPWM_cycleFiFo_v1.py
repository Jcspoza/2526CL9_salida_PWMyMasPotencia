# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 3 - 6
# Goal : External LED in GPIO15 - cyclic fadding
# Ref : https://www.coderdojotc.org/micropython/basics/04-fade-in-and-out/

from machine import Pin, PWM
from utime import sleep

# Informative block - start
p_ucontroler = "Pico W"
p_keyOhw = "Led + resistor on GPIO15"
p_project = "External LED - cyclic fadding"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

EXTERNAL_LED_PIN = 15
pwm_led = PWM(Pin(EXTERNAL_LED_PIN))
pwm_led.freq(1000)

try: # try fuera del bucle porque quiero que se dentenga y no reanude
    while (True):
        for duty in range(65025):
            pwm_led.duty_u16(duty)
            sleep(0.0001)
        for duty in range(65025, 0, -1):
            pwm_led.duty_u16(duty)
            sleep(0.0001)
            
except KeyboardInterrupt:
    pwm_led.duty_u16(0)
    pwm_led.deinit()
    print('Programa de ciclo de subida y bajada de brillo - Detenido')
        
