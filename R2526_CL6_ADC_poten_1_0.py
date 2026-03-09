# Hardware platform: Pico W & Pico
# Author : JC Santamaria 
# Date : 2023 - 5 - 11
# Goal : potenciometer reading basic
# Learning Target : Analog digital converter basic
# Ref : Get started with MicroPython on Raspberry Pi Pico, cap 8 Reading a potentiometer

from machine import ADC
from time import sleep

# Informative block - start
p_ucontroler = "Pico W & Pico _"
p_keyOhw = "External potenciometer on GPIO26 ADC0"
p_project = "Potenciometer basic reading with ADC0"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end


# 1- Crea el objeto ADC que conecta el pin central
# del potenciometro a adc0 = gpio 26
# Los otros 2 pines a +3.3 y 0 volt respectivamente

POTENCIOMETRO_ADC = 0 # es el ADC0
potentiometer = machine.ADC(POTENCIOMETRO_ADC)
FACTOR_CONVERSION = 3.245 / (65535)

# 2- Bucle de lectura
while True:
    potvalueRaw = potentiometer.read_u16()
    voltios = potvalueRaw * FACTOR_CONVERSION
    # print(f"Voltaje leido = {voltios:.3f} voltios | Valor ADC bruto = {potvalueRaw}")
    print(f"Voltaje leido = {voltios:.2f} voltios")
    sleep(.2)
    
