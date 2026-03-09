# Taller Programación y Robótica en CMM BML – 2024-2025 - Dodow
# Programa: Controlar MOTOR a 9 volt desde 3,3 volt con Transistor BJC por PWM
# por entrada analógica en PICO
# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2026 03
# Goal : potenciometer reading to control motor by PWM
# Learning Target : control a motor
# Librerias : Ninguna
# Ref librerias: 
# Licencia : CC BY-NC-SA 4.0
# REf basica https://dmccreary.github.io/learning-micropython/basics/04-fade-in-and-out/
# Ref : Get started with MicroPython on Raspberry Pi Pico, cap 8 Reading a potentiometer

from machine import ADC, Pin, PWM
from time import sleep

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External potenciometer on GPIO26 ADC0 + motor & tnn on GPIO15"
p_project = "Potenciometer control speed moptro by PWM"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0.1- Crea el objeto ADC que conecta el pin central
# del potenciometro a adc0 = gpio 26
# Los otros 2 pines a +3.3 y 0 volt respectivamente

POTENCIOMETRO_ADC = 0 # es el ADC0
potentiometer = machine.ADC(POTENCIOMETRO_ADC)

# 0.2- Crea un PWM en GPÎO15 a 1khz
MOTOR_PIN = 15
pwm_motor = PWM(Pin(MOTOR_PIN))
pwm_motor.freq(1000)

LOWP100 = 15 # menor valor para que el motro gire
por100 = 20 # fijamos inicialmente a 20% de la velocidad
# pasamos a dutty cicle  de 0 a 65 000
por60mil = int(65535 * por100 / 100)
pwm_motor.duty_u16(por60mil)

# 1- Bucle de lectura del potenciometro y 'lectura' del motor
try: # try fuera del bucle porque quiero que se dentenga y no reanude
    while (True):
        potvalueRaw = potentiometer.read_u16()
        por100 = int((potvalueRaw / 65535) * 100 )
        print(f"Porcentaje leido = {por100:2d} %")
        if por100 < LOWP100: # menor valor para que el motro gire
            potvalueRaw = int(65535 * LOWP100 / 100)
            print(f"Porcentaje truncado al minimo de {LOWP100:2d} %")
            
        sleep(.2)
        pwm_motor.duty_u16(potvalueRaw)
       
        
except KeyboardInterrupt:
    pwm_motor.duty_u16(0)
    pwm_motor.deinit()
