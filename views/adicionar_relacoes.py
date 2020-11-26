from entidades.RegioesAdmin import RegioesAdmin
from entidades.SituacaoAtual import SituacaoAtual
from entidades.Acoes import Acoes
from entidades.Hospitais import Hospitais as Hospital
from entidades.Pacientes import Paciente
from entidades.Testes import Testes
from entidades.TestesPacientes import TestesPacientes
from entidades.Sintomas import Sintomas
from entidades.SintomasPacientes import SintomasPacientes
from entidades.Medicacoes import Medicacoes
from entidades.MedicacoesPacientes import MedicacoesPacientes
from entidades.ProfissionaisSaude import ProfissionaisSaude
from entidades.ProfTrabalhaHospital import ProfTrabalhaHospital
from entidades.ProfAtendePaciente import ProfAtendePaciente
from entidades.Parentes import Parente
from entidades.ParentePaciente import ParentePaciente


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
