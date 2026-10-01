from flask import Blueprint, render_template, redirect, url_for, session, flash
from models.favorito import Favorito
from models.libro import Libro

favoritos_bp = Blueprint('favoritos', __name__)

def login_required(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            flash("Por favor inicia sesión para continuar.", "error_login")
            return redirect(url_for('auth.login_page'))
        return func(*args, **kwargs)
    return wrapper

@favoritos_bp.route('/favoritos')
@login_required
def ver_favoritos():
    usuario_id = session['usuario_id']
    mis_favoritos = Favorito.get_user_favorites(usuario_id)
    return render_template('favoritos.html', favoritos=mis_favoritos)

@favoritos_bp.route('/favoritos/agregar/<int:libro_id>', methods=['POST'])
@login_required
def agregar_favorito(libro_id):
    libro = Libro.get_by_id(libro_id)
    if not libro:
        flash("El libro no existe.", "error")
        return redirect(url_for('libros.mis_libros'))

    Favorito.add_favorite(session['usuario_id'], libro_id)
    flash("Añadido a tus favoritos.", "exito")
    return redirect(url_for('libros.detalle_libro', id=libro_id))

@favoritos_bp.route('/favoritos/quitar/<int:libro_id>', methods=['POST'])
@login_required
def quitar_favorito(libro_id):
    Favorito.remove_favorite(session['usuario_id'], libro_id)
    flash("Eliminado de tus favoritos.", "exito")
    return redirect(url_for('libros.detalle_libro', id=libro_id))