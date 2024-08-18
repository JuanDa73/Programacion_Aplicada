#MENU
print('....//Generador de onda Cuadrada//...')
print()
x=int(input('Coordenada del eje x: '))
f=float(input('Frecuencia (Hz): '))
A=float(input('Amplitud (V): '))
print()

#OPERACIONES
RangeX=(f/2)/0.001953125
Periodo=1/f
Regiones=2*Periodo



#Condicional
for i in range(0,int(Regiones+1)):
        Region = RangeX * i
        NextRegion= RangeX * (i + 1)

        if Region < x <= NextRegion:
            if i % 2 != 0:#pi
                b=-A
                PixY=(-6.35*b)+64.5
                print('Amplitud de ',int(b),' voltios ; Pixel',int(PixY),' en el eje Y')
            else:#pi/2
                a=A
                PixelY=(-6.35*a)+64.5
                print('Amplitud de ',int(a),' voltios ; Pixel',int(PixelY),' en el eje Y')
        else:
            print()          
            
        
