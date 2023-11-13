from basic_functions import forcar_opcao
from queries import cadastrar_bike_no_bd, obter_bikes_do_usuario, listar_informacoes_completas_bike, obter_bike_e_colunas_por_indice, inserir_fotos_vistoria_bd, inserir_relatorio_vistoria_bd


def cadastrar_bike(user):
    cadastrar_bike_no_bd(user[0])


def selecionar_bike(user):
    bike_selecionada = None
    escolha = ""
    while bike_selecionada is None:
        bikes_usuario = obter_bikes_do_usuario(user[0])
        if len(bikes_usuario) == 0:
            print("\nVocê ainda não possui bikes cadastradas.")
            cadastrar_bike(user)
        else:
            print("\nEssas são suas bikes cadastradas:")
            printar_lista_bikes(user)
            lista = []
            for bike in obter_bikes_do_usuario(user[0]):
                lista.append(str(bike[0]))
            lista.append("nova")
            lista.append("cancelar")
            escolha = forcar_opcao(
                '\nDigite o índice da bike para a qual deseja fazer vistoria ou "nova" para fazer a vistoria de uma nova bike. Para voltar ao menu, digite "cancelar". \n', lista)

            if escolha == "nova":
                cadastrar_bike(user)
            elif escolha == "cancelar":
                bike_selecionada = ""
            else:
                bike_selecionada = escolha
    return escolha


def printar_lista_bikes(user):
    for bike in obter_bikes_do_usuario(user[0]):
        # Aqui você pode ajustar de acordo com a estrutura real do seu banco de dados
        indice = bike[0]
        modelo = bike[2]
        valor = bike[3]
        modificacoes = bike[4]
        chassi = bike[5]

        string = f"{indice}) {modelo} - R$ {valor} - {modificacoes} - {chassi}"
        print(string)


def montar_relatorio(bike, colunas):
    relatorio = ""
    relatorio += "\nRelatório de Vistoria da Bike:\n---Informações completas da bicicleta---\n"
    relatorio += listar_informacoes_completas_bike(bike, colunas)
    relatorio += "---Comentários acerca da vistoria---\nA vistoria da bicicleta foi realizada com sucesso! Todas as informações fornecidas foram cuidadosamente verificadas, e as fotos enviadas confirmam a autenticidade e o excelente estado da bicicleta. Este relatório serve como confirmação da conclusão bem-sucedida da vistoria. O veículo pode ser segurado pela Porto sem problemas.\n"

    return relatorio


def vistoria(user):
    escolha = None
    colunas = None
    bike_escolhida = None
    while escolha == None:
        escolha = selecionar_bike(user)
        if escolha == "cancelar":
            return
        else:
            escolha = int(escolha)
            bike_escolhida, colunas = obter_bike_e_colunas_por_indice(escolha)

            if bike_escolhida[6] == "111111":
                print("\nA vistoria para essa bike já foi realizada com sucesso. Por favor, escolha uma bike que ainda não tenha sido vistoriada.")
                escolha = None

    print("Informações da Bike selecionada:")
    informacoes = listar_informacoes_completas_bike(bike_escolhida, colunas)
    print(informacoes)
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
            f"\n({6 - len(fotos)
                  }) fotos restantes.\n", ["1", "2", "3", "4", "5"]
        )
        if escolhaFoto == "5":
            print("Vistoria cancelada.")
            return
        fotos += escolhaFoto

    if fotos == "111111":  # 111111 é o valor que representa que todas as fotos são autênticas
        if bike_escolhida is not None:
            inserir_fotos_vistoria_bd(bike_escolhida, fotos)
            inserir_relatorio_vistoria_bd(
                bike_escolhida, montar_relatorio(bike_escolhida, colunas))
        print("Vistoria executada com sucesso! A apólice foi enviada para o seu email.")
    elif "2" in fotos:  # 2 é o valor que representa que uma das fotos é falsa
        print("Identificamos fotos falsas, por favor tente novamente enviando apenas fotos reais.")
    elif "3" in fotos:  # 3 é o valor que representa que uma das fotos é de uma bike de outro modelo
        print("Identificamos fotos de uma bike de outro modelo, por favor tente novamente enviando fotos de sua bike que corresponde com o modelo informado.")
    elif "4" in fotos:  # 4 é o valor que representa que uma das fotos é de uma bike com dano
        print("Pelas fotos identificamos que sua bike está danificada. Infelizmente o Seguro Bike da Porto não cobre bikes com esses tipos de danos.")
    else:
        print("Opção inválida.")
