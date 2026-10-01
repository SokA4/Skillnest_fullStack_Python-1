import re
from config.mysqlconnection import connectToMySQL
from werkzeug.security import generate_password_hash, check_password_hash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password_hash = data.get('password_hash')
        self.created_at = data.get('created_at')

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password_hash)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password_hash)s);
        """
        data['password_hash'] = generate_password_hash(data['password'])
        return connectToMySQL().query_db(query, data)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL().query_db(query, {'email': email})
        if not results:
            return None
        return cls(results[0])

    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL().query_db(query, {'id': user_id})
        if not results:
            return None
        return cls(results[0])

    @staticmethod
    def validar_registro(data):
        errores = []
        if len(data.get('nombre', '').strip()) < 2:
            errores.append("El nombre debe tener al menos 2 caracteres.")
        if len(data.get('apellido', '').strip()) < 2:
            errores.append("El apellido debe tener al menos 2 caracteres.")
        if not EMAIL_REGEX.match(data.get('email', '')):
            errores.append("El formato del correo electrónico no es válido.")
        elif Usuario.get_by_email(data.get('email', '')):
            errores.append("El correo electrónico ya se encuentra registrado.")
        if len(data.get('password', '')) < 6:
            errores.append("La contraseña debe tener al menos 6 caracteres.")
        if data.get('password') != data.get('confirm_password'):
            errores.append("Las contraseñas no coinciden.")
        return errores

    @staticmethod
    def validar_login(data):
        errores = []
        usuario = Usuario.get_by_email(data.get('email', ''))
        if not usuario or not check_password_hash(usuario.password_hash, data.get('password', '')):
            errores.append("Credenciales inválidas. Verifica tu e-mail y contraseña.")
            return errores, None
        return errores, usuario