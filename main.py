from bike import vistoria
from user import entrarNaConta, fazerCadastro
from types_db import ICliente
from sim_database import clientes
from basic_functions import forcar_opcao


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
            user = entrarNaConta(clientes)
        elif escolhaLogin == 2:
            user = fazerCadastro(clientes)
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
            bike = vistoria(user)
            if bike is not None:
                user["bikes"].append(bike)
        elif escolhaMenu == 2:
            # Dados do usuário
            print(f"{user['nome']} - {user['email']}")
            print(f"Telefone: {user['telefone']}")
            print(f"CPF: {user['cpf']}")
            print(f"CEP: {user['cep']}\n")
        elif escolhaMenu == 3:
            print("Bikes:")
            for bike in user["bikes"]:
                print(f"Modelo: {bike['modelo']}")
                print(f"Valor: {bike['valor']}")
                print(f"Modificações: {bike['modificacoes']}")
                print(f"Chassi: {bike['chassi']}\n")
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
