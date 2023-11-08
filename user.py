from types_db import ICliente


def fazerCadastro(clientes: list[ICliente]):
    print("Para fazer o cadastro digite:")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    telefone = input("Telefone para contato: ")
    cpf = input("CPF: ")
    cep = input("Cep: ")
    usuario: ICliente = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'telefone': telefone,
        'cpf': cpf,
        'cep': cep,
        'bikes': []
    }
    print("Seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.\n.")
    clientes.append(usuario)
    return usuario


def entrarNaConta(clientes: list[ICliente]):
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
