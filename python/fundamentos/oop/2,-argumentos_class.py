class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

# Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 20000)
ale = Usuario("Alexander", "Pino", "alexander@gmail.com", 5000, 10000)

# Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel


# -----------------------------------
# --- Tarea rápida
'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias para la clase con distintos estudiantes
- Imprimir el nombre y apellido concatenado + especialidad
'''

class Estudiante:
    def __init__(self, nombre, apellido, rut, especialidad, fecha_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

# Creación de instancias
matias = Estudiante("Matías", "Rojas", "21.834.567-9", "Informática", "14/03/2006")
valentina = Estudiante("Valentina", "Muñoz", "24.112.890-4", "Administración", "29/11/2007")
sebastian = Estudiante("Sebastián", "Torres", "20.765.432-1", "Contabilidad", "08/07/2005")

# Imprimir
print(f"{matias.nombre} {matias.apellido} estudia: {matias.especialidad}")
print(f"{valentina.nombre} {valentina.apellido} estudia: {valentina.especialidad}")
print(f"{sebastian.nombre} {sebastian.apellido} estudia: {sebastian.especialidad}")
