from user import fazerCadastro, entrarNaConta
from bike import vistoria
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
            input("""Bem-Vindo(a) á Porto Seguro. Escolha uma opção a baixo:
                    \n1 - Entrar na sua conta
                    \n2 - Fazer cadastro
                    \n3 - Sair\n"""))
        if escolhaLogin == 1:
            user = entrarNaConta(clientes)
        elif escolhaLogin == 2:
            user = fazerCadastro(clientes)
        elif escolhaLogin == 3:
            print("Obrigado. Volte logo.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    while True:
        escolhaMenu = int(input(
            "Bem-vindo(a) ao menu de funcionalidades:\n1 - Fazer vistoria\n2 - Sair\n"))
        if escolhaMenu == 1:
            vistoria()
        elif escolhaMenu == 2:
            print("Sessão encerrada")
            exit()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
