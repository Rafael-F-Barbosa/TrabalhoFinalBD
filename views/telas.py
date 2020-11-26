import os
from views.adicionar_dados import *
from views.adicionar_relacoes import *


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
                print("7 - Voltar para o início.")
                print("8 - Finalizar programa.")
                decisao = int(input(""))
                if(decisao in [1, 2, 3, 4, 5, 6, 7, 8]):
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
            sair = dec_atualizar_dados() # Arrumar 
        elif(decisao == 5):
            sair = dec_adicionar_dados() # Arrumar 
        elif(decisao == 6):
            sair = dec_adicionar_dados() # Arrumar 
        elif(decisao == 7):
            return False
        elif(decisao == 8):
            return True

    return False

# Acho que tá ok essa aqui
def dec_ver_informacoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O que você deseja fazer ")
    print("0 - Voltar ao menu principal.")
    print("1 - Ver relatório personalizado.")
    print("2 - Ver tabelas de dados.")
    print("3 - Ver tabelas de relações.")
    print("4 - Rastrear contatos.")

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
        return VerRelatorioPersonalizado()

    elif(decisao == 2):
        return VerTabelasDados()

    elif(decisao == 3):
        return VerTabelasRelacoes()

    elif(decisao == 4):
        return RastreamentoContatos()


    return False

# decide em qual tabela será feita a adição - Incompleto
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
        return AdcionarRegiaoAdmin()

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


# decide em qual tabela será feita a adição de relacao
# Não implementado
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
            if(decisao in [0, 1, 2, 3, 4, 5, 6, 7]):
                break
        except:
            print("Entrada inválida")

    if(decisao == 0):
        return False

    elif(decisao == 1):
        return AdcionarRegiaoAdmin()

    elif(decisao == 2):
        return SituacaoAtual()

    elif(decisao == 3):
        print(decisao)

    elif(decisao == 4):
        print(decisao)

    elif(decisao == 5):
        print(decisao)

    elif(decisao == 6):
        print(decisao)

    elif(decisao == 7):
        print(decisao)

    return False
