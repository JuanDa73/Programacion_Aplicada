import json

# Crear un diccionario (similar a un objeto)
usuario = {
    "nombre": "Juan",
    "edad": 30,
    "casado": True
}

# Convertir el diccionario a JSON
json_string = json.dumps(usuario)
print("JSON:", json_string)

# Convertir JSON a un diccionario
usuario2 = json.loads(json_string)
print("Nombre:", usuario2["nombre"])
print("Edad:",usuario2["edad"])
print("Casado:",usuario2["casado"])