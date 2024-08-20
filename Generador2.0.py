#MENU
print('....//Generador de Ondas//...')
print()
Tipo_Onda=input('Seleccione un tipo de onda "Sierra","Cuadrada": ')
x=int(input('Coordenada del eje x: '))
f=float(input('Frecuencia (Hz): '))
Vpp=float(input('Voltaje (Vpp): '))
duty_porc=float(input('Ciclo util: '))
offset=int(input('Offset: '))
print()

#OPERACIONES
Periodo=1/f
t=x/512

#Condicional
if Tipo_Onda == "Cuadrada":
    if t % Periodo <= duty_porc/(100*f):
      AmplitudC=Vpp/2 + offset
      PixelYC=(-6.4*AmplitudC)+64
      print('Amplitud de ',round(AmplitudC,3),' voltios; Pixel ',int(PixelYC),' en el eje Y')   
    else:
      AmplitudC=-Vpp/2 + offset
      PixelYC=(-6.4*AmplitudC)+64
      print('Amplitud de ',round(AmplitudC,3),' voltios; Pixel ',int(PixelYC),' en el eje Y')  

elif Tipo_Onda == "Sierra":
    if t <= Periodo:
      AmplitudS=((-Vpp*f)*(t))+(Vpp/2)+offset
      PixelYS=(-6.4*AmplitudS)+64
      print('Amplitud de ',round(AmplitudS,3),' voltios; Pixel ',int(PixelYS),' en el eje Y')   
    else:
      AmplitudS=(-Vpp*f)*(t-int(t/Periodo)*Periodo)+(Vpp/2)+offset
      PixelYS=(-6.4*AmplitudS)+64
      print('Amplitud de ',round(AmplitudS,3),' voltios; Pixel ',int(PixelYS),' en el eje Y')  
else:
    print()
    
    
    #t % Periodo <= (Periodo/2) or t==0 and t!=1
    #t % Periodo >= (Periodo/2) or t==1