# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
   {"nombre": "GameNinjaPro", "seguidores": 250000},
   {"nombre": "PixelWarrior", "seguidores": 180000}
]


# Eventos en distintas ciudades del mundo
eventos = {
   "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
   "España": ["Madrid", "Barcelona", "Valencia"]
}


# Coordenadas de la sede de un torneo internacional
ubicacion = [
   {"latitud": 34.052235, "longitud": -118.243683}
]

#En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda). Resultado esperado:

puntajes[1][0] = 600
print(puntajes)

# En streamers, cambia el nombre de ”GameNinjaPro” a ”EliteGamerX”.

streamers[0]["nombre"] = "EliteGamerX"
print(streamers)

# En eventos, cambia la ciudad “Las Vegas” por “San Francisco”.

eventos["Estados Unidos"][2] = "San Francisco"
print(eventos)

# En ubicacion, cambia el valo de ”latitud” a 40.712776 (cambiando la sede del torneo a Nueva York).

ubicacion[0]["latitud"] = 40.712776
print(ubicacion)


#recibe una lista de diccionarios e imprime cada diccionario en un formato legible, mostrando las claves y sus valores.
def iterar_diccionario(lista):
    for diccionario in lista:
         salida = ", ".join(f"{clave}: {valor}" for clave, valor in diccionario.items())
         print(salida)
iterar_diccionario(streamers)

#recibe una clave y una lista de diccionarios, e imprime el valor asociado a esa clave en cada diccionario de la lista.

def obtener_valores(clave, lista):
    for diccionario in lista:
        if clave in diccionario:
            print(diccionario[clave])
obtener_valores("nombre", streamers)
obtener_valores("seguidores", streamers)

#recibe un diccionario con listas como valores e imprime la cantidad de elementos en cada lista junto con los elementos mismos.
def mostrar_informacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
categorias = {
    "juegos_populares": ["Fortnite", "Minecraft", "Valorant", "GTA V"],
    "ciudades_eventos": ["Nueva York", "Madrid", "Tokio"]}
mostrar_informacion(categorias)
print(categorias)
         

