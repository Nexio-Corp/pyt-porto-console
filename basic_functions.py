def forcar_opcao(msg, lista_opcoes):
    resposta = input(msg)
    while not resposta in lista_opcoes:
        resposta = input("Digite um valor válido por favor. ")
    return resposta