from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login_page():
    if 'usuario_id' in session:
        return redirect(url_for('libros.mis_libros'))
    return render_template('login.html')

@auth_bp.route('/registro')
def registro_page():
    if 'usuario_id' in session:
        return redirect(url_for('libros.mis_libros'))
    return render_template('registro.html')

@auth_bp.route('/procesar_registro', methods=['POST'])
def procesar_registro():
    data = request.form.to_dict()
    errores = Usuario.validar_registro(data)
    
    if errores:
        for err in errores:
            flash(err, 'error_registro')
        return redirect(url_for('auth.registro_page'))

    user_id = Usuario.save(data)
    if user_id:
        session['usuario_id'] = user_id
        session['usuario_nombre'] = data['nombre']
        session['usuario_apellido'] = data['apellido']
        flash("¡Registro exitoso! Bienvenido a BookHub.", "exito")
        return redirect(url_for('libros.mis_libros'))
    
    flash("Ocurrió un problema al procesar tu registro.", "error_registro")
    return redirect(url_for('auth.registro_page'))

@auth_bp.route('/procesar_login', methods=['POST'])
def procesar_login():
    data = request.form.to_dict()
    errores, usuario = Usuario.validar_login(data)
    
    if errores:
        for err in errores:
            flash(err, 'error_login')
        return redirect(url_for('auth.login_page'))

    session['usuario_id'] = usuario.id
    session['usuario_nombre'] = usuario.nombre
    session['usuario_apellido'] = usuario.apellido
    return redirect(url_for('libros.mis_libros'))

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "exito")
    return redirect(url_for('auth.login_page'))