import os
import sys

# Agrega la carpeta 'flask_app' a la ruta de búsqueda de Python
sys.path.append(os.path.join(os.path.dirname(__file__), 'flask_app'))

# Importa la instancia 'app' del archivo app.py ubicado en flask_app
from flask_app.app import app

if __name__ == '__main__':
    app.run(debug=True)

    from flask import render_template, request, redirect, session
from flask_app import app

# Ruta raíz de la aplicación (la primera página que se carga)
@app.route('/')
def index():
    # Si el usuario ya inició sesión, redirigir a su muro/dashboard
    if 'usuario_id' in session:
        return redirect('/libros')
        
    # Si no ha iniciado sesión, cargar la vista combinada
    return render_template('index.html')

# Si tenías una ruta /login por separado, puedes hacer que redirija a /
@app.route('/login')
def login_page():
    return redirect('/')