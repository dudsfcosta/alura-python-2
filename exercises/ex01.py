# Uma pessoa está trabalhando em um projeto de streaming de música, e o paradigma que será utilizado é o de

# Programação Orientada a Objetos (POO), no qual o código é estruturado em unidades autônomas chamadas objetos. Cada
# objeto encapsula dados e comportamentos relacionados, promove modularidade e possibilita a reutilização de código.

# Sabendo disso, foi desenvolvido o seguinte código:
class Musica:
    nome = ''
    artista = ''
    duracao = int


musica = Musica()
musica.nome = 'Bohemian Rhapsody'
musica.duracao = 355

print(f'Música: {musica.nome} - Banda: {musica.artista} - {musica.duracao} segundos')

# Com base no código acima, analise as afirmações abaixo e marque aquela que contém a saída correta do console:

# Opção A
"""Música: Bohemian Rhapsody - Banda: Queen - 355 segundos"""
"""Não foi informado o nome da banda"""

# Opção B
"""Música: Bohemian Rhapsody - Banda:  - 355 segundos"""

# Opção C
"""<__main__.Musica object at 0x10073c310>"""
"""É feito o acesso direto às informações, e não ao endereço do objeto"""

# Opção D
"""Um erro de atributo será gerado informando que o objeto musica não possui a propriedade artista."""
"""Por ser inicializada como uma string vazia, essa variável não vai apresentar erros"""
