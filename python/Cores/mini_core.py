datos = [
   {"nombre": "Carlos", "puntaje": 80},
   {"nombre": "MarIa", "puntaje": 95},
   {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
print(datos[2]["nombre"])  # Imprime el nombre de pedro
datos[2]["puntaje"] = 75
print(datos[2]["puntaje"])  # Imprime el nuevo puntaje de pedro

# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"

def puntaje_carlos():
    for dato in datos:
        print(f"{dato['nombre']} obtuvo {dato['puntaje']} puntos")
        break 
puntaje_carlos()

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def imprimir_valores(nombre):
    input_nombre = input("Ingrese el nombre que desea imprimir: ")
    for dato in datos:
        if input_nombre == dato["nombre"]:
                print(f"{dato['nombre']} obtuvo {dato['puntaje']} puntos")
imprimir_valores("nombre")


