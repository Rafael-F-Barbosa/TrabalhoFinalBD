from entidades.RegioesAdmin import RegioesAdmin
from entidades.SituacaoAtual import SituacaoAtual

def AdcionarRegiaoAdmin():

    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome,populacao);
            break;
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False

# Se pá isso aqui não faz sentido. 

def AdcionarSituacaoAtual():
    while(True):
        try:
            data         = str(input("Nome da regiao: "))
            casos_leves  = int(input("Populacao: "))
            casos_graves =  
            SituacaoAtual.AdicionaSituacaoAtual(nome, populacao)
            break
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False
