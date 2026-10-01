from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.libro import Libro
from models.favorito import Favorito

libros_bp = Blueprint('libros', __name__, url_prefix='/libros')

def login_required(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            flash("Por favor inicia sesión para acceder a este apartado.", "error_login")
            return redirect(url_for('auth.login_page'))
        return func(*args, **kwargs)
    return wrapper

@libros_bp.route('')
@login_required
def mis_libros():
    usuario_id = session['usuario_id']
    mis_libros_lista = Libro.get_by_user(usuario_id)
    libros_comunidad = Libro.get_community_books(usuario_id)
    return render_template('mis_libros.html', mis_libros=mis_libros_lista, libros_comunidad=libros_comunidad)

@libros_bp.route('/nuevo')
@login_required
def nuevo_libro():
    return render_template('nuevo_libro.html')

@libros_bp.route('/crear', methods=['POST'])
@login_required
def crear_libro():
    data = request.form.to_dict()
    errores = Libro.validar_libro(data)
    
    if errores:
        for err in errores:
            flash(err, 'error_libro')
        return redirect(url_for('libros.nuevo_libro'))

    data['usuario_id'] = session['usuario_id']
    Libro.save(data)
    flash("¡El libro ha sido publicado exitosamente!", "exito")
    return redirect(url_for('libros.mis_libros'))

@libros_bp.route('/<int:id>')
@login_required
def detalle_libro(id):
    libro = Libro.get_by_id(id)
    if not libro:
        flash("El libro solicitado no existe.", "error")
        return redirect(url_for('libros.mis_libros'))

    es_favorito = Favorito.is_favorite(session['usuario_id'], id)
    usuarios_favoritos = Favorito.get_users_who_favorited(id)
    
    return render_template(
        'detalle_libro.html', 
        libro=libro, 
        es_favorito=es_favorito, 
        usuarios_favoritos=usuarios_favoritos
    )

@libros_bp.route('/<int:id>/editar')
@login_required
def editar_libro(id):
    libro = Libro.get_by_id(id)
    if not libro:
        flash("El libro no existe.", "error")
        return redirect(url_for('libros.mis_libros'))
    
    # Verificación de propiedad estricta
    if libro.usuario_id != session['usuario_id']:
        flash("Acceso denegado: No tienes permisos para editar este libro.", "error")
        return redirect(url_for('libros.mis_libros'))

    return render_template('editar_libro.html', libro=libro)

@libros_bp.route('/<int:id>/actualizar', methods=['POST'])
@login_required
def actualizar_libro(id):
    libro = Libro.get_by_id(id)
    if not libro or libro.usuario_id != session['usuario_id']:
        flash("No puedes modificar libros que no te pertenecen.", "error")
        return redirect(url_for('libros.mis_libros'))

    data = request.form.to_dict()
    errores = Libro.validar_libro(data)
    
    if errores:
        for err in errores:
            flash(err, 'error_libro')
        return redirect(url_for('libros.editar_libro', id=id))

    data['id'] = id
    data['usuario_id'] = session['usuario_id']
    Libro.update(data)
    flash("¡El libro se ha actualizado con éxito!", "exito")
    return redirect(url_for('libros.mis_libros'))

@libros_bp.route('/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_libro(id):
    libro = Libro.get_by_id(id)
    if not libro or libro.usuario_id != session['usuario_id']:
        flash("Operación no autorizada. No puedes eliminar este libro.", "error")
        return redirect(url_for('libros.mis_libros'))

    Libro.delete(id, session['usuario_id'])
    flash("El libro ha sido eliminado correctamente.", "exito")
    return redirect(url_for('libros.mis_libros'))