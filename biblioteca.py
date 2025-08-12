from livro import Livro
from leitor import Usuario

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.historico = []

    def cadastrar_livro(self, livro):
        if any(l.titulo.lower() == livro.titulo.lower() for l in self.livros):
            print(f" O livro '{livro.titulo}' já está cadastrado!")
            return
        self.livros.append(livro)
        print(f" Livro '{livro.titulo}' cadastrado com sucesso!")

    def cadastrar_usuario(self, usuario):
        if any(u.email == usuario.email for u in self.usuarios):
            print(f" Usuário com e-mail '{usuario.email}' já existe!")
            return
        self.usuarios.append(usuario)
        print(f" Usuário '{usuario.nome_usuario}' cadastrado com sucesso!")

    def emprestar_livro(self, id_usuario, titulo_livro):
        usuario = self._buscar_usuario(id_usuario)
        livro = self._buscar_livro(titulo_livro)

        if not usuario or not livro:
            return
        if livro.quantidade <= 0:
            print(f" Livro '{livro.titulo}' está indisponível.")
            return

        usuario.livros_emprestados.append(livro.titulo)
        livro.quantidade -= 1
        self.historico.append(f"{usuario.nome_usuario} pegou '{livro.titulo}' emprestado.")
        print(f" '{livro.titulo}' emprestado para {usuario.nome_usuario}.")

    def devolver_livro(self, id_usuario, titulo_livro):
        usuario = self._buscar_usuario(id_usuario)
        livro = self._buscar_livro(titulo_livro)

        if not usuario or not livro:
            return
        if titulo_livro not in usuario.livros_emprestados:
            print(f" Este livro não está com {usuario.nome_usuario}.")
            return

        usuario.livros_emprestados.remove(titulo_livro)
        livro.quantidade += 1
        self.historico.append(f"{usuario.nome_usuario} devolveu '{livro.titulo}'.")
        print(f" '{livro.titulo}' devolvido por {usuario.nome_usuario}.")

    def listar_livros(self):
        print("\n Lista de Livros:")
        for livro in self.livros:
            print(livro)

    def listar_usuarios(self):
        print("\n🧑 Lista de Usuários:")
        for usuario in self.usuarios:
            print(usuario)

    def buscar_livro(self, termo):
        termo = termo.lower()
        resultados = [l for l in self.livros if termo in l.titulo.lower() or termo in l.autor.lower()]
        if resultados:
            print("\n Resultado da busca:")
            for l in resultados:
                print(l)
        else:
            print("Nenhum livro encontrado.")

    def resumo(self):
        total_livros = sum(l.quantidade for l in self.livros)
        emprestados = sum(len(u.livros_emprestados) for u in self.usuarios)
        print("\n Resumo da Biblioteca")
        print(f"Total de títulos: {len(self.livros)}")
        print(f"Total de livros em estoque: {total_livros}")
        print(f"Total de usuários: {len(self.usuarios)}")
        print(f"Empréstimos ativos: {emprestados}")

    def mostrar_historico(self):
        print("\n Histórico de operações:")
        for evento in self.historico:
            print(f"- {evento}")

    def _buscar_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print(" Usuário não encontrado.")
        return usuario

    def _buscar_livro(self, titulo):
        livro = next((l for l in self.livros if l.titulo.lower() == titulo.lower()), None)
        if not livro:
            print(" Livro não encontrado.")
        return livro
