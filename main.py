from bike import vistoria
from user import entrar_na_conta, fazer_cadastro, exibir_informacoes_usuario
from types_db import ICliente
from sim_database import clientes
from basic_functions import forcar_opcao, printar_dic_em_lista


def main():
    user = clientes[1]
    print(user["nome"])
    while user is None:
        escolhaLogin = int(
            forcar_opcao(
                "Bem-vindo(a)! \nO que deseja fazer? \n1- Entrar \n2- Cadastrar-se \n3- Sair \n",
                ["1", "2", "3"],
            )
        )
        if escolhaLogin == 1:
            user = entrar_na_conta(clientes)
        elif escolhaLogin == 2:
            user = fazer_cadastro(clientes)
        else:
            print("Obrigado. Volte logo.")
            return
    while True:
        isAdm = "@porto" in user["email"]
        escolhaMenu = int(
            forcar_opcao(
                "Este é nosso menu de funcionalidades:"
                "\n1 - Fazer vistoria"
                "\n2 - Visualizar Dados de Usuário"
                "\n3 - Visualizar Bikes"
                + ("\n4 - Visualizar relatório de vistoria" if isAdm else "")
                +
                # TODO Adicionar relatório de vistoria
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
            printar_dic_em_lista(user["bikes"])
            print("\n")
       
        elif escolhaMenu == 4 and isAdm:
            for cliente in clientes:
                print(f"Nome: {cliente['nome']}")
                print(f"E-mail: {cliente['email']}")
                print(f"Telefone: {cliente['telefone']}")
                print(f"CPF: {cliente['cpf']}")
                print(f"CEP: {cliente['cep']}")
                print("Bikes:")
                for bike in cliente["bikes"]:
                    print(f"\tModelo: {bike['modelo']}")
                    print(f"\tValor: {bike['valor']}")
                    print(f"\tModificações: {bike['modificacoes']}")
                    print(f"\tChassi: {bike['chassi']}")
                    print(
                        f"\tVistoria: {'Aprovada' if bike['fotos'] == '111111' else 'Reprovada'}\n"
                    )
        
        else:
            print("Sessão encerrada")
            return


# if __name__ == "__main__":

main()
