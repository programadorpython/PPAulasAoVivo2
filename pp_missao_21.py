'''Escreva uma funcao mostra_mensagem() que exiba uma frase a todos o que você esta aprendendo neste vídeo.
Chame a função e tenha certeza que a mensagem realmente foi exibida.
'''

def mostra_mensagem():
    """
    Função para exibir mensagem
    :return:
    """
    mensagem = 'Estou aprendendo funções.'
    print(mensagem)

mostra_mensagem()


'''2.Escreva uma função carro_favorito() que aceite um parâmetro modelo_carro.A função tem que exibir a mensagem
"Um dos meus carros favoritos é Fusion. " Chame a função e não se esqueça de informar o modelo do carro como
argumento  na chamada função.
'''



def carro_favorito(modelo_carro):
    """
    Função para exibir o modelo do carro
    :param modelo_carro: string
    :return:
    """
    print(f"Um dos meus carros favoritos é {modelo_carro.title()}.")



modelo = input("Qual seu modelo favorito: ")
carro_favorito(modelo)
