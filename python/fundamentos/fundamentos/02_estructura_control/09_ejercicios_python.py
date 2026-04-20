""" 1. Números Pares Dinámicos
Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos."""
def numerosDinamicos():
    n = int(input("Ingrese la cantidad de números pares que desea ver: "))
    pares = []
    for i in range(1, (n * 2) + 1):
        if i % 2 == 0:
            pares.append(i)
    print(f"Mostrando pares: {pares}")

""" 2. Verificador de Edad y Acceso
Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad."""
def verificarEdad():
    nacimiento = int(input("Ingrese su año de nacimiento: "))
    anio_actual = 2026
    calculo = anio_actual - nacimiento 

    if calculo >= 18:
        print("Eres mayor de edad.")
    else:
        faltan = 18 - calculo
        print("Eres menor de edad.")
        print(f"Te faltan {faltan} años para ser mayor de edad.")

""" 3. Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final."""

def aplicarDescuento():
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    producto = precio * cantidad
    if producto > 100:
        descuento = producto * 0.15
    else:
        descuento = 0
        total = producto - descuento
        print(f"El subtotal es: ${producto}. el descuento aplicado es: ${descuento} y el total final es: ${total}")

""" 4. Clasificador de Números  
Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero."""
def clasificadorNum():
    num = int(input("Ingrese un número: "))
    if num > 0:
        if num % 2 == 0:
            print("Positivo-par")
        elif num % 2 == 1:
            print("Positivo-impar")




""" 5. Tabla de Multiplicar Personalizada
Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra los resultados que sean múltiplos de 3."""

def tabladeMultiplicar():
    num = int(input("Ingrese número a trabajar: "))
    for i in range (1, 13):
        resultado = num * i
        if resultado % 3 == 0:
            print(f"del {num} solo estos números son divisibles por 3: {resultado}")

# 6. Sumatoria con Centinela
# Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo)."""

def sumaCentinela():
    suma_total = 0
    while True:
        n = int(input("Ingrese un número (negativo para salir): "))
        if n < 0:
            break
        suma_total += n
        print(f"la suma total es: {suma_total}")

# 7. Contador de Vocales
# Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total."""


continuar = True    
while continuar:
    print("---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    print("---Ejercicio 7---")
    print("---Ejercicio 8---")
    print("---Ejercicio 9---")
    print("---Ejercicio 10---")
    print("---Ejercicio 11---")
    print("---Ejercicio 12---")
    print("---Ejercicio 13---")
    print("---Ejercicio 14---")
    print("---Ejercicio 15---")

    opcion = input("\n--- elige una opción (1-15) (0 para salir)")
    if opcion == "1":
        print("\n---Ejecutando Ejercicio 1---")
        numerosDinamicos()
    elif opcion == "2":
        print("\n---Ejecutando Ejercicio 2---")
        verificarEdad()
    elif opcion == "3":
        print("\n---Ejecutando Ejercicio 3---")
        aplicarDescuento()
    elif opcion == "4":
        print("\n---Ejecutando Ejercicio 4---")
        clasificadorNum()
    elif opcion == "5":
        print("\n---Ejecutando Ejercicio 5---")
        tabladeMultiplicar()
    elif opcion == "6":
        print("\n---Ejecutando Ejercicio 6---")
        tabladeMultiplicar()
    elif opcion == "0":
        print("\n---Saliendo del programa---")
        continuar = False
    else:
        print("\n---Opción no válida, por favor intente otra vez---")