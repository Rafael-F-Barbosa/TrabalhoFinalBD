
from entidades.TestesPacientes import TestesPacientes
from entidades.SintomasPacientes import SintomasPacientes
from entidades.MedicacoesPacientes import MedicacoesPacientes
from entidades.ProfTrabalhaHospital import ProfTrabalhaHospital
from entidades.ProfAtendePaciente import ProfAtendePaciente
from entidades.ParentePaciente import ParentePaciente


#---------------------------------------------------------------------------------------
# Função que recebe uma lista de atrinutos de uma classe como entrada e atualiza o valor
# escolhido pelo usuário
def Atualizar(lista):
    # Decide o por qual parâmetro a tabela será atualizada
    print("Por qual parâmetro você quer atualizar: ")
    for l in range(len(lista)):
        print(l + 1, " - ", lista[l])
    coluna2 = int(input(""))
    # Pega o valor que será buscado no banco de dados
    print("Qual o valor do ", lista[coluna2 - 1], " que você deseja atualizar: ")
    valor2 = str(input(""))
    # Decide qual coluna será atualizada
    print("Qual parâmetro você quer atualizar: ")
    for l in range(len(lista)):
        print(l + 1, " - ", lista[l])
    coluna1 = int(input(""))
    # Decide o novo valor que será colocado no banco de dados
    print("Qual novo valor de  ", lista[coluna1 - 1], ": ")
    valor1 = str(input(""))

    return coluna1,valor1, coluna2, valor2


#---------------------------------------------------------------------------------------

# Função específica para atualização da tabela de MedicaçãoPacientes, utilizando Atualizar()
def AtualizarMedicacoesPaciente():
    while(True):
        try:
            # Obtém valores para atualização e chama a função do modelo
            coluna1, valor1, coluna2, valor2 = Atualizar(MedicacoesPacientes.dicio)
            MedicacoesPacientes.AtualizaMedicacoesPacientes(MedicacoesPacientes.dicio[coluna1-1], valor1, MedicacoesPacientes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a medicacao do paciente.\nTente novamente.")
    return False

#---------------------------------------------------------------------------------------

# Função específica para atualização da tabela de ParentePacientes, utilizando Atualizar()
def AtualizarParentePaciente():
    while(True):
        try:
            # Obtém valores para atualização e chama a função do modelo
            coluna1, valor1, coluna2, valor2 = Atualizar(ParentePaciente.dicio)
            ParentePaciente.AtualizaParentePaciente(ParentePaciente.dicio[coluna1-1], valor1, ParentePaciente.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a relação entre o parente e o paciente.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

# Função específica para atualização da tabela de ProfissionaisPacientes, utilizando Atualizar()
def AtualizarProfissionalPaciente():
    while(True):
        try:
            # Obtém valores para atualização e chama a função do modelo
            coluna1, valor1, coluna2, valor2 = Atualizar(ProfAtendePaciente.dicio)
            ProfAtendePaciente.AtualizaProfissionalPaciente(ProfAtendePaciente.dicio[coluna1-1], valor1, ProfAtendePaciente.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a relação entre o profissional e o paciente.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

# Função específica para atualização da tabela de ProfissionaisHospitais, utilizando Atualizar()
def AtualizarProfissionalHospital():
    while(True):
        try:
            # Obtém valores para atualização e chama a função do modelo
            coluna1, valor1, coluna2, valor2 = Atualizar(ProfTrabalhaHospital.dicio)
            ProfTrabalhaHospital.AtualizaProfissionalHospital(ProfTrabalhaHospital.dicio[coluna1-1], valor1, ProfTrabalhaHospital.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar a relação entre o profissional e o hospital.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

# Função específica para atualização da tabela de SintomasPacientes, utilizando Atualizar()
def AtualizarSintomasPacientes():
    while(True):
        try:
            # Obtém valores para atualização e chama a função do modelo
            coluna1, valor1, coluna2, valor2 = Atualizar(SintomasPacientes.dicio)
            SintomasPacientes.AtualizaSintomasPacientes(SintomasPacientes.dicio[coluna1-1], valor1, SintomasPacientes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar os sintomas do paciente.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

# Função específica para atualização da tabela de TestesPacientes, utilizando Atualizar()
def AtualizarTestesPacientes():
    while(True):
        try:
            # Obtém valores para atualização e chama a função do modelo
            coluna1, valor1, coluna2, valor2 = Atualizar(TestesPacientes.dicio)
            TestesPacientes.AtualizaTestesPacientes(TestesPacientes.dicio[coluna1-1], valor1, TestesPacientes.dicio[coluna2-1], valor2)
            break
        except:
            print("Não foi possivel atualizar os testes do paciente.\nTente novamente.")

    return False
