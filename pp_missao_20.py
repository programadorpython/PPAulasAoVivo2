'''
MISSÃ0 20
1.	Crie uma lista com o nome pedidos_carros e adicione vários carros diferentes a ela.
Crie então uma segunda lista vazia com o nome concluidos_carros. Itere cada item da lista pedidos_carros
 e mostre na tela para cada carro, uma mensagem "Carro: pedido Fusion enviado a concessionária" e
 transfira esse carro para a nova lista que estava vazia. No final mostre na tela a lista concluidos_carros
 com todos os itens dentro dela.
'''

pedidos_carros = ['ford', 'toyota', 'honda', 'kia']
carros_concluidos = []

while pedidos_carros:
    carro_removido = pedidos_carros.pop()
    print(f"Carro: {carro_removido.title()} enviado a fábrica.")
    carros_concluidos.append(carro_removido)

print()

for carro in carros_concluidos:
    print(f"Carro {carro.title()} concluído.")

print(f"Lista de pedidos de carros - {len(pedidos_carros)}")

'''
2. Usando a lista pedidos_carros, faça com que o carro Fusion apareça umas quantro vezes na lista.
Escreva um código logo no início para exibir que a fábrica está sem o carro Fusion e faça um WHILE
para remover todos os carros Fusion na lista pedidos_carros. Certifique-se que nenhum Fusion esteja
na lista concluidos_carros.
'''
print()

pedidos_carros = ['fusion', 'corolla', 'civic', 'fusion', 'fusion', 'fiesta', 'fusion']
carros_concluidos = []

print(f"Infelizmente a fábrica está sem Fusion")
modelo = 'fiesta'
while modelo in pedidos_carros:
    pedidos_carros.remove(modelo)

print(pedidos_carros)

while pedidos_carros:
    carro_removido = pedidos_carros.pop()
    print(f"Carro: {carro_removido.title()} enviado a fábrica.")
    carros_concluidos.append(carro_removido)

print()

for carro in carros_concluidos:
    print(f"Carro {carro.title()} concluído.")

print(f"Lista de pedidos de carros - {len(pedidos_carros)}")
print(f"Lista de pedidos de concluídos - {len(carros_concluidos)}")



























