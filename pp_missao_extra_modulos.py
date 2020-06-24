def fazer_pizza(*ingredientes):
    """
    Função para fazer pizza de acordo com os ingredientes
    :param ingredientes: tuple
    :return:
    """
    print(f"\nComeçando a produção da pizza: ")
    for ingrediente in ingredientes:
        print(f"Adicionando {ingrediente} a sua pizza.")

    print("Sua pizza está pronta")

def criar_cantor(nome_cantor, tipo_musica, **mais_info):
    """
    Faz um dicionário para representar um perfil de cantor
    :param nome_cantor: string
    :param tipo_musica: string
    :param mais_info: **kwargs
    :return: dicionário
    """
    perfil_cantor = {
        'nome': nome_cantor,
        'estilo': tipo_musica
    }
    for chave, valor in mais_info.items():
        perfil_cantor[chave] = valor

    return perfil_cantor