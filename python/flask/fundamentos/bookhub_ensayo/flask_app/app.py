import os
import sys
from flask import Flask
from dotenv import load_dotenv

# Asegura que Python encuentre la carpeta 'controllers', 'models' y 'config'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'clave_secreta_default')

from controllers.auth import auth_bp
from controllers.libros import libros_bp
from controllers.favoritos import favoritos_bp

app.register_blueprint(auth_bp)
app.register_blueprint(libros_bp)
app.register_blueprint(favoritos_bp)

if __name__ == '__main__':
    app.run(debug=True)