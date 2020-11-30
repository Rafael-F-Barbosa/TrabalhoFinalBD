
from entidades.TestesPacientes import TestesPacientes
from entidades.SintomasPacientes import SintomasPacientes
from entidades.MedicacoesPacientes import MedicacoesPacientes
from entidades.ProfTrabalhaHospital import ProfTrabalhaHospital
from entidades.ProfAtendePaciente import ProfAtendePaciente
from entidades.ParentePaciente import ParentePaciente

#---------------------------------------------------------------------------------------

#Função que adiciona um relacionamento entre um parente e um paciente
def AdicionarParentesPacientes():
    while(True):
        try:
            #Pega os dados da relação
            cpf_paciente = str(input("CPF do Paciente: "))
            cpf_parente = str(input("CPF do Parente: "))
            #Chama o método da classe que adiciona um ítem ao banco 
            ParentePaciente.AdicionaParentePaciente(cpf_paciente, cpf_parente)
            break
        except:
            #Caso não seja possível adicionar a relação
            print("Não foi possivel adicionar relação entre parente e paciente.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um relacionamento entre um profissional da saúde e um paciente
def AdicionarProfissionaisPacientes():
    while(True):
        try:
            #Pega os dados da relação
            cpf_paciente = str(input("CPF do Paciente: "))
            cpf_profissional = str(input("CPF do Profissional da Saúde: "))
            #Chama o método da classe que adiciona um ítem ao banco 
            ProfAtendePaciente.AdicionaProfAtendePaciente(cpf_paciente, cpf_profissional)
            break
        except:
            #Caso não seja possível adicionar a relação
            print("Não foi possivel adicionar relação entre paciente e profissional da saúde.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um relacionamento entre um profissional da saúde e um hospital
def AdicionarProfissionaisHospitais():
    while(True):
        try:
            #Pega os dados da relação
            cod_hospital = str(input("Código do Hospital: "))
            cpf_profissional = str(input("CPF do Profissional da Saúde: "))
            #Chama o método da classe que adiciona um ítem ao banco 
            ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(cod_hospital, cpf_profissional)
            break
        except:
            #Caso não seja possível adicionar a relação
            print("Não foi possivel adicionar relação entre hospital e profissional da saúde.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um relacionamento entre um paciente e uma medicação
def AdicionarPacientesMedicacoes():
    while(True):
        try:
            #Pega os dados da relação
            data = str(input("Data da prescrição da Medicação (aaaa-mm-dd): "))
            dosagem = str(input("Dosagem da Medicação: "))
            cod_med = str(input("Código da Medicação: "))
            cpf_paciente = str(input("CPF do Paciente: "))
            #Chama o método da classe que adiciona um ítem ao banco 
            MedicacoesPacientes.AdicionaMedicacoesPacientes(data, dosagem, cod_med, cpf_paciente)
            break
        except:
            #Caso não seja possível adicionar a relação
            print("Não foi possivel adicionar relação entre paciente e medicação.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um relacionamento entre um paciente e um sintoma
def AdicionarPacientesSintomas():
    while(True):
        try:
            #Pega os dados da relação
            data = str(input("Data do início do Sintoma (aaaa-mm-dd): "))
            cod_sin = str(input("Código do Sintoma: "))
            cpf_paciente = str(input("CPF do Paciente: "))
            #Chama o método da classe que adiciona um ítem ao banco 
            SintomasPacientes.AdicionaSintomasPacientes(data, cod_sin, cpf_paciente)
            break
        except:
            #Caso não seja possível adicionar a relação
            print("Não foi possivel adicionar relação entre paciente e sintoma.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um relacionamento entre um paciente e um teste
def AdicionarPacientesTestes():
    while(True):
        try:
            #Pega os dados da relação
            data = str(input("Data de realização do teste (aaaa-mm-dd): "))
            cod_teste = str(input("Código do Teste: "))
            cpf_paciente = str(input("CPF do Paciente: "))
            resultado = str(input("Resultado do Teste: "))
            #Chama o método da classe que adiciona um ítem ao banco 
            SintomasPacientes.AdicionaSintomasPacientes(data, resultado, cod_teste, cpf_paciente)
            break
        except:
            #Caso não seja possível adicionar a relação
            print("Não foi possivel adicionar relação entre paciente e teste.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------
