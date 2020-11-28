from entidades.RegioesAdmin import RegioesAdmin
from entidades.SituacaoAtual import SituacaoAtual
from entidades.Hospitais import Hospitais
from entidades.ProfissionaisSaude import ProfissionaisSaude
from entidades.Pacientes import Paciente
from entidades.Testes import Testes
from entidades.Sintomas import Sintomas
from entidades.Medicacoes import Medicacoes
from entidades.Acoes import Acoes
from entidades.Parentes import Parente


def Atualizar(lista):
            
            print("Por qual parâmetro você quer atualizar: ")
            for l in range(len(lista)):
                print(l + 1, " - ", lista[l])

            coluna2 = int(input(""))
            print("Qual o valor do ", lista[coluna2 - 1], " que você deseja atualizar: ")
            valor2 = str(input(""))
            print("Qual parâmetro você quer atualizar: ")

            for l in range(len(lista)):
                print(l + 1, " - ", lista[l])

            coluna1 = int(input(""))
            print("Qual novo valor de  ", lista[coluna1 - 1], ": ")
            valor1 = str(input(""))

            return coluna1,valor1, coluna2, valor2

def AtualizarAcao():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(Acoes.dicio)
            Acoes.AtualizaAcoes(Acoes.dicio[coluna1-1], valor1, Acoes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a ação.\nTente novamente.")

    return False

def AtualizarHospital():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(Hospitais.dicio)
            Hospitais.AtualizaHospital(Hospitais.dicio[coluna1-1], valor1, Hospitais.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar o Hospital.\nTente novamente.")

    return False


def AtualizarMedicacao():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(Medicacoes.dicio)
            Medicacoes.AtualizaMedicacao(Medicacoes.dicio[coluna1-1], valor1, Medicacoes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a medicação.\nTente novamente.")

    return False

def AtualizarPaciente():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(Paciente.dicio)
            Paciente.AtualizaPaciente(Paciente.dicio[coluna1-1], valor1, Paciente.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar o paciente.\nTente novamente.")

    return False


def AtualizarProfissional():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(ProfissionaisSaude.dicio)
            ProfissionaisSaude.AtualizaProfissional(ProfissionaisSaude.dicio[coluna1-1], valor1, ProfissionaisSaude.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar o profissional da saúde.\nTente novamente.")

    return False


def AtualizarParente():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(Parente.dicio)
            Parente.AtualizaParente(Parente.dicio[coluna1-1], valor1, Parente.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar o parente.\nTente novamente.")

    return False


def AtualizarRegiao():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(RegioesAdmin.dicio)
            RegioesAdmin.AtualizaRegiao(RegioesAdmin.dicio[coluna1-1], valor1, RegioesAdmin.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar o paciente.\nTente novamente.")

    return False


def AtualizarSintomas():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(Sintomas.dicio)
            Sintomas.AtualizaSintomas(Sintomas.dicio[coluna1-1], valor1, Sintomas.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar o sintoma.\nTente novamente.")

    return False

def AtualizarSituacao():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(SituacaoAtual.dicio)
            SituacaoAtual.AtualizaSituacao(SituacaoAtual.dicio[coluna1-1], valor1, SituacaoAtual.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a situação.\nTente novamente.")

    return False

def AtualizarTestes():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(Testes.dicio)
            Testes.AtualizaTestes(Testes.dicio[coluna1-1], valor1, Testes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar o teste.\nTente novamente.")

    return False