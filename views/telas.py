import os
from views.adicionar_dados import *
from views.adicionar_relacoes import *
from views.atualizar_dados import *
from views.selecionar_tabelas import *
from views.atualizar_relacoes import *
import views.deletar as deletar



def main():
    sair = False
    while(sair == False):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\t\tBANCO DE DADOS\n\t\t   COVID19\n")
        print("Pressione enter para começar.")
        a = input('')
        sair = dec_apresenta_funcionalidades()

    print("Programa encerrado.")

def dec_apresenta_funcionalidades():
    sair = False
    while(sair == False):
        while(True):
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("O que você deseja fazer: ")
                print("1 - Ver informações sobre a pandemia.")
                print("2 - Adicionar dados sobre a pandemia.")
                print("3 - Adicionar relacionamenos.")
                print("4 - Atualizar dados sobre a pandemia.")
                print("5 - Atualizar relacionamentos.")
                print("6 - Deletar dados.")
                print("7 - Deletar relacionamentos.")
                print("8 - Voltar para o início.")
                print("9 - Finalizar programa.")
                decisao = int(input(""))
                if(decisao in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
                    break
            except:
                print("Entrada inválida")

        if(decisao == 1):
            sair = dec_ver_informacoes()
        elif(decisao == 2):
            sair = dec_adicionar_dados()
        elif(decisao == 3):
            sair = dec_adicionar_relacoes()
        elif(decisao == 4):
            sair = dec_atualizar_dados()
        elif(decisao == 5):
            sair = dec_atualizar_relacoes() 
        elif(decisao == 6):
            sair = dec_deletar_dados() 
        elif(decisao == 7):
            sair = dec_deletar_relacoes() 
        elif(decisao == 8):
            return False
        elif(decisao == 9):
            return True

    return False

def dec_ver_informacoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Consultas personalizadas.")
    print("2 - Ver tabelas de dados.")
    print("3 - Ver tabelas de relações.")

    while(True):
        try:
            decisao = int(input(""))
            if(decisao in [0, 1, 2, 3, 4]):
                break
        except:
            print("Entrada inválida")

    if(decisao == 0):
        return False

    elif(decisao == 1):
        return ConsultasPersonalizadas()

    elif(decisao == 2):
        return VerTabelasDados()

    elif(decisao == 3):
        return VerTabelasRelacoes()

    return False


def dec_adicionar_dados():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Adicionar regiao administrativa.")
    print("2 - Adicionar situacao atual.")
    print("3 - Adicionar ação.")
    print("4 - Adicionar hospital.")
    print("5 - Adicionar paciente.")
    print("6 - Adicionar teste.")
    print("7 - Adicionar sintoma.")
    print("8 - Adicionar medicação.")
    print("9 - Adicionar profissional saúde.")
    print("10 - Adicionar parente.")

    while(True):
        try:
            decisao = int(input(""))
            if(decisao in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                break
        except:
            print("Entrada inválida")

    if(decisao == 0):
        return False

    elif(decisao == 1):
        return AdicionarRegiaoAdmin()

    elif(decisao == 2):
        return AdicionarSituacaoAtual()

    elif(decisao == 3):
        return AdicionarAcao()

    elif(decisao == 4):
        return AdicionarHospital()

    elif(decisao == 5):
        return AdicionarPaciente()

    elif(decisao == 6):
        return AdicionarTeste()

    elif(decisao == 7):
        return AdicionarSintoma()

    elif(decisao == 8):
        return AdicionarMedicacao()

    elif(decisao == 9):
        return AdicionarProfissional()

    elif(decisao == 10):
        return AdicionarParente()

    return False


def dec_adicionar_relacoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Relacionar parentes e pacientes.")
    print("2 - Relacionar profissionais da saúde e pacientes.")
    print("3 - Relacionar profissionais da saúde e hospitais.")
    print("4 - Relacionar pacientes e medicações.")
    print("5 - Relacionar pacientes com sintomas.")
    print("6 - Relacionar pacientes com testes.")

    while(True):
        try:
            decisao = int(input(""))
            if(decisao in [0, 1, 2, 3, 4, 5, 6]):
                break
        except:
            print("Entrada inválida")

    if(decisao == 0):
        return False

    elif(decisao == 1):
        return AdicionarParentesPacientes()

    elif(decisao == 2):
        return AdicionarProfissionaisPacientes()

    elif(decisao == 3):
        return AdicionarProfissionaisHospitais()

    elif(decisao == 4):
        return AdicionarPacientesMedicacoes()

    elif(decisao == 5):
        return AdicionarPacientesSintomas()

    elif(decisao == 6):
        return AdicionarPacientesTestes()


    return False


def dec_atualizar_dados():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Atualizar regiao administrativa.")
    print("2 - Atualizar situacao atual.")
    print("3 - Atualizar ação.")
    print("4 - Atualizar hospital.")
    print("5 - Atualizar paciente.")
    print("6 - Atualizar teste.")
    print("7 - Atualizar sintoma.")
    print("8 - Atualizar medicação.")
    print("9 - Atualizar profissional saúde.")
    print("10 - Atualizar parente.")

    while(True):
        try:
            decisao = int(input(""))
            if(decisao in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                break
        except:
            print("Entrada inválida")

    if(decisao == 0):
        return False

    elif(decisao == 1):
        return AtualizarRegiao()

    elif(decisao == 2):
        return AtualizarSituacao()

    elif(decisao == 3):
        return AtualizarAcao()

    elif(decisao == 4):
        return AtualizarHospital()

    elif(decisao == 5):
        return AtualizarPaciente()

    elif(decisao == 6):
        return AtualizarTestes()

    elif(decisao == 7):
        return AtualizarSintomas()

    elif(decisao == 8):
        return AtualizarMedicacao()

    elif(decisao == 9):
        return AtualizarProfissional()

    elif(decisao == 10):
        return AtualizarParente()

    return False


# decide em qual tabela será feita a atualização de relacao
def dec_atualizar_relacoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Atualizar parentes e pacientes.")
    print("2 - Atualizar profissionais da saúde e pacientes.")
    print("3 - Atualizar profissionais da saúde e hospitais.")
    print("4 - Atualizar pacientes e medicações.")
    print("5 - Atualizar pacientes com sintomas.")
    print("6 - Atualizar pacientes com testes.")

    while(True):
        try:
            decisao = int(input(""))
            if(decisao in [0, 1, 2, 3, 4, 5, 6]):
                break
        except:
            print("Entrada inválida")

    if(decisao == 0):
        return False

    elif(decisao == 1):
        return AtualizarParentePaciente()

    elif(decisao == 2):
        return AtualizarProfissionalPaciente()

    elif(decisao == 3):
        return AtualizarProfissionalHospital()

    elif(decisao == 4):
        return AtualizarMedicacoesPaciente()

    elif(decisao == 5):
        return AtualizarSintomasPacientes()

    elif(decisao == 6):
        return AtualizarTestesPacientes()


    return False


# decide em qual tabela será deletado 
def dec_deletar_dados():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Deletar regiao administrativa.")
    print("2 - Deletar situacao atual.")
    print("3 - Deletar ação.")
    print("4 - Deletar hospital.")
    print("5 - Deletar paciente.")
    print("6 - Deletar teste.")
    print("7 - Deletar sintoma.")
    print("8 - Deletar medicação.")
    print("9 - Deletar profissional saúde.")
    print("10 - Deletar parente.")

    while(True):
        try:
            decisao = int(input(""))
            if(decisao in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                break
        except:
            print("Entrada inválida")

    if(decisao == 0):
        return False

    elif(decisao == 1):
        lista = RegioesAdmin.dicio
        tabela = "RegiaoAdmin"

    elif(decisao == 2):
        lista = SituacaoAtual.dicio
        tabela = "SituacaoAtual"

    elif(decisao == 3):
        lista = Acoes.dicio
        tabela = "Acoes"

    elif(decisao == 4):
        lista = Hospitais.dicio
        tabela = "Hospitais"

    elif(decisao == 5):
        lista = Paciente.dicio
        tabela = "Pacientes"

    elif(decisao == 6):
        lista = Testes.dicio
        tabela = "Testes"

    elif(decisao == 7):
        lista = Sintomas.dicio
        tabela = "Sintomas"

    elif(decisao == 8):
        lista = Medicacoes.dicio
        tabela = "Medicacoes"

    elif(decisao == 9):
        lista = ProfissionaisSaude.dicio
        tabela = "ProfissionaisSaude"

    elif(decisao == 10):
        lista = Parente.dicio
        tabela = "Parentes"

    deletar.Deletar(tabela, lista)


    return False

 
def dec_deletar_relacoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Deletar relação entre parentes e pacientes.")
    print("2 - Deletar relação entre profissionais da saúde e pacientes.")
    print("3 - Deletar relação entre profissionais da saúde e hospitais.")
    print("4 - Deletar relação entre pacientes e medicações.")
    print("5 - Deletar relação entre pacientes com sintomas.")
    print("6 - Deletar relação entre pacientes com testes.")

    while(True):
        try:
            decisao = int(input(""))
            if(decisao in [0, 1, 2, 3, 4, 5, 6]):
                break
        except:
            print("Entrada inválida")

    if(decisao == 0):
        return False

    elif(decisao == 1):
        lista = ParentePaciente.dicio
        tabela = "ParentePaciente"

    elif(decisao == 2):
        lista = ProfAtendePaciente.dicio
        tabela = "ProfAtendePaciente"

    elif(decisao == 3):
        lista = ProfTrabalhaHospital.dicio
        tabela = "ProfTrabalhaHospital"

    elif(decisao == 4):
        lista = MedicacoesPacientes.dicio
        tabela = "MedicacoesPacientes"

    elif(decisao == 5):
        lista = SintomasPacientes.dicio
        tabela = "SintomasPacientes"

    elif(decisao == 6):
        lista = TestesPacientes.dicio
        tabela = "TestesPacientes"

    deletar.Deletar(tabela, lista)

    return False