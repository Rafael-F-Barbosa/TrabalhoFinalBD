from entidades.RegioesAdmin import RegioesAdmin
from entidades.SituacaoAtual import SituacaoAtual
from entidades.Acoes import Acoes
from entidades.Hospitais import Hospitais as Hospital
from entidades.Pacientes import Paciente
from entidades.Testes import Testes
from entidades.TestesPacientes import TestesPacientes
from entidades.Sintomas import Sintomas
from entidades.SintomasPacientes import SintomasPacientes
from entidades.Medicacoes import Medicacoes
from entidades.MedicacoesPacientes import MedicacoesPacientes
from entidades.ProfissionaisSaude import ProfissionaisSaude
from entidades.ProfTrabalhaHospital import ProfTrabalhaHospital
from entidades.ProfAtendePaciente import ProfAtendePaciente
from entidades.Parentes import Parente
from entidades.ParentePaciente import ParentePaciente


def AdicionarParentesPacientes():
    while(True):
        try:
            cpf_paciente = str(input("CPF do Paciente: "))
            cpf_parente = str(input("CPF do Parente: "))
            ParentePaciente.AdicionaParentePaciente(cpf_paciente, cpf_parente)
            break
        except:
            print("Não foi possivel adicionar relação entre parente e paciente.\nTente novamente.")

    return False


def AdicionarProfissionaisPacientes():
    while(True):
        try:
            cpf_paciente = str(input("CPF do Paciente: "))
            cpf_profissional = str(input("CPF do Profissional da Saúde: "))
            ProfAtendePaciente.AdicionaProfAtendePaciente(cpf_paciente, cpf_profissional)
            break
        except:
            print("Não foi possivel adicionar relação entre paciente e profissional da saúde.\nTente novamente.")

    return False


def AdicionarProfissionaisHospitais():
    while(True):
        try:
            cod_hospital = str(input("Código do Hospital: "))
            cpf_profissional = str(input("CPF do Profissional da Saúde: "))
            ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(cod_hospital, cpf_profissional)
            break
        except:
            print("Não foi possivel adicionar relação entre hospital e profissional da saúde.\nTente novamente.")

    return False



def AdicionarPacientesMedicacoes():
    while(True):
        try:
            data = str(input("Data da prescrição da Medicação (aaaa-mm-dd): "))
            dosagem = str(input("Dosagem da Medicação: "))
            cod_med = str(input("Código da Medicação: "))
            cpf_paciente = str(input("CPF do Paciente: "))

            MedicacoesPacientes.AdicionaMedicacoesPacientes(data, dosagem, cod_med, cpf_paciente)
            break
        except:
            print("Não foi possivel adicionar relação entre paciente e medicação.\nTente novamente.")

    return False


def AdicionarPacientesSintomas():
    while(True):
        try:
            data = str(input("Data do início do Sintoma (aaaa-mm-dd): "))
            cod_sin = str(input("Código do Sintoma: "))
            cpf_paciente = str(input("CPF do Paciente: "))

            SintomasPacientes.AdicionaSintomasPacientes(data, cod_sin, cpf_paciente)
            break
        except:
            print("Não foi possivel adicionar relação entre paciente e sintoma.\nTente novamente.")

    return False


def AdicionarPacientesTestes():
    while(True):
        try:
            data = str(input("Data de realização do teste (aaaa-mm-dd): "))
            cod_teste = str(input("Código do Teste: "))
            cpf_paciente = str(input("CPF do Paciente: "))
            resultado = str(input("Resultado do Teste: "))

            SintomasPacientes.AdicionaSintomasPacientes(data, resultado, cod_teste, cpf_paciente)
            break
        except:
            print("Não foi possivel adicionar relação entre paciente e teste.\nTente novamente.")

    return False