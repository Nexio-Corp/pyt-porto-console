from bike import vistoria, printar_lista_bikes
from user import entrar_na_conta, fazer_cadastro, exibir_informacoes_usuario
from basic_functions import forcar_opcao
from report import visualizar_relatorio_vistoria


def main():
    user = None
    while user is None:
        escolhaLogin = int(
            forcar_opcao(
                "Bem-vindo(a)! \nO que deseja fazer? \n1- Entrar \n2- Cadastrar-se \n3- Sair \n",
                ["1", "2", "3"],
            )
        )
        if escolhaLogin == 1:
            user = entrar_na_conta()
        elif escolhaLogin == 2:
            user = fazer_cadastro()
        else:
            print("Obrigado. Volte logo.")
            return
    while True:
        isAdm = "@porto" in user[2]
        escolhaMenu = int(
            forcar_opcao(
                "Este é nosso menu de funcionalidades:"
                "\n1 - Fazer vistoria"
                "\n2 - Visualizar Dados de Usuário"
                "\n3 - Visualizar Bikes"
                + ("\n4 - Visualizar relatório de vistoria" if isAdm else "")
                +
                "\n9 - Sair"
                "\nQual delas deseja utilizar? ",
                ["1", "2", "3", "4", "9"],
            )
        )

        if escolhaMenu == 1:
            vistoria(user)
            

        elif escolhaMenu == 2:
            exibir_informacoes_usuario(user)

        elif escolhaMenu == 3:
            print("\nEssas são suas bikes cadastradas:\n")
            printar_lista_bikes(user)
            print("\n")

        elif escolhaMenu == 4 and isAdm:
            visualizar_relatorio_vistoria()
        else:
            print("Sessão encerrada")
            return


main()
