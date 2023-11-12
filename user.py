from types_db import IUsuario


def fazer_cadastro(clientes: list[IUsuario]):
    print("Para fazer o cadastro digite:")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    telefone = input("Telefone para contato: ")
    cpf = input("CPF: ")
    cep = input("Cep: ")
    usuario: IUsuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'telefone': telefone,
        'cpf': cpf,
        'cep': cep,
        'bikes': []
    }
    print(f"{usuario['nome']}, seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.")
    clientes.append(usuario)


def entrar_na_conta(clientes: list[IUsuario]):
    user = None
    while user is None:
        email = input("Digite o seu e-mail: ")
        password = input("Digite a sua senha: ")
        for cliente in clientes:
            if cliente['email'] == email and cliente['senha'] == password:
                user = cliente
                break
        if user is not None:
            print(f"Olá {user['nome']}, você entrou na sua conta.")
        else:
            print("E-mail ou senha incorretos. Tente novamente.")
    return user


def exibir_informacoes_usuario(user: IUsuario):
    # Dados do usuário
    print(f"\n{user['nome']}")
    print(f"Email: {user['email']}")
    print(f"Telefone: {user['telefone']}")
    print(f"CPF: {user['cpf']}")
    print(f"CEP: {user['cep']}\n")