def forcar_opcao(msg, lista_opcoes):
    resposta = input(msg)
    while not resposta in lista_opcoes:
        resposta = input("Digite um valor válido por favor. ")
    return resposta


def printar_dic_em_lista(dic):
    for i, element in enumerate(dic, start=1):
        string = f"{i}) "
        for value in element.values():
            string += f"{value} - "
        string = string[:-3]
        print(string)


def gerar_lista_baseada_em_len(obj):
    lista = []
    for i in range(len(obj)):
        lista.append(f"{i+1}")
    return lista


def printar_objeto_do_dic(objeto_no_dic):
    for key in objeto_no_dic:
        print(f"{key}: {objeto_no_dic[key]}")
