import os
from util.formata import imprime_lista_tabela_formatado as formata_tabela

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

# NÃO IMPLEMENTADO
def VerRelatorioPersonalizado():
    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome,populacao);
            break;
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False



# INCOMPLENTO
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
            decisao = int(input(""))
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
                
                # FORMATAR IMPRESSÃO DA LISTA
                a = input('Enter para sair')
                break

            elif(decisao == 0):
                break
        except:
            print("Entrada inválida.")

    return False

# NÃO IMPLEMENTADO
def VerTabelasRelacoes():
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
def RastreamentoContatos():
    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome,populacao);
            break;
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False

