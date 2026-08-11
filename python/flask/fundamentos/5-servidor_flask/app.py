from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def inicio():
    return "<h1>Bienvenido a mi servidor Flask</h1>"

# Ruta genérica para explorar enrutamiento
@app.route("/explorar")
def explorar():
    return "<h2>Explorando rutas en Flask</h2>"

# Rutas dinámicas para personalización
@app.route("/usuario/<nombre>")
def usuario(nombre):    
    return f"<h2>Hola, {nombre}!</h2>"
# Ruta que repite un mensaje varias veces
@app.route("/repetir/<mensaje>/<int:veces>")
def repetir(mensaje, veces):
    return f"<h2>{mensaje * veces}</h2>"
# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1><p>Lo sentimos, la página que buscas no existe.</p>", 404

# Ejecuta el servidor
if __name__ == "__main__":
   app.run(debug=True)