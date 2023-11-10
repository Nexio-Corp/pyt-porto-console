from typing import TypedDict
from types_db import IBike, ICliente
from basic_functions import forcar_opcao, printar_dic_em_lista, gerar_lista_baseada_em_len_dic, printar_objeto_do_dic

def cadastrar_bike(user: ICliente):
    print("Para darmos início na vistoria, precisaremos de alguns dados da sua bike:")
    bike : IBike = {
            'modelo': input("Digite o modelo da sua bike: "),
            'valor': float(input("Digite o valor da sua bike: ")),
            'modificacoes': [mod.strip() for mod in input("Digite as modificações feitas na bike - separe-as por virgula: ").split(",")],
            'chassi': input("Digite o número do chassi: "),
            'fotos': ""
        }
    user["bikes"].append(bike)
    print(user["bikes"])

def selecionar_bike(user: ICliente):
    bike_selecionada = None
    escolha = ""
    while bike_selecionada is None:
        if (len(user["bikes"]) == 0):
            print("\nVocê ainda não possui bikes cadastradas.")
            cadastrar_bike(user)
        else:
            print("\nEssas são suas bikes cadastradas:")
            printar_dic_em_lista(user["bikes"])
            lista = gerar_lista_baseada_em_len_dic(user["bikes"])
            lista.append("nova")
            escolha = forcar_opcao('\nDigite o número da bike para a qual deseja fazer vistoria ou "nova" para fazer a vistoria de uma nova bike. \n', lista)
            if escolha == "nova":
                cadastrar_bike(user)
            else:
                bike_selecionada = escolha
    return escolha

def vistoria(user: ICliente):
    escolha = None
    bike_escolhida = None
    while escolha == None:
        escolha = int(selecionar_bike(user))
        bike_escolhida = user["bikes"][escolha - 1]
                    
        if bike_escolhida["fotos"] == "111111":
            print("\nA vistoria para essa bike já foi realizada com sucesso. Por favor, escolha uma bike que ainda não tenha sido vistoriada.")
            escolha = None

    print("Informações da Bike selecionada:")
    printar_objeto_do_dic(bike_escolhida)
    print("\nPara o próximo passo, é necessário estar com a bike ao seu lado.")
    print("\nAgora precisaremos de 6 fotos da sua bike:")

    fotos = ""
    while len(fotos) < 6:
        escolhaFoto = forcar_opcao(
            "Para simular o envio de fotos escolha as opções abaixo:"
            "\n1 - Foto autêntica"
            "\n2 - Foto da internet(Falsa)"
            "\n3 - Foto de uma bike de outro modelo"
            "\n4 - Foto de uma bike com dano"
            "\n5 - Desistir do envio de fotos"
            f"\n({6 - len(fotos)}) fotos restantes.\n", ["1","2","3","4","5"]
        )
        if escolhaFoto == "5":
            print("Vistoria cancelada.")
            return
        fotos += escolhaFoto
    
    if fotos == "111111":  # 111111 é o valor que representa que todas as fotos são autênticas
        if bike_escolhida is not None:
            bike_escolhida["fotos"] = fotos
        print("Vistoria executada com sucesso! A apólice foi enviada para o seu email.")
        printar_objeto_do_dic(bike_escolhida)
    elif "2" in fotos:  # 2 é o valor que representa que uma das fotos é falsa
        print("Identificamos fotos falsas, por favor tente novamente enviando apenas fotos reais.")
    elif "3" in fotos:  # 3 é o valor que representa que uma das fotos é de uma bike de outro modelo
        print("Identificamos fotos de uma bike de outro modelo, por favor tente novamente enviando fotos de sua bike que corresponde com o modelo informado.")
    elif "4" in fotos:  # 4 é o valor que representa que uma das fotos é de uma bike com dano
        print("Pelas fotos identificamos que sua bike está danificada. Infelizmente o Seguro Bike da Porto não cobre bikes com esses tipos de danos.")
    else:
        print("Opção inválida.")
