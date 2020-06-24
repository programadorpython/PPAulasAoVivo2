'''2. Escreva um laço para informar ao usuário o preço da entrada num parque aquático. Se a pessoa tiver
menos de 2 anos a entrada é de graça, entre 2 e 12 anos paga meia entrada, 10 reais, e maior que 60 anos
pagará 8 reais.'''

texto = '\n Informe aqui sua idade. '
texto += "\n Digite 'sair' quando estiver finalizado: "

while True:
    idade = input(texto)
    if idade.lower() != 'sair':
        idade = int(idade)
        if idade <= 2:
            print("Voce nao pagará nada.")
        elif idade <= 12:
            print("Voce pagara meia entrada, 10 reais")
        elif idade >= 60:
            print("Voce pagará 8 reais.")
        else:
            print("Voce pagara o valor cheio, 20 reais")
    else:
        break



#
# texto = "Digite sair para encerrar a compra"
# texto += "\n - Entre com a idade do usuario --->  "
#
# mensagem = ''
# while mensagem.lower() != 'sair':
#     mensagem = input(texto)
#     if mensagem.lower() != 'sair':
#        if int(mensagem) <= 2:
#           print('Menor que dois anos não paga a entrada')
#        elif int(mensagem) <= 12:
#           print('Esse usuário paga meia entrada, valor da meia entrada = R$10,00')
#        elif int(mensagem) <= 59:
#
#
