num = 15
if num > 20:
   print("Número mayor a 20")
else:
   print("Número menor a 20")
'''
La variable num es menor a 20, por lo que el bloque de código de else será ejecutado.
Es decir que vamos a imprimir "Número menor a 20"
'''
num = 101
if num > 50:
   print("Número mayor a 50")
elif num > 100:
   print("Número mayor a 100")
else:
   print("Número menor a 10")
'''
A pesar de que num es mayor que 50 y 100, la primera condicional que se cumpla es la única que se ejecutará.
Es por eso que solo imprimirá: "Número mayor a 50"
'''
if num < 60:
   print("Número menor a 50")

#No se cumple con la condicional, por lo que no se ejecuta el bloque de código


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if num1 >= num2 and num1 >= num3:
   mayor = num1
   if num2 <= num3:
    menor = num2
   else:
    menor = num3
elif num2 >= num1 and num2 >= num3:
   mayor = num2
   if num1 <= num3:
    menor = num1
   else:
    menor = num3
else:   mayor = num3
if num1 <= num2:
        menor = num1
else:
        menor = num2
print(f"El número mayor es: {mayor} y el número menor es: {menor}")