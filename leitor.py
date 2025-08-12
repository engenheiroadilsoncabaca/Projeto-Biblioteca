class Usuario:
    def __init__(self, nome_usuario, email, id_usuario):
        self.nome_usuario = nome_usuario.strip()
        self.email = email.strip().lower()
        self.id_usuario = id_usuario
        self.livros_emprestados = []

    def __str__(self):
        return f" {self.nome_usuario} - {self.email} | Livros emprestados: {len(self.livros_emprestados)}"
