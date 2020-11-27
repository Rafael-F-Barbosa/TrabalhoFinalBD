
from entidades.TestesPacientes import TestesPacientes
from entidades.SintomasPacientes import SintomasPacientes
from entidades.MedicacoesPacientes import MedicacoesPacientes
from entidades.ProfTrabalhaHospital import ProfTrabalhaHospital
from entidades.ProfAtendePaciente import ProfAtendePaciente
from entidades.ParentePaciente import ParentePaciente


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



def AtualizarMedicacoesPaciente():

    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(MedicacoesPacientes.dicio)
            MedicacoesPacientes.AtualizaMedicacoesPacientes(MedicacoesPacientes.dicio[coluna1-1], valor1, MedicacoesPacientes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a medicacao do paciente.\nTente novamente.")

    return False

def AtualizarParentePaciente():

    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(ParentePaciente.dicio)
            ParentePaciente.AtualizaParentePaciente(ParentePaciente.dicio[coluna1-1], valor1, ParentePaciente.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a relação entre o parente e o paciente.\nTente novamente.")

    return False

def AtualizarProfissionalPaciente():

    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(ProfAtendePaciente.dicio)
            ProfAtendePaciente.AtualizaProfissionalPaciente(ProfAtendePaciente.dicio[coluna1-1], valor1, ProfAtendePaciente.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a relação entre o profissional e o paciente.\nTente novamente.")

    return False


def AtualizarProfissionalHospital():

    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(ProfTrabalhaHospital.dicio)
            ProfTrabalhaHospital.AtualizaProfissionalHospital(ProfTrabalhaHospital.dicio[coluna1-1], valor1, ProfTrabalhaHospital.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a relação entre o profissional e o hospital.\nTente novamente.")

    return False


def AtualizarSintomasPacientes():

    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(SintomasPacientes.dicio)
            SintomasPacientes.AtualizaSintomasPacientes(SintomasPacientes.dicio[coluna1-1], valor1, SintomasPacientes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar os sintomas do paciente.\nTente novamente.")

    return False

def AtualizarTestesPacientes():

    while(True):
        try:
            coluna1, valor1, coluna2, valor2 = Atualizar(TestesPacientes.dicio)
            TestesPacientes.AtualizaTestesPacientes(TestesPacientes.dicio[coluna1-1], valor1, TestesPacientes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar os testes do paciente.\nTente novamente.")

    return False