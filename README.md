# 2526CL9_salida_PWMyMasPotencia

Salidas pseudo-analógicas PWM y como controlar mas Potencia

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/2526_PyR_Index: Curso Programación y Robotica 2025 2026 - CMM BML](https://github.com/Jcspoza/2526_PyR_Index)

## Clase 9 - Indice

- Propuesta de estudio : entradas analógicas en micro Controladores

- Materiales y links a información
  
  * Lista de materiales
  
  * Links a Tutoriales  e informacion
  - Librerías importantes - No necesarias

- Aprender / Entender: entradas analógicas en micro Controladores
  
  - Intro Teórica breve a los ADC´s
  
  - 1er montaje : Divisor de tensión
  
  - 2do Montaje : Potenciómetro
  
  - 3ro Montaje : LDR
  
  - 4to Montaje : 

- Lista (no completa) de sensores analógicos en robotica

- Proyecto completo: por decidir

- Tabla resumen de programas

- TO DO y Notas

## Propuesta de estudio : salidas pseudo-analógicas en micro Controladores => PWM + controlar mas potencia

Más que un proyecto para ir construyendo, esta Clase #9 será un estudio de como disponer de salidas pseudo-analogicas con el método de modulación del ancho del ciclo de trabajo ( PWM) dentro del rango de voltajes de la PICO 0 a 3.3 volt

## Materiales y links a información

Materiales y links a informacion

| Material                                                                                                               | Descripcion                                                                                                                                                      | Kit SF |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| [Protoboard 700](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_breadboard.html)        | Placa para prototipos ver apartado [Uso de la protoboard](https://github.com/Jcspoza/2526CL1_R_CircElect0#uso-de-la-protoboard). Mejor usar la protoboard de 700 | SI     |
| [Cables dupond M-M](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_wire.html)           | Sirven para hacer conexiones en protoboard                                                                                                                       | SI     |
| [Led rojo](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_led.html)                    | Se usara para indicar comienzo de cuenta de Tiempo de reacción                                                                                                   | SI     |
| [Resistencia 220 ohm x1](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_resistor.html) | Resistencia 220 ohm para limitar corriente de LED                                                                                                                | SI     |
|                                                                                                                        |                                                                                                                                                                  |        |
|                                                                                                                        |                                                                                                                                                                  |        |
|                                                                                                                        |                                                                                                                                                                  |        |
|                                                                                                                        |                                                                                                                                                                  |        |

### Fotos del montaje final

| <img src="./doc/LDRrele_detalle.jpg" title="" alt="" width="398"> | <img title="" src="./doc/LDRreleEncendido.jpg" alt="" width="398"> | <img title="" src="./doc/LDRreleApagado.jpg" alt="" width="398"> |
| ----------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- |

### Librerías importantes - No son necesarias en CL6

## Aprender / Entender: salidas pseudo-analógicas en micro Controladores PWM

### Intro Teórica breve a los DAC, el protocolo I2S y la modulación PWM

#### DAC´s y protocolo i2S

El mundo real es analógico, luego si queremos controlarlo con electrónica programable (=microcontroladores), **tenemos que poder 'escribir'  informacion analógica** y viceversa ( ver clase 6 de este curso)

Por eso, no es raro que desde el inicio los micro Controladores tuvieran entradas que podían convertir la informacion analógica, normalmente un valor de voltaje, en informacion digital: el controlador Arduino UNO R3 ( lanzado en 2011)  tiene 6 entradas analógicas directas, o ADC´s. 

La conversión contraria, que es la que vamso a ver en esta Clase, **desde digital a analógico o DAC no es común en los uControladores porque priorizan la funcionalidad básica el bajo costo y el bajo consumo**.

--> El microcontrolador PICO _/ W /2 / 2W no dispone de DAC´s

--> Algunos modelo del micro controlador ESOP32 disponen de 2 DAC´s pero tiene una resolución de 8 -bits, muy baja para dar una mínima calidad

Para aplicaciones de alta fidelidad o velocidad (audio, video), un DAC externo ofrece mejor rendimiento, precisión, flexibilidad y diseño modular.

La comunicación de los micro-controladores con un DAC externo se realiza normalmente con un protocolo digital llamado **I2S**. Es un tema extenso y requiere comprar micrófonos y/o DAC´s i2c. Toda la familia PICO puede comunicarse en I2S y en micropython hay una libreria para ello, y esta disponible y estable desde la version de micropython 1.20



Si tienes curiosidad mira el excelente tutorial 

[GitHub - miketeachman/micropython-i2s-examples: Examples for I2S support on microcontrollers that run MicroPython](https://github.com/miketeachman/micropython-i2s-examples)



#### Conceptos a conocer modulacion PWM

-- ME QUEDE AQUI--



### 1er montaje : Cambiar brillo de un led por PWM





## Proyecto completo: en inicio de pruebas : sensor humedad suelo + bomba agua (moto)

Esta lección forma parte del los aprendizajes necesarios para controlar cargas analógicas de cierta potencia como un motor

## Tabla resumen de programas

| Programa | Lenguaje | HW si Robotica y Notas | Objetivo de Aprendizaje |
| -------- | -------- | ---------------------- | ----------------------- |
|          | uPy      |                        |                         |
|          | uPy      |                        |                         |
|          | uPy      |                        |                         |
|          | uPy      |                        |                         |
|          | uPy      |                        |                         |
|          | uPy      |                        |                         |

---

## TO DO y Nota

- Todo: 
