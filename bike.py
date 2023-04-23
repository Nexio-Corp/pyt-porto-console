def vistoria(user: dict[str, str]):
    print("Para darmos início na vistoria, precisaremos de alguns dados da sua bike:")
    modeloBike = input("Digite o modelo da sua bike: ")
    valorBike = float(input("Digite o valor da sua bike: "))
    modificacoesBike = input(
        "Digite as modificações feitas na bike - separas por virgula: ")
    numeroDoChassi = int(input("Digite o número do chassi: "))

    print("\nDados enviados! Para o seguinte passo, é necessário estar com a sua bike do seu lado.")
    print("Agora precisaremos de 6 fotos da sua bike:")

    fotos = ""
    while fotos != "111111":
        while len(fotos) < 6:
            escolhaFoto = input(
                "Para simular o envio de fotos escolha as opções abaixo:"
                "\n1 - Foto autêntica"
                "\n2 - Foto da internet(Falsa)"
                "\n3 - Foto de uma bike de outro modelo"
                "\n4 - Foto de uma bike com dano"
                "\n5 - Desistir do envio de fotos"
                f"({6 - len(fotos)}) fotos restantes.\n"
            )
            if escolhaFoto == "5":
                print("Vistoria cancelada.")
                return
            fotos += escolhaFoto
        if fotos == "111111":  # 111111 é o valor que representa que todas as fotos são autênticas
            print(
                "Vistoria executada com sucesso! A apólice foi enviada para o seu email.")
            bike = {
                'modelo': modeloBike,
                'valor': valorBike,
                'modificacoes': [mod.strip() for mod in modificacoesBike.split(",")],
                'chassi': numeroDoChassi,
                'fotos': fotos
            }
            return bike
        elif "2" in fotos:  # 2 é o valor que representa que uma das fotos é falsa
            print(
                "Identificamos fotos falsas, por favor envie fotos reais.")
        elif "3" in fotos:  # 3 é o valor que representa que uma das fotos é de uma bike de outro modelo
            print(
                "Identificamos fotos com uma bike de outro modelo,"
                " por favor envie fotos com a sua bike cadastrada.")
        elif "4" in fotos:  # 4 é o valor que representa que uma das fotos é de uma bike com dano
            print(
                "Identificamos fotos com uma bike danificada, infelizmente o seguro desse bike.")
        else:
            print("Opções inválidas.")
