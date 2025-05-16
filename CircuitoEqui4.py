import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def calcular():
    try:
        # Datos del transformador
        V_alta = float(entry_valta.get())
        V_baja = float(entry_vbaja.get())
        frecuencia = float(entry_frecuencia.get())
        kva = float(entry_kva.get())

        # Datos de prueba de vacío
        seleccion_vacio = var_vacio.get()
        Vcab = float(entry_vcab.get())
        Icab = float(entry_icab.get())
        Pcab = float(entry_pcab.get())

        # Datos de prueba de cortocircuito
        seleccion_corto = var_corto.get()
        Vcc = float(entry_vcc.get())
        Icc = float(entry_icc.get())
        Pcc = float(entry_pcc.get())

        # Datos de regulación de tensión
        Fp = float(entry_hp.get())
        tipo = tipo_carga.get()
        cargabilidad = float(entry_cargabilidad.get())

        # Cálculos Generales
        Rp = Pcc/ (Icc**2)
        Zp = Vcc / Icc
        teta = math.acos(Rp / Zp)
        Xp = Zp*math.sin(teta)
        
        a1 = V_alta / V_baja
        Rs=Rp/(a1**2)
        Zs=Zp/(a1**2) 
        Xs = Xp / (a1**2)
        
        Ins = (kva*10**3)/V_baja
        
        
        Y = Icab / Vcab
        Fp1 = Pcab / (Vcab * Icab)
        O = math.acos(Fp1)
      
        #Z = Vcc / Icc
        #Fp2 = Pcc / (Vcc * Icc)
        #Q = math.acos(Fp2)
       

       
        
        # Determinar a qué lado se refiere la impedancia
        if seleccion_corto == "Primario":
            referido_a = "Primario"    
            
            Y = Icab / Vcab
            Fp1 = Pcab / (Vcab * Icab)
            O = math.acos(Fp1)  
            Rc = (Y * math.cos(O))**-1
            Xm = (Y * math.sin(O))**-1
            Rcf=((a1**2)*Rc)*10**-3
            Xmf=((a1**2)*Xm)*10**-3
            
            Z = Vcc / Icc
            Fp2 = Pcc / (Vcc * Icc)
            Q = math.acos(Fp2)
            Req= (Z*math.cos(Q))
            Xeq= (Z*math.sin(Q))
        
        else:
            referido_a = "secundario"            
            Y = Icab / Vcab
            Fp1 = Pcab / (Vcab * Icab)
            O = math.acos(Fp1)  
            Rc = (Y * math.cos(O))**-1
            Xm = (Y * math.sin(O))**-1
            Rcf=((a1**2)*Rc)*10**-3
            Xmf=((a1**2)*Xm)*10**-3
            
            Z = Vcc / Icc
            Fp2 = Pcc / (Vcc * Icc)
            Q = math.acos(Fp2)
            Req= (Z*math.cos(Q))
            Xeq= (Z*math.sin(Q))
             
        # Cálculo de regulación
        if tipo == "Adelantado":
            Mag = Ins*Zs
            tetaf = teta - math.acos(Fp)
            E2Sen = V_baja + (Mag*math.cos(tetaf))
            E2Cos = Mag*math.sin(tetaf)
            E2 = math.sqrt((E2Sen**2)+(E2Cos**2))
            porcentaje_reg = ((E2- V_baja)*cargabilidad)/V_baja
        else:
            Mag = Ins*Zs
            tetaf = teta + math.acos(Fp)
            E2Sen = V_baja + (Mag*math.cos(tetaf))
            E2Cos = Mag*math.sin(tetaf)
            E2 = math.sqrt((E2Sen**2)+(E2Cos**2))
            porcentaje_reg = ((E2- V_baja)*cargabilidad)/V_baja

        resultado = (
            f"Circuito Equivalente\n"
            f"Referido al: {referido_a}\n"
            f"Req = {Req:.2f}Ω\n"
            f"jXeq = {Xeq:.2f}Ω\n"
             f"Rc = {Rcf:.2f}Ω\n"
            f"jXm = {Xmf:.2f}Ω\n"
            f"Rp = {Rp:.2f}Ω  Rs = {Rs:.2f}Ω\n"
            f"jXp = {Xp:.2f}Ω  jXs = {Xs:.2f}Ω\n"
            f"Regulación De tensión = {porcentaje_reg:.2f} %"
        )

        messagebox.showinfo("Resultados", resultado)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Interfaz
root = tk.Tk()
root.title("Prueba de Transformadores")

# Variables globales
tipo_carga = tk.StringVar()

# ======= Datos del transformador ========
frame_datos = ttk.LabelFrame(root, text="Datos del Transformador")
frame_datos.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

ttk.Label(frame_datos, text="Voltaje de Alta (V) :").grid(row=0, column=0)
entry_valta = ttk.Entry(frame_datos)
entry_valta.grid(row=0, column=1)

ttk.Label(frame_datos, text="Voltaje de Baja (V) :").grid(row=0, column=2)
entry_vbaja = ttk.Entry(frame_datos)
entry_vbaja.grid(row=0, column=3)

ttk.Label(frame_datos, text="Frecuencia (Hz) :").grid(row=1, column=0)
entry_frecuencia = ttk.Entry(frame_datos)
entry_frecuencia.grid(row=1, column=1)

ttk.Label(frame_datos, text="Potencia (KVA) :").grid(row=1, column=2)
entry_kva = ttk.Entry(frame_datos)
entry_kva.grid(row=1, column=3)

# ======= Prueba de Vacío ========
frame_vacio = ttk.LabelFrame(root, text="Prueba de Vacío")
frame_vacio.grid(row=1, column=0, padx=10, pady=10)

var_vacio = tk.StringVar()
ttk.Label(frame_vacio, text="Lado :").grid(row=0, column=0)
ttk.Combobox(frame_vacio, textvariable=var_vacio, values=["Primario", "Secundario"]).grid(row=0, column=1)

ttk.Label(frame_vacio, text="Vcab (V) :").grid(row=1, column=0)
entry_vcab = ttk.Entry(frame_vacio)
entry_vcab.grid(row=1, column=1)

ttk.Label(frame_vacio, text="Icab (A) :").grid(row=2, column=0)
entry_icab = ttk.Entry(frame_vacio)
entry_icab.grid(row=2, column=1)

ttk.Label(frame_vacio, text="Pcab (W) :").grid(row=3, column=0)
entry_pcab = ttk.Entry(frame_vacio)
entry_pcab.grid(row=3, column=1)

# ======= Prueba de Cortocircuito ========
frame_corto = ttk.LabelFrame(root, text="Prueba de Cortocircuito")
frame_corto.grid(row=1, column=1, padx=10, pady=10)

var_corto = tk.StringVar()
ttk.Label(frame_corto, text="Lado :").grid(row=0, column=0)
ttk.Combobox(frame_corto, textvariable=var_corto, values=["Primario", "Secundario"]).grid(row=0, column=1)

ttk.Label(frame_corto, text="Vcc (V) :").grid(row=1, column=0)
entry_vcc = ttk.Entry(frame_corto)
entry_vcc.grid(row=1, column=1)

ttk.Label(frame_corto, text="Icc (A) :").grid(row=2, column=0)
entry_icc = ttk.Entry(frame_corto)
entry_icc.grid(row=2, column=1)

ttk.Label(frame_corto, text="Pcc (W) :").grid(row=3, column=0)
entry_pcc = ttk.Entry(frame_corto)
entry_pcc.grid(row=3, column=1)

# ======= Regulación de Tensión ========
frame_regulacion = ttk.LabelFrame(root, text="Regulación de Tensión")
frame_regulacion.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

ttk.Label(frame_regulacion, text="Factor de Potencia :").grid(row=0, column=0)
entry_hp = ttk.Entry(frame_regulacion)
entry_hp.grid(row=0, column=1)

ttk.Label(frame_regulacion, text="Tipo :").grid(row=1, column=0)
combo_tipo = ttk.Combobox(frame_regulacion, textvariable=tipo_carga, values=["Adelantado", "Atrasado"])
combo_tipo.grid(row=1, column=1)

ttk.Label(frame_regulacion, text="Cargabilidad (%) :").grid(row=2, column=0)
entry_cargabilidad = ttk.Entry(frame_regulacion)
entry_cargabilidad.grid(row=2, column=1)

# Botón de cálculo
btn_calcular = ttk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
