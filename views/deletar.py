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

import util.OpDb as OpDb

#---------------------------------------------------------------------------------------

#Função que deleta o ítem de uma tabela
def Deletar(tabela, lista):
            
    print("Por qual parâmetro você quer deletar: ")

    for l in range(len(lista)):
        print(l + 1, " - ", lista[l])

    coluna = int(input(""))

    print("Qual o valor do ", lista[coluna - 1], " que você deseja deletar: ")

    valor = str(input(""))

    OpDb.Deleta(tabela, lista[coluna-1], valor)

#---------------------------------------------------------------------------------------

