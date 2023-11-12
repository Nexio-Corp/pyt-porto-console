from types_db import IUsuario
from sim_database import usuarios
from basic_functions import forcar_opcao, gerar_lista_baseada_em_len_dic
from bike import printar_lista_bikes


def escolher_usuario_relatorio():
    escolha_usuario = None
    while escolha_usuario is None:
        escolha_usuario = input("Digite o nome do usuário para o qual deseja visualizar o relatório de vistoria: ")
        usuario_encontrado = False
        for usuario in usuarios:
            if escolha_usuario in usuario["nome"]:
                print(f"Usuário encontrado.")
                usuario_encontrado = True
                return usuario
        if usuario_encontrado is False:
            print("Usuário não encontrado, por favor tente novamente.")
            escolha_usuario = None
    

def escolher_bike_relatorio(user: IUsuario):
    bike_selecionada = None
    escolha = ""
    while bike_selecionada is None:
        if (len(user["bikes"]) == 0):
            print(f"\n{user['nome']} ainda não possui bikes cadastradas.")
        else:
            print(f"\nEssas são as bikes cadastradas para {user['nome']}:")
            printar_lista_bikes(user)
            lista = gerar_lista_baseada_em_len_dic(user["bikes"])
            lista.append("cancelar")
            escolha = forcar_opcao('\nDigite o número da bike para a qual deseja visualizar o relatório de vistoria. Para voltar ao menu, digite "cancelar". \n', lista)
            if escolha == "cancelar":
                bike_selecionada = ""
            else:
                bike_selecionada = user["bikes"][int(escolha) - 1]
    return bike_selecionada
   

def visualizar_relatorio_vistoria():
    try:
        usuario = escolher_usuario_relatorio()

        if usuario is not None:
            try:
                bike = escolher_bike_relatorio(usuario)

                if isinstance(bike, dict):
                    if bike["fotos"] == "111111":
                        print(bike["relatorio"])                        
                    else:
                        print(f"{usuario['nome']} ainda não realizou a vistoria para esta bike.")
                else:
                    print("Bike não encontrada para o usuário.")
            
            except TypeError:
                print("Erro: Problema ao acessar informações da bike.")
        else:
            print("Erro: Usuário não encontrado.")

    except Exception as e:
        print(f"Erro: {e}")