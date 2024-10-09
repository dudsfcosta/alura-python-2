class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    @classmethod
    def listar_livros(cls):
        print(f'{"Título".ljust(35)} | {"Autor".ljust(20)} | {"Ano".ljust(5)}| {"Disponível?"}')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(35)} | {livro._autor.ljust(20)} | {str(livro._ano_publicacao).ljust(5)}| {livro.disponivel}')

    @property
    def disponivel(self):
        return '⌧' if self._disponivel else '☐'

    def emprestar(self):
        if self._disponivel:
            self._disponivel = not self._disponivel
            print(f'O livro \"{self._titulo}\" foi emprestado e não está disponível até sua devolução.')
        else:
            print("Este livro não pode ser emprestado no momento.")

    @staticmethod
    def verificar_disponibilidade(cls, ano):
        flag = 0
        for livro in cls.livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                flag = 1
                print(f'{livro._titulo}')
        if not flag:
            print(f'Não foram encontrados livros de {ano}')

# print('||====================================  Livro A e Livro B  ====================================||')
# livroA = Livro('O Retrato de Dorian Gray', 'Oscar Wilde', 1902)
# livroB = Livro('Maus', 'Art Spiegelman', 1973)
# print('||==================================== Listar livros A e B ====================================||')
# Livro.listar_livros()
# print('||====================================  Livro C e Livro D  ====================================||')
# livroC = Livro('Arsène Lupin, o Ladrão de Casaca', 'Maurice Leblanc', 2021)
# livroD = Livro('The Witcher: O Último Desejo',   'Andrzej Sapkowski', 2020)
# print('||==================================== Listar livros C e D ====================================||')
# Livro.listar_livros()
# Livro.emprestar(livroC)
# print('||====================================  Emprestar livro C  ====================================||')
# Livro.emprestar(livroC)
# print('||====================================  Disponibilidade 1  ====================================||')
# Livro.verificar_disponibilidade(Livro,2021)
