from datos.conexion import ConexionDB
from auxiliares.seguridad import Seguridad  
from servicios.api_service import ApiService

class GestorNegocio:
    def __init__(self):
        self.db = ConexionDB()
        self.db.conectar()

    def registrar_usuario(self, username, password):
        hashed = Seguridad.encriptar_pass(password)
        conn = self.db.conectar()
        try:
            conn.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed))
            conn.commit()
            print(">> Usuario registrado con éxito.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    def login(self, username, password):
        conn = self.db.conectar()
        cursor = conn.execute("SELECT password FROM usuarios WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()
        if row and Seguridad.validar_pass(password, row[0]):
            return True
        return False

    def sincronizar_api(self):
        print(">> Descargando datos de API...")
        posts = self.api.get_posts()
        if posts:
            conn = self.db.conectar()
            # Limpiar tabla para evitar duplicados en pruebas
            conn.execute("DELETE FROM posts") 
            for p in posts[:10]: # Guardamos solo 10 para probar
                conn.execute("INSERT INTO posts (id, userId, title, body) VALUES (?,?,?,?)",
                             (p['id'], p['userId'], p['title'], p['body']))
            conn.commit()
            conn.close()
            print(">> Datos guardados en DB Local correctamente.")

    def mostrar_locales(self):
        conn = self.db.conectar()
        cursor = conn.execute("SELECT id, title FROM posts")
        print("\n--- LISTA DE POSTS (DB LOCAL) ---")
        for row in cursor:
            print(f"ID: {row[0]} | Título: {row[1]}")
        conn.close()