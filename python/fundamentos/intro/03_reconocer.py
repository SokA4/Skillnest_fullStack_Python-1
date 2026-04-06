"""este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'."""


import random


nombre = "Frida Kahlo"
print(type(nombre))
print(len(nombre))


edad = 25


if edad < 18:
   print("Eres menor de edad.")
elif edad == 18:
   print("Tienes 18 años.")
else:
   print("Eres mayor de edad.")


frutas = ["manzana", "pera", "fresa"]
print(frutas[0])
frutas[0] = "banana"
frutas.append("uva")
frutas.remove("pera")


dimensiones = (200, 50)
print(dimensiones[0])


persona = { #Variable tipo objeto (object)
   "nombre": "Carlos", #Se establece un item y su respectivo valor
   "edad": 30 # Se establece un item y su respectivo valor
}
print(persona["nombre"]) #imprime el valor del item(ej: "Carlos")
persona["edad"] = 31 #Se modifica el valor del item edad a 31
persona["ciudad"] = "Santiago"#Se agrega un nuevo item con su respectivo valor
del persona["ciudad"]#Se elimina el item completo


for i in range(5):#for range: Se crea un bucle en rango 5
   print(i)
   if i == 2:#se establece condición if == 2
       continue#continue ignora el proceso y continúa.
   if i == 4:#Se establece condición if i == 4.
       break#Si i = 4 se rompe el bucle.
   print(i)#Imprime el valor de i en cada interacion.(hasta 4)


contador = 0#Se crea una variable contador tipo numerica(int)
while contador < 3:#Se crea bucle While con una condición
   print(f"while contador es: {contador}")#Imprime el contador en un mensaje concatenado con f"" string
   contador += 1#


def saludar_usuario(nombre):
   return f"Hola, {nombre}"

 
print(saludar_usuario("Francisca"))