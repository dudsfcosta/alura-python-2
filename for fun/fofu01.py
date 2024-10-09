# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção
# de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para
# melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?
from modelos import restaurante


# Exercícios
# 1- Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante.restaurante_praca.categoria = 'Italiana'


# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
print(restaurante.restaurante_praca._nome)


# 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando
# se o restaurante está ativo ou inativo.
msg = 'o restaurante está ativo' if restaurante.restaurante_praca.ativo else 'o restaurante está desativado'
print(msg)


# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável
# chamada categoria.
categoria = restaurante.Restaurante.categoria


# Altere o valor do atributo nome para 'Bistrô'.
restaurante.restaurante_praca._nome = 'Bistrô'


# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast
# Food'.
restaurante_pizza = restaurante.Restaurante
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'


# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(restaurante_pizza.categoria)


# Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True
msg = 'o restaurante está ativo' if restaurante.restaurante_praca.ativo else 'o restaurante está desativado'
print(msg)

# Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome do restaurante: {restaurante.restaurante_praca._nome}')
print(f'Categoria do restaurante: {restaurante.restaurante_praca.categoria}')
