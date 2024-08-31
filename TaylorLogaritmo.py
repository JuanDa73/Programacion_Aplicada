import math

def logaritmo_natural(x, n=100):
    if x <= 0:
        raise ValueError("El logaritmo natural solo está definido para x > 0.")
    
    # Elegimos un valor a cercano a x
    a = math.exp(1)  # elegimos e como valor de a
    y = (x / a) - 1
    
    resultado = 0
    
    # Serie de Taylor para ln(1 + y)
    for i in range(1, n + 1):
        termino = ((-1) ** (i + 1)) * (y ** i) / i
        resultado += termino
    
    # Sumar el valor de ln(a)
    resultado += 1  # ln(e) = 1
    
    return resultado

resultado = logaritmo_natural(6)
print(resultado)
