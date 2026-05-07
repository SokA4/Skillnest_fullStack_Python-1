"""Crear una función que reciba una lista de números y genere una nueva lista sin elementos repetidos.
 Luego debe mostrar la lista original y la lista resultante. sin usar split"""

import os


def crear_lista_original(lista):
    lista_sin_repetidos = []
    for numero in lista:
        if numero not in lista_sin_repetidos:
            lista_sin_repetidos.append(numero)
    return lista_sin_repetidos
lista_original = [1, 2, 3, 4, 2, 5, 1, 6]
lista_resultante = crear_lista_original(lista_original)

def ejercicio():
    resultado = crear_lista_original(lista_original)
    print(f"Lista original: {lista_original}")
    print(f"Lista resultante sin elementos repetidos: {resultado}")
    


def limpiar_consola():
   os.system('cls')

continuar = True    
while continuar:
    print("---Ejercicios Python---")
    print("---Ejercicio 1---")

    opcion = input("\n--- elige una opción (1-15) (0 para salir)")
    if opcion =="1":
        limpiar_consola()
        print("\nEjecutando ejercicio 1: ")
        ejercicio()
        continuar = False
    elif opcion == "0":
        print("\n---Saliendo del programa---")
        continuar = False
    else:
        print("\n---Opción no válida, por favor intente otra vez---")
