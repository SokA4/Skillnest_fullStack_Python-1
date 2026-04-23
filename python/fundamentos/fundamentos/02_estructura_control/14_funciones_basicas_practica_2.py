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
   if len(lista) < 2:
      print(len(lista))
      return []
   else :
      segEle = lista[1]
      nueva_lista = []
      for num in lista:
         nueva_lista.append(num * segEle)
      longitud = len(nueva_lista)
      print(longitud)
      return nueva_lista
   
def ejercicio4():
   result1 = valores_multiplicados_segundo([100, 3, 50, 20])
   print(result1)
   print()
   result2 = valores_multiplicados_segundo([100])
   print(result2)



def valor_multiplicado_longitud(a, b):
    multiList = []
    for i in range(0, b):
       multiList.append(a * b)
       return multiList
    
def ejercicio5():
   resultado = valor_multiplicado_longitud(5, 2)
   print(f"Resultado 1: {resultado}")
   resultado2 = valor_multiplicado_longitud(7, 5)
   print(f"Resultado 2: {resultado2}")



def limpiar_consola():
   os.system('cls')
# --- MENÚ (afuera de las funciones) ---

# Menú de navegación para ejercicios
continuar = True
while continuar:
    print("\n--- Ejercicios Python ---")
    print("--- Ejercicio 1: ---")
    print("--- Ejercicio 2: ---")
    print("--- Ejercicio 3: ---")
    print("--- Ejercicio 4: ---")
    print("--- Ejercicio 5: ---")
    opcion = input("\nElige una opción (1-5) (0 para salir) = ")
    if opcion =="1":
        limpiar_consola()
        print("\nEjecutando ejercicio 1: ")
        ejercicio1()
    elif opcion =="2":
        limpiar_consola()
        print("\nEjecutando ejercicio 2: ")
        ejercicio2()
    elif opcion =="3":
        limpiar_consola()
        print("\nEjecutando ejercicio 3: ")
        ejercicio3()
    elif opcion =="4":
        limpiar_consola()
        print("\nEjecutando ejercicio 4: ")
        ejercicio4()
    elif opcion =="5":
        limpiar_consola()
        print("\nEjecutando ejercicio 5: ")
        ejercicio5()
    else:
        limpiar_consola()
        print("Opción no válida, intenta otra vez")

