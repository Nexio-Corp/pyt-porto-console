import oracledb

# QUERIES PARA OPERAÇÕES RELATIVAS AOS USUÁRIOS


def obter_ultimo_usuario():  # Essa função é usada apenas para obter as informações acerca do usuário que acaba de se cadastrar e possibilitar interação do programa com ele pelo nome
    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    # Recuperar o último ID cadastrado (id é auto incrementado no Banco de Dados)
    cur.execute("SELECT MAX(id) FROM usuario")
    ultimo_id = cur.fetchone()[0]

    # Recuperar os dados do último usuário cadastrado
    cur.execute("SELECT * FROM usuario WHERE id = :ultimo_id",
                ultimo_id=ultimo_id)
    ultimo_usuario = cur.fetchone()

    cur.close()
    con.close()

    return ultimo_usuario


def cadastrar_usuario_no_bd(nome, email, senha, telefone, cpf, cep):
    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    # Usando parâmetros vinculados
    cur.execute("INSERT INTO usuario (nome, email, senha, telefone, cpf, cep) VALUES (:nome, :email, :senha, :telefone, :cpf, :cep)",
                nome=nome, email=email, senha=senha, telefone=telefone, cpf=cpf, cep=cep)

    con.commit()  # Commit para efetivar a inserção

    cur.close()
    con.close()


def verificar_credenciais_no_bd(email, senha):
    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    user = None
    try:
        # Consulta SQL para verificar se há um usuário com o email e senha fornecidos
        cur.execute(
            "SELECT * FROM usuario WHERE email = :email AND senha = :senha", email=email, senha=senha)
        user = cur.fetchone()

        if user:
            print(f"Olá {user[1]}, você entrou na sua conta.\n")
        else:
            print(
                "\nFalha ao entrar na conta. Verifique suas credenciais e tente novamente.")

    finally:
        cur.close()
        con.close()
        return user


# Essa função é utilizada para obter informações do usuário que está logado na sessão.
def obter_usuario_no_bd(user):

    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    cur.execute("SELECT * FROM usuario WHERE id = :id",
                id=user[0])
    usuario = cur.fetchone()

    cur.close()
    con.close()

    return usuario


# Essa função é utilizada apenas no momento em que um Admin deseja encontrar um usuário pelo nome para acessar seus relatórios de vistoria.
def obter_usuario_por_nome(nome):

    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    usuario = None
    try:
        cur.execute("SELECT * FROM usuario WHERE nome = :nome",
                    nome=nome)
        usuario = cur.fetchone()

        if usuario:
            print(f"Usuário encontrado.\n")
        else:
            print(
                "\nUsuário não encontrado, por favor tente novamente.")

    finally:
        cur.close()
        con.close()
        return usuario


# QUERIES PARA OPERAÇÕES RELATIVAS ÀS BIKES

def cadastrar_bike_no_bd(user_id):
    print("Para darmos início na vistoria, precisaremos de alguns dados da sua bike:")

    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    while True:
        try:
            modelo = input("Digite o modelo da sua bike: ")
            valor = float(input("Digite o valor da sua bike: "))
            modificacoes = input(
                "Digite as modificações feitas na bike - separe-as por vírgula: ")
            chassi = input("Digite o número do chassi: ")

            # Insere a bike no banco de dados
            cur.execute("""
                INSERT INTO bike (usuario_id, modelo, valor, modificacoes, chassi, fotos, relatorio)
                VALUES (:usuario_id, :modelo, :valor, :modificacoes, :chassi, '', NULL)
            """, modelo=modelo, valor=valor, modificacoes=modificacoes, chassi=chassi, usuario_id=user_id)

            con.commit()  # Commit para efetivar a inserção

            print("Bike cadastrada com sucesso!")
            break  # Sai do loop se todas as entradas forem válidas
        except ValueError:
            print("Erro: Certifique-se de digitar um valor válido para o preço.")
        except oracledb.DatabaseError as e:
            print(f"Erro no banco de dados: {e}")

    cur.close()
    con.close()


def obter_bikes_do_usuario(user_id):
    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()
    bikes_do_usuario = []

    try:
        cur.execute(
            "SELECT * FROM bike WHERE usuario_id = :user_id ORDER BY id", user_id=user_id)
        bikes_do_usuario = cur.fetchall()

    except oracledb.DatabaseError as e:
        print(f"Erro no banco de dados: {e}")

    finally:
        cur.close()
        con.close()

    # Retorna uma lista contendo todas as bikes do usuário referido pelo Id.
    return bikes_do_usuario


# Essa função acessa e retorna uma bike especificamente e também suas colunas, permitindo que essas colunas sejam percorridas para, por exemplo, imprimir as informações da bike.
def obter_bike_e_colunas_por_indice(bike_id):
    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    # Consulta para obter uma bike específica pelo ID
    cur.execute("SELECT * FROM bike WHERE id = :bike_id", bike_id=bike_id)
    bike = cur.fetchone()

    # Obtém os nomes das colunas
    colunas = [coluna[0] for coluna in cur.description]

    cur.close()
    con.close()

    return bike, colunas


def listar_informacoes_completas_bike(bike, colunas):
    infos = ""
    if bike:
        for coluna, valor in zip(colunas, bike):
            if coluna != "RELATORIO":
                if coluna == "MODIFICACOES":
                    if valor == None:
                        infos += f"{coluna}: sem modificações\n"
                else:
                    infos += f"{coluna}: {valor}\n"
    else:
        infos = "Bike não encontrada."

    return infos


def inserir_fotos_vistoria_bd(bike, fotos):
    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    cur.execute("UPDATE bike SET fotos = :fotos WHERE id = :bike_id",
                fotos=fotos, bike_id=bike[0])
    con.commit()

    cur.close()
    con.close()


def inserir_relatorio_vistoria_bd(bike, relatorio):
    con = oracledb.connect(user="rm97784", password="081100",
                           dsn="oracle.fiap.com.br:1521/orcl")
    cur = con.cursor()

    cur.execute("UPDATE bike SET relatorio = :relatorio WHERE id = :bike_id",
                relatorio=relatorio, bike_id=bike[0])
    con.commit()

    cur.close()
    con.close()
