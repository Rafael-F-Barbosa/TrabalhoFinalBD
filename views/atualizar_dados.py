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
                print(l + 1, lista[l])

            coluna2 = int(input(""))

            print("Qual o valor do ", lista[coluna2 - 1], " que você deseja atualizar: ")

            valor2 = str(input(""))

            print("Qual parâmetro você quer atualizar: ")

            for l in range(len(lista)):
                print(l + 1, lista[l])

            coluna1 = int(input(""))

            print("Qual novo valor de  ", lista[coluna1 - 1], ": ")

            valor1 = str(input(""))

            return coluna1,valor1, coluna2, valor2

#nao implementado
def AtualizarAcao():
    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(Acoes.dicio)
            Acoes.AtualizaAcoes(Acoes.dicio[coluna1-1], valor1, Acoes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a ação.\nTente novamente.")

    return False
