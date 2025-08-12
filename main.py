from livro import Livro
from leitor import Usuario
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    biblioteca.cadastrar_livro(Livro("Inteligência Artificial Aplicada", "Pedro Silva", 2021, 4))
    biblioteca.cadastrar_livro(Livro("Estruturas de Dados Avançadas", "Carla Souza", 2022, 3))
    biblioteca.cadastrar_livro(Livro("Aprendizado de Máquina para Iniciantes", "João Almeida", 2020, 5))
    biblioteca.cadastrar_livro(Livro("Banco de Dados com PostgreSQL", "Mariana Santos", 2023, 2))

    biblioteca.cadastrar_usuario(Usuario("Cleiton", "cleiton@email.com", 1))
    biblioteca.cadastrar_usuario(Usuario("Amanda", "amanda@email.com", 2))

    biblioteca.emprestar_livro(1, "Inteligência Artificial Aplicada")
    biblioteca.emprestar_livro(2, "Estruturas de Dados Avançadas")
    biblioteca.devolver_livro(1, "Inteligência Artificial Aplicada")

    biblioteca.listar_livros()
    biblioteca.listar_usuarios()

    biblioteca.buscar_livro("Dados")
    biblioteca.resumo()
    biblioteca.mostrar_historico()

if __name__ == "__main__":
    main()
