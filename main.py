from bike import vistoria
from user import entrarNaConta, fazerCadastro

clientes = [
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
            # TODO Adicionar relatório de vistoria
            "\n9 - Sair\n"))
        if escolhaMenu == 1:
            user['bikes'].append(vistoria(user))
        elif escolhaMenu == 2:
            # TODO Melhorar a visualização dos dados
            print(user)
        elif escolhaMenu == 3:
            print("Sessão encerrada")
            return
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
