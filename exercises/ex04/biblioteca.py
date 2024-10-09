from livro import Livro

class Biblioteca:
    livroA = Livro('O Retrato de Dorian Gray', 'Oscar Wilde', 1981)
    livroB = Livro('Maus', 'Art Spiegelman', 2016)
    livroC = Livro('Arsène Lupin, o Ladrão de Casaca', 'Maurice Leblanc', 2021)
    livroD = Livro('The Witcher: O Último Desejo',   'Andrzej Sapkowski', 2020)

    Livro.listar_livros()
    Livro.emprestar(livroC)

    Livro.verificar_disponibilidade(Livro, 2021)
    Livro.verificar_disponibilidade(Livro, 2020)
