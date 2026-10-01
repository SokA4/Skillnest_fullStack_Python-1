from config.mysqlconnection import connectToMySQL

class Favorito:
    @classmethod
    def add_favorite(cls, usuario_id, libro_id):
        query = """
            INSERT IGNORE INTO favoritos (usuario_id, libro_id)
            VALUES (%(usuario_id)s, %(libro_id)s);
        """
        return connectToMySQL().query_db(query, {'usuario_id': usuario_id, 'libro_id': libro_id})

    @classmethod
    def remove_favorite(cls, usuario_id, libro_id):
        query = """
            DELETE FROM favoritos 
            WHERE usuario_id = %(usuario_id)s AND libro_id = %(libro_id)s;
        """
        return connectToMySQL().query_db(query, {'usuario_id': usuario_id, 'libro_id': libro_id})

    @classmethod
    def is_favorite(cls, usuario_id, libro_id):
        query = """
            SELECT * FROM favoritos 
            WHERE usuario_id = %(usuario_id)s AND libro_id = %(libro_id)s;
        """
        results = connectToMySQL().query_db(query, {'usuario_id': usuario_id, 'libro_id': libro_id})
        return len(results) > 0

    @classmethod
    def get_users_who_favorited(cls, libro_id):
        query = """
            SELECT u.nombre, u.apellido 
            FROM usuarios u
            JOIN favoritos f ON u.id = f.usuario_id
            WHERE f.libro_id = %(libro_id)s
            ORDER BY u.nombre ASC;
        """
        return connectToMySQL().query_db(query, {'libro_id': libro_id})

    @classmethod
    def get_user_favorites(cls, usuario_id):
        query = """
            SELECT l.*, CONCAT(u.nombre, ' ', u.apellido) AS publicado_por
            FROM libros l
            JOIN favoritos f ON l.id = f.libro_id
            JOIN usuarios u ON l.usuario_id = u.id
            WHERE f.usuario_id = %(usuario_id)s
            ORDER BY f.created_at DESC;
        """
        return connectToMySQL().query_db(query, {'usuario_id': usuario_id})