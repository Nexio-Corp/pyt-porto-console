from types_db import IUsuario
from sim_database import usuarios
from basic_functions import forcar_opcao, gerar_lista_baseada_em_len
from bike import cadastrar_bike, printar_lista_bikes
from queries import obter_bikes_do_usuario, obter_usuario_por_nome, obter_bike_e_colunas_por_indice


def escolher_usuario_relatorio():
    usuario_encontrado = False
    usuario = None
    while usuario_encontrado is False:
        escolha_usuario = input(
            "Digite o nome do usuário para o qual deseja visualizar o relatório de vistoria: ")
                
        usuario = obter_usuario_por_nome(escolha_usuario)
        
        if usuario != None:
            usuario_encontrado = True
    
    return usuario


def escolher_bike_relatorio(user):
    bike_selecionada = None
    escolha = ""
    while bike_selecionada is None:
        bikes_usuario = obter_bikes_do_usuario(user[0])
        if len(bikes_usuario) == 0:
            print(f"\n{user[1]} ainda não possui bikes cadastradas.")
            break
        else:
            print(f"\nEssas são as bikes cadastradas para {user[1]}:")
            printar_lista_bikes(user)
            lista = []
            for bike in obter_bikes_do_usuario(user[0]):
                lista.append(str(bike[0]))
            lista.append("cancelar")
            escolha = forcar_opcao(
                '\nDigite o índice da bike para a qual deseja visualizar o relatório de vistoria. Para voltar ao menu, digite "cancelar". \n', lista)
            if escolha == "cancelar":
                bike_selecionada = ""
            else:
                bike_selecionada = escolha
    return escolha


def visualizar_relatorio_vistoria():
    try:
        usuario = escolher_usuario_relatorio()

        if usuario is not None:
            try:
                escolha = escolher_bike_relatorio(usuario)
                escolha = int(escolha)
                bike, colunas = obter_bike_e_colunas_por_indice(escolha)

                if bike is not None:
                    if bike[6] == "111111":
                        print(bike[7])
                    else:
                        print(
                            f"{usuario[1]} ainda não realizou a vistoria para esta bike.\n")
                else:
                    print("Bike não encontrada para o usuário.\n")
                
            except TypeError:
                print("Erro: Problema ao acessar informações da bike.")
        else:
            print("Erro: Usuário não encontrado.")

    except Exception as e:
        print(f"Erro: {e}")
