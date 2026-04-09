#1. Números Pares Dinámicos 
# Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). El programa debe imprimir los primeros $n$ números pares positivos.

par = int(input("¿Cuántos números pares deseas ver? "))
for i in range(1, par + 1):
    print(i * 2)