import os 
def multiplica_por_2():
    return [i * 2 for i in range(6)]

def suma_y_resta(lista):
    total = sum(lista)
    diferencia = abs(lista[0] - lista[1])
    print(total)
    return diferencia

def sumatoria_menos_longitud(lista):
    return sum(lista) - len(lista)

def valores_multiplicados_segundo(lista):
    print(len(lista))
    if len(lista) < 2:
        return []
    return [x * lista[1] for x in lista]

def valor_multiplicado_longitud(valor, longitud):
    return [valor * longitud] * longitud

def limpiar_consola():
   os.system('cls')
# --- MENÚ (afuera de las funciones) ---


continuar = True
while continuar:
 opcion = input("Elige una opción (1-5): ")
 if opcion == "1":
    limpiar_consola()
    print(multiplica_por_2())

 elif opcion == "2":
    limpiar_consola()
    print(suma_y_resta([120, 115]))

 elif opcion == "3":
    limpiar_consola()
    print(sumatoria_menos_longitud([10, 5, 3, 7]))

 elif opcion == "4":
    limpiar_consola()
    print(valores_multiplicados_segundo([100, 3, 50, 20]))

 elif opcion == "5":
    limpiar_consola()
    print(valor_multiplicado_longitud(5, 2))
 elif opcion == "0":
      print("Saliendo...")
      continuar = False
else:
   limpiar_consola()
   print("Opcion no Valida, intente otra vez")
