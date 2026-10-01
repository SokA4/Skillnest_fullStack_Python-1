from datetime import datetime
from config.mysqlconnection import connectToMySQL

class Libro:
    def __init__(self, data):
        self.id = data.get('id')
        self.titulo = data.get('titulo')
        self.autor = data.get('autor')
        self.genero = data.get('genero')
        self.fecha_publicacion = data.get('fecha_publicacion')
        self.descripcion = data.get('descripcion')
        self.usuario_id = data.get('usuario_id')
        self.created_at = data.get('created_at')
        
        # Atributos extendidos para vistas
        self.publicado_por = data.get('publicado_por')
        self.total_favoritos = data.get('total_favoritos', 0)

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO libros (titulo, autor, genero, fecha_publicacion, descripcion, usuario_id)
            VALUES (%(titulo)s, %(autor)s, %(genero)s, %(fecha_publicacion)s, %(descripcion)s, %(usuario_id)s);
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def get_by_user(cls, usuario_id):
        query = """
            SELECT l.*, COUNT(f.id) AS total_favoritos
            FROM libros l
            LEFT JOIN favoritos f ON l.id = f.libro_id
            WHERE l.usuario_id = %(usuario_id)s
            GROUP BY l.id
            ORDER BY l.created_at DESC;
        """
        results = connectToMySQL().query_db(query, {'usuario_id': usuario_id})
        libros = []
        if results:
            for row in results:
                libros.append(cls(row))
        return libros

    @classmethod
    def get_community_books(cls, usuario_id):
        query = """
            SELECT l.*, CONCAT(u.nombre, ' ', u.apellido) AS publicado_por, COUNT(f.id) AS total_favoritos
            FROM libros l
            JOIN usuarios u ON l.usuario_id = u.id
            LEFT JOIN favoritos f ON l.id = f.libro_id
            WHERE l.usuario_id != %(usuario_id)s
            GROUP BY l.id
            ORDER BY l.created_at DESC;
        """
        results = connectToMySQL().query_db(query, {'usuario_id': usuario_id})
        libros = []
        if results:
            for row in results:
                libros.append(cls(row))
        return libros

    @classmethod
    def get_by_id(cls, libro_id):
        query = """
            SELECT l.*, CONCAT(u.nombre, ' ', u.apellido) AS publicado_por, COUNT(f.id) AS total_favoritos
            FROM libros l
            JOIN usuarios u ON l.usuario_id = u.id
            LEFT JOIN favoritos f ON l.id = f.libro_id
            WHERE l.id = %(id)s
            GROUP BY l.id;
        """
        results = connectToMySQL().query_db(query, {'id': libro_id})
        if not results:
            return None
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """
            UPDATE libros 
            SET titulo = %(titulo)s, autor = %(autor)s, genero = %(genero)s, 
                fecha_publicacion = %(fecha_publicacion)s, descripcion = %(descripcion)s
            WHERE id = %(id)s AND usuario_id = %(usuario_id)s;
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete(cls, libro_id, usuario_id):
        query = "DELETE FROM libros WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL().query_db(query, {'id': libro_id, 'usuario_id': usuario_id})

    @staticmethod
    def validar_libro(data):
        errores = []
        if len(data.get('titulo', '').strip()) < 2:
            errores.append("El título es obligatorio y debe tener al menos 2 caracteres.")
        if not data.get('autor', '').strip():
            errores.append("El nombre del autor es obligatorio.")
        if not data.get('genero', '').strip():
            errores.append("Debes seleccionar un género.")
        
        fecha_str = data.get('fecha_publicacion', '')
        if not fecha_str:
            errores.append("La fecha de publicación es obligatoria.")
        else:
            try:
                fecha_valida = datetime.strptime(fecha_str, '%Y-%m-%d').date()
                if fecha_valida > datetime.now().date():
                    errores.append("La fecha de publicación no puede ser una fecha futura.")
            except ValueError:
                errores.append("El formato de fecha no es válido.")

        if len(data.get('descripcion', '').strip()) < 10:
            errores.append("La descripción es obligatoria y debe tener al menos 10 caracteres.")
            
        return errores