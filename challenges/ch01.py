class Musica:
    nome = ''
    artista = ''
    duracao = int


musica1 = Musica()
musica2 = Musica()
musica3 = Musica()

musica1.nome = 'Bad Feeling (Oompa Loompa)'
musica1.artista = 'Jagwar Twin'
musica1.duracao = 2 * 60 + 13

musica2.nome = 'Under The Influence'
musica2.artista = 'Shayne Orok'
musica2.duracao = 2 * 60 + 26

musica3.nome = 'TOMBI'
musica3.artista = 'Kvi Baba'
musica3.duracao = 3 * 60 + 26

print('#===========================#')
print(musica1.nome)
print(musica1.artista)
print(musica1.duracao, 'segundos')
print('#===========================#')
print(musica2.nome)
print(musica2.artista)
print(musica2.duracao, 'segundos')
print('#===========================#')
print(musica3.nome)
print(musica3.artista)
print(musica3.duracao, 'segundos')
print('#===========================#')
