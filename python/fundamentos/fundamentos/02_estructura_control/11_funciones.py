def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado

def buenos_dias(nombre):
   print("Buenos días "+nombre)

   buenos_dias("alegría")
   buenos_dias("al amor")
   buenos_dias("a la vida")
   buenos_dias("señor Sol")    

def buenos_dias(nombre):
   return "Buenos días "+nombre

#El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese

frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python
