from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola gente"

@app.route("/")
def nosotros():
    return "¡Conocenos!"

@app.route("/")
def contactos():
    return "¡Contactanos!"

@app.route("/")
def productos():
    return "¡Conoce nuestros productos!"

if __name__ == "__main__":
    app.run(debug=True)