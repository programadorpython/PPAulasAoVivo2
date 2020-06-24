import pp_missao_extra_modulos
from pp_missao_extra_modulos import fazer_pizza, criar_cantor

'''Escreva uma função que aceita uma lista do que a pessoa quer de ingredientes numa pizza. A função deve ter um
parâmetro que agrupe tantos ingredientes quantos forem fornecidos ao ser chamada a função e deve apresentar um
resumo da pizza pedida. Chame a função três vezes usando um número diferentes de ingredientes a cada vez.'''

fazer_pizza('cebola', 'presunto')
fazer_pizza('presunto')
fazer_pizza('presunto', 'queijo', 'milho')


'''2.	Crie uma função que guarde informações sobre um cantor num dicionário. A função deve sempre receber o
nome do cantor e o tipo de música que canta. Um número arbitrário de argumentos nomeados então deverá ser aceito. 
Chame a função com as informações necessárias e dois outros pares nome-valor. Por exemplo, ano de nascimento e 
cidade de nascimento. Sua função deve ser apropriada para uma chamada como esta:
a. cantor = criar_cantor(‘Renato Russo’, ‘Rock’, ano_nasc=1970, cidade_nasc=’São Paulo’)
b. Mostre o dicionário devolvido para garantir que as informações foram armazenadas corretamente.'''

print()

nome = input('nome: ')
estilo = input('estilo: ')
idade = input('idade: ')

cantor_1 = criar_cantor(nome, estilo, idade=idade, cidade='curitiba', estado='pr')
print(cantor_1)

nome = input('nome: ')
estilo = input('estilo: ')
idade = input('idade: ')

cantor_2 = criar_cantor('Roberto Carlos', 'MPB')
print(cantor_2)

















