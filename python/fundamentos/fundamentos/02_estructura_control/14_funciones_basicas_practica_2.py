import os 
def multiplica_por_2(num):
   resultado = []
   for i in range(num + 1 ):
      resultado.append(i * 2)
   return resultado
def ejercicio1():
   resultado = multiplica_por_2(5)
   print(resultado)
   

def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    print(f"suma: {suma}")
    return resta

def ejercicio2():
    resta = suma_y_resta([120, 115])
    print(f"resta: {resta}")


def sumatoria_menos_longitud(sumatoria):
   total = sum(sumatoria)
   longitud = len(sumatoria)
   resultado = total - longitud
   print(f"Total = {total}, Longitud = {longitud}")
   return resultado
def ejercicio3():
   retornar = sumatoria_menos_longitud([10, 5, 3, 7])
   print(f"Resultado: {retornar}")


def valores_multiplicados_segundo(lista):
   

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

