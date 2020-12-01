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

#Função que deleta o item de uma tabela
def Deletar(tabela, lista):
    # Escolhe parâmetro que será utilizado para deletar um item da tabela
    print("Por qual parâmetro você quer deletar: ")
    for l in range(len(lista)):
        print(l + 1, " - ", lista[l])
    coluna = int(input(""))
    # Digita o novo valor que será inserido no banco de dados
    print("Qual o valor do ", lista[coluna - 1], " que você deseja deletar: ")
    valor = str(input(""))
    OpDb.Deleta(tabela, lista[coluna-1], valor)

#---------------------------------------------------------------------------------------

#Função que deleta o item de uma tabela
def DeletarMedicacoesPacientes():
    while(True):
        try:
            # Escolhe parâmetro que será utilizado para deletar um item da tabela
            valor1 = str(input("Cpf do paciente: "))
            valor2 = str(input("Codigo da Medicação: "))

            OpDb.DeletaRelacao("MedicacoesPacientes", "CpfPaciente", valor1, "CodMedicacao", valor2)
            break
        except:
            print("Não foi possível deletar")

    return False
#---------------------------------------------------------------------------------------

#Função que deleta o item de uma tabela
def DeletarPacientePaciente():
    while(True):
        try:
            # Escolhe parâmetro que será utilizado para deletar um item da tabela
            valor1 = str(input("Cpf do paciente: "))
            valor2 = str(input("Cpf do parente: "))

            OpDb.DeletaRelacao("ParentePaciente", "CpfPaciente", valor1, "CpfParente", valor2)
            break
        except:
            print("Não foi possível deletar")

    return False
#---------------------------------------------------------------------------------------
#Função que deleta o item de uma tabela
def DeletarProfPaciente():
    while(True):
        try:
            # Escolhe parâmetro que será utilizado para deletar um item da tabela
            valor1 = str(input("Cpf do paciente: "))
            valor2 = str(input("Cpf do Profissional da saúde: "))

            OpDb.DeletaRelacao("ProfAtendePaciente", "CpfPaciente", valor1, "CpfProfissional", valor2)
            break
        except:
            print("Não foi possível deletar")

    return False

#---------------------------------------------------------------------------------------
#Função que deleta o item de uma tabela
def DeletarProfHospital():
    while(True):
        try:
            # Escolhe parâmetro que será utilizado para deletar um item da tabela
            valor1 = str(input("Cpf do profissional da saúde: "))
            valor2 = str(input("Codigo do Hospital: "))

            OpDb.DeletaRelacao("ProfTrabalhaHospital", "CpfProfissional", valor1, "CodHospital", valor2)
            break
        except:
            print("Não foi possível deletar")

    return False

#---------------------------------------------------------------------------------------
#Função que deleta o item de uma tabela
def DeletarSintomasPacientes():
    while(True):
        try:
            # Escolhe parâmetro que será utilizado para deletar um item da tabela
            valor1 = str(input("Cpf do paciente: "))
            valor2 = str(input("Codigo do Sintoma: "))

            OpDb.DeletaRelacao("SintomasPacientes", "CpfPaciente", valor1, "CodSintoma", valor2)
            break
        except:
            print("Não foi possível deletar")

    return False

#---------------------------------------------------------------------------------------
#Função que deleta o item de uma tabela
def DeletarTestesPacientes():
    while(True):
        try:
            # Escolhe parâmetro que será utilizado para deletar um item da tabela
            valor1 = str(input("Cpf do paciente: "))
            valor2 = str(input("Codigo do Teste: "))

            OpDb.DeletaRelacao("TestesPacientes", "CpfPaciente", valor1, "CodTeste", valor2)
            break
        except:
            print("Não foi possível deletar")

    return False

#---------------------------------------------------------------------------------------
#Função que deleta o item de uma tabela
def DeletarSituacaoAtual():
    while(True):
        try:
            # Escolhe parâmetro que será utilizado para deletar um item da tabela
            valor1 = str(input("Data: "))
            print(valor1)
            valor2 = str(input("Codigo da regiao administrativa: "))

            OpDb.DeletaRelacao("SituacaoAtual", "DataSituacao", valor1, "CodRegiao", valor2)
            break
        except:
            print("Não foi possível deletar")

    return False

#---------------------------------------------------------------------------------------
