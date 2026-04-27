class usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):
        self.saldo_pagar += monto

#instancias de la clase
miyagi = usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.cl")
daniel = usuario("Daniel", "Larusso", "daniel@codingdojo.cl")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}") #Imprime: 2000
segunda_compra = 300
miyagi.hacer_compra(segunda_compra)
print(f"Segunda compra de {segunda_compra}") #Imprime: 2300
#imprimir el cuanto le queda de credito a miyagi
print(f"Credito restante de {miyagi.nombre}: ${miyagi.limite_credito - miyagi.saldo_pagar}") #Imprime: 27700


