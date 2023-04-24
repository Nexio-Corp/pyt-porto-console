from bike import vistoria, IBike
from user import entrarNaConta, fazerCadastro
from types_db import ICliente
# ICliente = dict[str, (str | list[dict[str, str]])]


clientes: list[ICliente] = [  # Mock de clientes
    {
        'nome': 'cliente1',
        'email': 'cliente1@gmail.com',
        'senha': '1234',
        'telefone': '123456789',
        'cpf': '123456789',
        'cep': '123456789',
        'bikes': []
    },
    {
        'nome': 'teste',
        'email': 'teste@email.com',
        'senha': '1234',
        'telefone': '123456789',
        'cpf': '123456789',
        'cep': '123456789',
        'bikes': []
    }
]


def main():
    user = None
    while user is None:
        escolhaLogin = int(
            input("Bem-Vindo(a) á Porto Seguro. Escolha uma opção a baixo:"
                  "\n1 - Entrar na sua conta"
                  "\n2 - Fazer cadastro"
                  "\n3 - Sair\n"
                  ))
        if escolhaLogin == 1:
            user = entrarNaConta(clientes)
        elif escolhaLogin == 2:
            user = fazerCadastro(clientes)
        elif escolhaLogin == 3:
            print("Obrigado. Volte logo.")
            return
        else:
            print("Opção inválida. Tente novamente.")
    while True:
        escolhaMenu = int(input(
            "Bem-vindo(a) ao menu de funcionalidades:\n1 - Fazer vistoria"
            "\n2 - Visualizar Dados"
            "\n3 - Visualizar Bikes"
            # TODO Adicionar relatório de vistoria
            "\n9 - Sair\n"))
        if escolhaMenu == 1:
            bike = vistoria(user)
            if bike is not None:
                user['bikes'].append(bike)
        elif escolhaMenu == 2:
            # Dados do usuário
            print(f"{user['nome']} - {user['email']}")
            print(f"Telefone: {user['telefone']}")
            print(f"CPF: {user['cpf']}")
            print(f"CEP: {user['cep']}\n")

        elif escolhaMenu == 3:
            print("Bikes:")
            for bike in user['bikes']:
                print(f"Modelo: {bike['modelo']}")
                print(f"Valor: {bike['valor']}")
                print(f"Modificações: {bike['modificacoes']}")
                print(f"Chassi: {bike['chassi']}\n")
        elif escolhaMenu == 9:
            print("Sessão encerrada")
            return
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
