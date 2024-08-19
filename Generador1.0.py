#MENU
print('....//Generador de onda Cuadrada//...')
print()
x=int(input('Coordenada del eje x: '))
f=float(input('Frecuencia (Hz): '))
Vpp=float(input(' Voltaje (Vpp): '))
duty_porc=float(input('Ciclo util: '))
offset=int(input('Offset: '))
print()

#OPERACIONES
Periodo=1/f
t=x/512

#Condicional
if t % Periodo <= duty_porc/(100*f):
    Amplitud=Vpp/2 + offset
    PixelY=(-6.4*Amplitud)+64
    print('Amplitud de ',Amplitud,' voltios; Pixel ',PixelY,' en el eje Y')   
else:
    Amplitud=-Vpp/2 + offset
    PixelY=(-6.4*Amplitud)+64
    print('Amplitud de ',Amplitud,' voltios; Pixel ',PixelY,' en el eje Y')  
    

