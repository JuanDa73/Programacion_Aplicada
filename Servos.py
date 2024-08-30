import time
import board
import pwmio
import analogio

# Configurar los potenciometros 
potentiometer1 = analogio.AnalogIn(board.GP26)
potentiometer2 = analogio.AnalogIn(board.GP27)
potentiometer3  = analogio.AnalogIn(board.GP28)

# Configurar el PWM
pwm_servo1 = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=50)
pwm_servo2 = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=50)
pwm_servo3 = pwmio.PWMOut(board.GP13, duty_cycle=0, frequency=50)

# Definir los valores de minimos y maximos
min_duty = 1638  # 5% duty cycle de 65535 (~1 ms, 0 grados)
max_duty = 8192# 10% duty cycle de 65535 (~2 ms, 180 grados)

while True:
    # Leer los valores de los  potenciómetro (0 a 65535)
    pot_value1 = potentiometer1.value
    pot_value2 = potentiometer2.value
    pot_value3 = potentiometer3.value

    # Mapear el valor del potenciómetro(0 a 180 grados)
    angle1 = (pot_value1 / 65535) * 180
    angle2 = (pot_value2 / 65535) * 180
    angle3 = (pot_value3 / 65535) * 180

    # Convertir el ángulo al ciclo de trabajo 
    duty_cycle1 = int(min_duty + (angle1 / 180) * (max_duty - min_duty))
    duty_cycle2 = int(min_duty + (angle2 / 180) * (max_duty - min_duty))
    duty_cycle3 = int(min_duty + (angle3 / 180) * (max_duty - min_duty))

    # Aplicar el ciclo de trabajo al PWM
    pwm_servo1.duty_cycle = duty_cycle1
    pwm_servo2.duty_cycle = duty_cycle2
    pwm_servo3.duty_cycle = duty_cycle3

    # Pequeña pausa para estabilidad
    time.sleep(0.01)


