
class Usuario:
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"Usuario: {self.username}"

class Post:
    def __init__(self, id, userId, title, body):
        self.id = id
        self.userId = userId
        self.title = title
        self.body = body

    def __str__(self):
        return f"Post [{self.id}]: {self.title}"

    # Método útil para convertir el objeto a diccionario si lo necesito enviar a la API
    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "title": self.title,
            "body": self.body
        }