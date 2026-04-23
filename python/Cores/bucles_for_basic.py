"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)
def generadorNiveles():
    for num in range(1, 100 + 1):
        print(num)

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)
def potenciadoresEnergia():
    n = 250
    pares = []
    for i in range(1, (n * 2) + 1):
        if i % 2 == 0:
            pares.append(i)
    print(f"Mostrando pares: {pares}")

# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)

def trampaEmojis():
    for num in range(1, 100 + 1):
        if num % 5 == 0:
            print(num)
        if num % 10 == 0:
            print(num)

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)

def sumaColosal():
    suma_total = 0

    for num in range(0, 500000 + 1):
        if num % 2 == 0:
            suma_total += num

    print(f"La suma total de los numeros pares del 0 al 500,000 es: {suma_total}")

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)

def retrocesoTemporal():
    for num in range(2024, -1, -3): 
        print(num)

# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)

def contadorDinamico():
    inicio = 3
    fin = 10
    salto = 2

    for num in range(inicio, fin + 1, salto):
        print(num)


# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

continuar = True    
while continuar:
    print("---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    
    opcion = input("\n--- elige una opción (1-15) (0 para salir)")
    if opcion == "1":
        print("\n---Ejecutando Ejercicio 1---")
        generadorNiveles()
    elif opcion == "2":
        print("\n---Ejecutando Ejercicio 2---")
        potenciadoresEnergia()
    elif opcion == "3":
        print("\n---Ejecutando Ejercicio 3---")
        trampaEmojis()
    elif opcion == "4":
        print("\n---Ejecutando Ejercicio 4---")
        sumaColosal()
    elif opcion == "5":
        print("\n---Ejecutando Ejercicio 5---")
        retrocesoTemporal()
    elif opcion == "6":
        print("\n---Ejecutando Ejercicio 6---")
        contadorDinamico()
    elif opcion == "0":
        print("\n---Saliendo del programa---")
        continuar = False
    else:
        print("\n---Opción no válida, por favor intente otra vez---__")
        