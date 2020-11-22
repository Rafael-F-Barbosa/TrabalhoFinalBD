import os
from views.adicionar_dados import *

def main():
    sair = False;
    while(sair == False):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\tBANCO DE DADOS\n\t\t   COVID19\n")
        print("Pressione enter para começar.")
        a = input('')
        sair = dec_adicionar_ou_ver_dados()
        
    print("Programa encerrado.")


# dec = decisao
def dec_adicionar_ou_ver_dados():
    sair = False
    while(sair == False):
        while(True):
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("O que você deseja fazer: ")
                print("1 - Ver informações sobre a pandemia.")
                print("2 - Adicionar dados sobre a pandemia.")
                print("3 - Voltar para o início.")
                print("4 - Finalizar programa.")
                decisao = int(input(""))
                if(decisao in [1,2,3,4]):
                    break;
            except:
                print("Entrada inválida")
        
        if(decisao == 1):
            print(decisao)
        elif(decisao == 2):
            sair = dec_adicionar_dados()
        elif(decisao == 3):
            return False
        else:
            return True

    # return False

# dec = decisao
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
            if(decisao in [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]):
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

    return False
