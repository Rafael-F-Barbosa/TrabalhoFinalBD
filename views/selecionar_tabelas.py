import os
from util.formata import imprime_lista_tabela_formatado as formata_tabela
from util.formata import formata_lista
from util.OpDb import ChamaProcedure
from util.OpDb import SelecionaTudo

from entidades.RegioesAdmin import RegioesAdmin
from entidades.SituacaoAtual import SituacaoAtual
from entidades.Acoes import Acoes
from entidades.Hospitais import Hospitais as Hospital
from entidades.Pacientes import Paciente
from entidades.Testes import Testes
from entidades.Sintomas import Sintomas
from entidades.Medicacoes import Medicacoes
from entidades.ProfissionaisSaude import ProfissionaisSaude
from entidades.Parentes import Parente
from entidades.TestesPacientes import TestesPacientes
from entidades.SintomasPacientes import SintomasPacientes
from entidades.MedicacoesPacientes import MedicacoesPacientes
from entidades.ProfTrabalhaHospital import ProfTrabalhaHospital
from entidades.ProfAtendePaciente import ProfAtendePaciente
from entidades.ParentePaciente import ParentePaciente


#---------------------------------------------------------------------------------------

# Função que escolhe qual tabela de dados será mostrada
def VerTabelasDados():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Ver tabelas regiao administrativa.")
    print("2 - Ver tabelas situacao atual.")
    print("3 - Ver tabelas ação.")
    print("4 - Ver tabelas hospital.")
    print("5 - Ver tabelas paciente.")
    print("6 - Ver tabelas teste.")
    print("7 - Ver tabelas sintoma.")
    print("8 - Ver tabelas medicação.")
    print("9 - Ver tabelas profissional saúde.")
    print("10 - Ver tabelas parente.")

    while(True):
        try:
            # Pega a resposta do usuario
            decisao = int(input(""))
            # De acordo com a resposta do usuário, chama a função que lista os ítens da 
            # classe escolhida, e depois chama a função formata_tabela que formata para 
            # mostrar para o usuário
            if(decisao in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                if(decisao == 1):
                    lista = RegioesAdmin.ListaTodasRegioesAdmin()
                    formata_tabela(lista, RegioesAdmin.dicio)
                elif(decisao == 2):
                    lista = SituacaoAtual.ListaTudoSituacaoAtual()
                    formata_tabela(lista, SituacaoAtual.dicio)
                elif(decisao == 3):
                    lista = Acoes.ListaTudoAcoes()
                    formata_tabela(lista, Acoes.dicio)
                elif(decisao == 4):
                    lista = Hospital.ListaTudoHospitais()
                    formata_tabela(lista, Hospital.dicio)
                elif(decisao == 5):
                    lista = Paciente.ListaTodosPacientes()
                    formata_tabela(lista, Paciente.dicio)
                elif(decisao == 6):
                    lista = Testes.ListaTestes()
                    formata_tabela(lista, Testes.dicio)
                elif(decisao == 7):
                    lista = Sintomas.ListaSintomas()
                    formata_tabela(lista, Sintomas.dicio)
                elif(decisao == 8):
                    lista = Medicacoes.ListaMedicacoes()
                    formata_tabela(lista, Medicacoes.dicio)
                elif(decisao == 9):
                    lista = ProfissionaisSaude.ListaProfissionaisSaude()
                    formata_tabela(lista, ProfissionaisSaude.dicio)
                elif(decisao == 10):
                    lista = Parente.ListaTodosParentes()
                    formata_tabela(lista, Parente.dicio)
                
                a = input('Enter para sair')
                break
            # Volta ao menu principal
            elif(decisao == 0):
                break
        except:
            # Caso o usuário coloque uma entrada inválida
            print("Entrada inválida")

    return False
#---------------------------------------------------------------------------------------

# Função que escolhe qual tabela de relações será mostrada
def VerTabelasRelacoes():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Ver parentes e pacientes.")
    print("2 - Ver profissionais da saúde e pacientes.")
    print("3 - Ver profissionais da saúde e hospitais.")
    print("4 - Ver pacientes e medicações.")
    print("5 - Ver pacientes com sintomas.")
    print("6 - Ver pacientes com testes.")

    while(True):
        try:
            # Pega a resposta do usuário
            decisao = int(input(""))
            # De acordo com a resposta do usuário, chama a função que lista os ítens da 
            # classe escolhida, e depois chama a função formata_tabela que formata para 
            # mostrar para o usuário
            if(decisao in [1, 2, 3, 4, 5, 6]):
                if(decisao == 1):
                    lista = ParentePaciente.ListaParentePaciente()
                    formata_tabela(lista, ParentePaciente.dicio)
                elif(decisao == 2):
                    lista = ProfAtendePaciente.ListaProfAtendePaciente()
                    formata_tabela(lista, ProfAtendePaciente.dicio)
                elif(decisao == 3):
                    lista = ProfTrabalhaHospital.ListaProfTrabalhaHospital()
                    formata_tabela(lista, ProfTrabalhaHospital.dicio)
                elif(decisao == 4):
                    lista = MedicacoesPacientes.ListaMedicacoesPacientes()
                    formata_tabela(lista, MedicacoesPacientes.dicio)
                elif(decisao == 5):
                    lista = SintomasPacientes.ListaSintomasPacientes()
                    formata_tabela(lista, SintomasPacientes.dicio)
                elif(decisao == 6):
                    lista = TestesPacientes.ListaTestesPacientes()
                    formata_tabela(lista, TestesPacientes.dicio)
                
                a = input('Enter para sair')
                break
            # volta ao menu principal
            elif(decisao == 0):
                break
        except:
            # Caso o suário coloque uma entrada inválida
            print("Entrada inválida")

    return False


#---------------------------------------------------------------------------------------

# Função que escolhe qual consulta personalizada será realizada
def ConsultasPersonalizadas():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Rastrear contatos.")
    print("2 - Ver Hospitais cheios.")
    print("3 - Informações gerais do DF")
    print("4 - Relatório Paciente")
    print("5 - Pacientes do grupo de risco")



    while(True):
        try:
            # Pega a resposta do usuário
            decisao = int(input(""))
            # De a cordo com a resposta do usuário, chama a função da consulta personalizada desejada
            if(decisao in [1, 2, 3, 4, 5]):
                if(decisao == 1):
                    RastreamentoContatos()
                elif(decisao == 2):
                    HospitaisCheios()
                elif(decisao == 3):
                   InformacoesDF()
                elif(decisao == 4):
                   RelatorioPaciente()
                elif(decisao == 5):
                   PacientesGrupoRisco()

                a = input('Enter para sair')
                break
            # Volta ao menu principal
            elif(decisao == 0):
                break
        except:
            # Caso o usuário coloque uma entrada inválida
            print("Entrada inválidaa")

    return False    

#---------------------------------------------------------------------------------------

# Função que retorna os parentes e profissionais da saúde de um paciente
def RastreamentoContatos():
    while(True):
        try:
            # Pega o Cpf do paciente desejado
            cpf = str(input("CPF Paciente: "))

            # Chama as procedures RastreiaParentesPacientes e RastreiaProfsPacientes
            lista1 = ChamaProcedure('RastreiaParentesPacientes', cpf)
            lista2 = ChamaProcedure('RastreiaProfsPacientes', cpf)
            
            # Mostra os parentes e os profissionais da saúde relacionados com o paciente
            print('\nParentes: ')
            formata_tabela(lista1, ['Nome', 'CPF'])
            print('\nProfissionais da Saúde: ')
            formata_tabela(lista2, ['Nome', 'CPF'])
            
            break
        except:
            # Caso nao seja possível encontrar os contatos do paciente
            print("Não foi possível encontrar contatos desse paciente.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

# Função que mostra todos os hospitais que tem zero leitos disponíveis
def HospitaisCheios():
    while(True):
        try:
            # Pega os ítens que estão na view vw_hospitais_cheios
            lista = SelecionaTudo("vw_hospitais_cheios")


            # Mostra os ítens formatados para o usuário
            print('\nHospitais cheios: ')
            formata_tabela(lista, ['Codigo', 'Nome', 'Cep'])

            break
        except:
            # Caso nao seja possível mostrar os hospitais cheios
            print("Não foi possível mostrar os hospitais cheios.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

# Funçãoq eu mostra as informações gerais do distrito federal, somando as situações de cada
# região de uma data especifica
def InformacoesDF():
    while(True):
        try:
            # Pega do usuário a data desejada
            data = str(input("Data da Situação: "))
            # Chama a procedure InformacoesDf passando como parâmetro a data informada
            lista = ChamaProcedure('InformacoesDf', data)
            
            # Mostra a saída da procedure.
            print('\nSituação Geral do DF: ')
            # Formata a lista para ser mostrada ao usuário
            formata_tabela(lista, ['Casos Leves', 'Casos Graves', 'Mortes', 'Recuperados'])
            
            break
        except:
            # Caso nao seja possivel mostrar a situação geral do DF
            print("Não foi possível mostrar a situação geral do DF.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

# Função que mostra todos as medicações, testes e sintomas de um paciente
def RelatorioPaciente():
    while(True):
        try:
            # Pega o CPF do paciente desejado 
            cpf = str(input("CPF Paciente: "))

            # Chama as procedures RastreiaMedicacoesPacientes, RastreiaTestesPacientes e
            # RastreiaSintomasPacientes, utilizando o CPF informado
            lista1 = ChamaProcedure('RastreiaMedicacoesPacientes', cpf)
            lista2 = ChamaProcedure('RastreiaTestesPacientes', cpf)
            lista3 = ChamaProcedure('RastreiaSintomasPacientes', cpf)
            
            # Mostra as informações formatadas das medicações
            print('\nMedicacoes: ')
            formata_tabela(lista1, ['Nome', 'Dosagem', 'DataMed'])

            # Mostra as informações formatadas dos testes
            print('\nTestes: ')
            lista_editada = []
            for x in range(len(lista2)):
                lista_editada.append(list(lista2[x]))
                if (int(lista_editada[x][2]) == 0):
                    lista_editada[x][2] = 'Negativo'
                else:
                    lista_editada[x][2] = 'Positivo'
                
            formata_tabela(lista_editada, ['Nome', 'Data', 'Resultado'])

            # Mostra as informações formatadas dos sintomas
            print('\nSintomas: ')
            formata_tabela(lista3, ['Nome', 'Tipo', 'Data'])
            
            break
        except:
            # Caso não seja possível mostrar o relatório do paciente
            print("Não foi possível encontrar o relatório do paciente.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

# Função que mostra os pacientes com mais de 60 anos
def PacientesGrupoRisco():
    while(True):
        try:
            # Pega ítens da view vw_grupo_risco
            lista = SelecionaTudo("vw_grupo_risco")

            # Mostra os ítens formatados para  usuário
            print('\nPacientes do Grupo de Risco: ')
            formata_tabela(lista, ['Cpf', 'Nome'])

            break
        except:
            # Caso naão seja possível mostrar os pacientes do grupo de risco
            print("Não foi possível mostrar os pacientes do grupo de risco.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------
