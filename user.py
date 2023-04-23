def fazerCadastro(clientes: list[dict[str, str]]):
    print("Para fazer o cadastro digite:")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    telefone = input("Telefone para contato: ")
    cpf = input("CPF: ")
    cep = input("Cep: ")
    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'telefone': telefone,
        'cpf': cpf,
        'cep': cep
    }
    print("Seu cadastro foi concluído com sucesso!\nVocê será redirecionado para a página inicial.\n.\n.\n.\n.")
    clientes.append(usuario)
    return usuario


def entrarNaConta(clientes: list[dict[str, str]]):
    user = None
    while user is None:
        user = input("Digite o seu e-mail: ")
        password = input("Digite a sua senha: ")
        print(user, password)
        for cliente in clientes:
            if cliente['email'] == user and cliente['senha'] == password:
                user = cliente
                break
        if user is not None:
            print(f"Olá {user['nome']}, você entrou na sua conta")
        else:
            print("E-mail ou senha incorretos. Tente novamente")
    return user
