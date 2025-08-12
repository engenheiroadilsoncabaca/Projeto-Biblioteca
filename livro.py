class Livro:
    def __init__(self, titulo, autor, ano, quantidade):
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.ano = ano
        self.quantidade = quantidade

    def __str__(self):
        return f" {self.titulo} ({self.ano}) - {self.autor} | Disponível: {self.quantidade}"
