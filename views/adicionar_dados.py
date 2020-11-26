from entidades.RegioesAdmin import RegioesAdmin
from entidades.SituacaoAtual import SituacaoAtual
from entidades.Hospitais import Hospitais
from entidades.ProfissionaisSaude import ProfissionaisSaude
from entidades.Pacientes import Paciente
from entidades.Testes import Testes
from entidades.Sintomas import Sintomas
from entidades.Medicacoes import Medicacoes
from entidades.Acoes import Acoes
from entidades.Parentes import Parente



def AdcionarRegiaoAdmin():

    while(True):
        try:
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))
            RegioesAdmin.AdicionaRegiaoAdmin(nome,populacao)
            break
        except:
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False

def AdicionarHospital():

    while(True):
        try:
            nome = str(input("Nome do Hospital: "))
            cep = str(input("CEP: "))
            qtdLeitosDisponiveis = int(input("Quantidade de Leitos Disponíveis: "))
            qtdLeitosOcupados = int(input("Quantidade de Leitos Ocupados: "))
            numeroPessoasComCovid = int(input("Número de pessoas com Covid-19: "))
            codRegiao = int(input("Código da Região: "))


            Hospitais.AdicionaHospital(nome, cep, qtdLeitosDisponiveis, qtdLeitosOcupados, numeroPessoasComCovid, codRegiao)
            break
        except:
            print("Não foi possivel adicionar o Hospital.\nTente novamente.")

    return False

def AdicionarProfissional():

    while(True):
        try:
            nome = str(input("Nome do Profissional da Saúde: "))
            cpf = str(input("CPF: "))
            profissao = str(input("Profissão: "))
            teve_covid = str(input("Já teve Covid-19 (sim/nao): "))

            while(teve_covid != "sim" and teve_covid != "nao"):
                print("Sua resposta deve ser sim ou nao")
                teve_covid = str(input("Já teve Covid-19 (sim/nao): "))

            teve_covid_bool = 0
            if(teve_covid == "sim"):
                teve_covid_bool = 1

            ProfissionaisSaude.AdicionaProfissionaisSaude(cpf, nome, profissao, teve_covid_bool)
            break
        except:
            print("Não foi possivel adicionar o profissional da saúde.\nTente novamente.")

    return False


def AdicionarPaciente():
    while(True):
        try:
            nome = str(input("Nome do Paciente: "))
            cpf = str(input("CPF: "))
            data_nasc = str(input("Data de nascimento (aaaa-mm-dd): "))
            cod_hospital = int(input("Código do Hospital: "))

            Paciente.AdicionaPaciente(cpf, nome, data_nasc, cod_hospital)
            break
        except:
            print("Não foi possivel adicionar o paciente.\nTente novamente.")

    return False

def AdicionarMedicacao():
    while(True):
        try:
            nome = str(input("Nome da medicação: "))

            Medicacoes.AdicionaMedicacoes(nome)
            break
        except:
            print("Não foi possivel adicionar a medicação.\nTente novamente.")

    return False

def AdicionarTeste():
    while(True):
        try:
            nome = str(input("Nome do Teste: "))

            Testes.AdicionaTestes(nome)
            break
        except:
            print("Não foi possivel adicionar o teste.\nTente novamente.")

    return False

def AdicionarSintoma():
    while(True):
        try:
            nome = str(input("Nome do Sintoma: "))
            tipo = str(input("Tipo do Sintoma (psicológico/físico): "))

            Sintomas.AdicionaSintomas(nome, tipo)
            break
        except:
            print("Não foi possivel adicionar o sintoma.\nTente novamente.")

    return False


def AdicionarSituacaoAtual():
    while(True):
        try:
            data          = str(input("Data (aaaa-mm-dd): "))
            cod_reg       = int(input("Código da Região: "))
            casos_leves   = int(input("Número de casos Leves: "))
            casos_graves  = int(input("Número de casos Graves: "))
            mortos        = int(input("Número de mortos: "))
            recuperados   = int(input("Número de recuperados: "))

            SituacaoAtual.AdicionaSituacaoAtual(data, casos_leves, casos_graves, mortos, recuperados, cod_reg)
            break
        except:
            print("Não foi possivel adicionar a situação atual.\nTente novamente.")

    return False


def AdicionarAcao():
    while(True):
        try:
            cod_reg = str(input("Código da Região: "))
            tipo = str(input("Tipo de ação: "))
            eficiencia = str(input("Eficiência (0 a 5): "))


            Acoes.AdicionaAcoes(eficiencia, tipo, cod_reg)
            break
        except:
            print("Não foi possivel adicionar a Ação.\nTente novamente.")

    return False

def AdicionarParente():
    while(True):
        try:
            nome = str(input("Nome do Parente: "))
            cpf = str(input("CPF: "))
            data_nasc = str(input("Data de nascimento (aaaa-mm-dd): "))
            teve_contato = str(input("Teve contato com o paciente (sim/nao): "))

            while(teve_contato != "sim" and teve_contato != "nao"):
                print("Sua resposta deve ser sim ou nao")
                teve_contato = str(input("Teve contato com o paciente (sim/nao): "))

            teve_contato_bool = 0
            if(teve_contato == "sim"):
                teve_contato_bool = 1

            Parente.AdicionaParente(cpf, nome, data_nasc, teve_contato_bool)
            break
        except:
            print("Não foi possivel adicionar o parente.\nTente novamente.")

    return False