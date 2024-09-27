import math

def calcular_coordenadas_cinematica(longitudes, angulos):
    """
    Calcula las coordenadas de los segmentos de un sistema articulado en 2D.
    
    Parámetros:
    - longitudes: una lista con las longitudes de los segmentos [A2, A3].
    - angulos: una lista con los ángulos [O2, O3] en grados.
    
    Retorna:
    - Una tupla con las coordenadas (X2, Y2) para el extremo del segmento A2
      y (X3, Y3) para el extremo del segmento A3.
    """
    A2, A3 = longitudes
    O2, O3 = angulos
    
    # Convertir los ángulos a radianes
    O2_rad = math.radians(O2)
    O3_rad = math.radians(O3)
    
    # Calcular las coordenadas del extremo del segundo segmento
    X2 = math.sin(O2_rad) * A2
    Y2 = math.cos(O2_rad) * A2
    
    # Manejar caso de Y2 = 0 para evitar división por cero
    if Y2 == 0:
        ang_aux = math.pi / 2 if X2 > 0 else -math.pi / 2
    else:
        ang_aux = math.atan(X2 / Y2)
    
    # Calcular el ángulo auxiliar y las coordenadas del tercer segmento
    angulo_total = math.pi - O3_rad - ang_aux
    X3 = math.sin(angulo_total) * A3
    Y3 = math.cos(angulo_total) * A3
    
    return (X2, Y2, X3, Y3)

# Ejemplo de uso
longitudes = [10, 5]  # Longitudes A2 y A3
angulos = [30, 45]    # Ángulos O2 y O3 en grados

resultados = calcular_coordenadas_cinematica(longitudes, angulos)
print("Coordenadas calculadas:", resultados)
