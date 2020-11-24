from entidades.RegioesAdmin import RegioesAdmin
from entidades.SituacaoAtual import SituacaoAtual


# NÃO IMPLEMENTADO
def AdicionarParentesPacientes():
    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome,populacao);
            break;
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False


# NÃO IMPLEMENTADO
def AdcionarProfissionaisPacientes():
    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome, populacao)
            break
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")
    return False


# NÃO IMPLEMENTADO
def AdcionarProfissionaisHospitais():

    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome, populacao)
            break
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False
# NÃO IMPLEMENTADO
def AdcionarPacientesMedicacoes():

    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome, populacao)
            break
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False


# NÃO IMPLEMENTADO
def AdcionarPacientesSintomas():

    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome, populacao)
            break
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False


# NÃO IMPLEMENTADO
def AdcionarPacientesTestes():

    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome, populacao)
            break
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False
