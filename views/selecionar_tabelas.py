import os
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

# NÃO IMPLEMENTADO
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
                elif(decisao == 2):
                    lista = SituacaoAtual.ListaTudoSituacaoAtual()
                elif(decisao == 3):
                    lista = Acoes.ListaTudoAcoes()
                elif(decisao == 4):
                    lista = Hospital.ListaTudoHospitais()
                elif(decisao == 5):
                    lista = Paciente.ListaTodosPacientes()
                elif(decisao == 6):
                    lista = Testes.ListaTestes()
                elif(decisao == 7):
                    lista = Sintomas.ListaSintomas()
                elif(decisao == 8):
                    lista = Medicacoes.ListaMedicacoes()
                elif(decisao == 9):
                    lista = ProfissionaisSaude.ListaProfissionaisSaude()
                elif(decisao == 10):
                    lista = Parente.ListaTodosParentes()
                
                # FORMATAR IMPRESSÃO DA LISTA
                print(lista)
                a = input('Enter para seguir')
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

