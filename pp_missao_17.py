'''
MISSÃO 17
1. Crie três dicionários que contenham cidades diferentes com algumas características, como
cidade = {'nome': 'curitiba', 'ano_fundacao': '1932', 'estado': 'PR'}
e os guarde em uma lista chamada cidades. Itere sua lista de cidades com um laço de repetição.
Mostre na tela todas as características da cidade.
'''

cidades = []

cidade = {
    'nome': 'curitiba',
    'ano_fundacao': 1700,
    'estado': 'PR'
}
cidades.append(cidade)

cidade = {
    'nome': 'são paulo',
    'ano_fundacao': 1650,
    'estado': 'SP'
}
cidades.append(cidade)
cidade = {
    'nome': 'fortaleza',
    'ano_fundacao': 1850,
    'estado': 'CE'
}
cidades.append(cidade)
# print(cidades)

for cidade in cidades:
    # print(cidade)
    nome_cidade = cidade['nome'].title()
    ano = cidade['ano_fundacao']
    estado = cidade['estado']
    print(f"Dados da cidade: {nome_cidade}, Ano fundação: {ano}, Estado: {estado}.")

'''
2. Crie vários dicionários, na qual cada possua uma chave nome, que receberá o nome de uma fruta. Nestes
dicionários inclua além do nome, a cor da fruta e o mês da estação. Guarde esses dicionários numa lista chamada
frutas. Itere essa lista com FOR e mostre na tela tudo que criou sobre as frutas.
'''
frutas = []

fruta = {
    'nome': 'banana',
    'cor': 'amarela',
    'estacao': 'ano todo'
}
frutas.append(fruta)
fruta = {
    'nome': 'pera',
    'cor': 'verde',
    'estacao': 'abril a setembro'
}
frutas.append(fruta)
fruta = {
    'nome': 'maça',
    'cor': 'vermelha',
    'estacao': 'Dezembro'
}
frutas.append(fruta)
# print(frutas)

for fruta in frutas:
    # print(fruta)
    print(f"\nInformações sobre {fruta['nome'].title()}:")
    for chave, valor in fruta.items():
        print(f"\t {chave.title()}: {valor}")

'''
3. Crie um dicionário chamado comidas_favoritas. Pense em nomes de amigos para ser as chaves do dicionário e
então guarde um ou duas comidas favoritas para cada amigo. Itere esse dicionário e apresente o nome de cada
pessoa e sua(s) comidas favoritas.
'''

comidas_favoritas = {
    'jefferson': ['churrasco', 'pizza'],
    'pedro': ['pão', 'massas'],
    'marcos': ['churrasco', 'risoto']
}

for nome, comidas in comidas_favoritas.items():
    print(f"\n{nome.title()} gosta das seguintes comidas:")
    for comida in comidas:
        print(f" - {comida.title()}")


