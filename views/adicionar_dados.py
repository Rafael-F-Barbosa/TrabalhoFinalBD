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

#---------------------------------------------------------------------------------------

#Função que adiciona uma regiao administrativa
def AdicionarRegiaoAdmin():

    while(True):
        try:
            #Pega os dados da regiao administrativa
            nome = str(input("Nome da regiao: "))
            populacao = int(input("Populacao: "))

            #Chama o método da classe que adiciona um ítem ao banco 
            RegioesAdmin.AdicionaRegiaoAdmin(nome,populacao)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar a região.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um hospital
def AdicionarHospital():

    while(True):
        try:
            #Pega os dados do hospital
            nome = str(input("Nome do Hospital: "))
            cep = str(input("CEP: "))
            qtdLeitosDisponiveis = int(input("Quantidade de Leitos Disponíveis: "))
            qtdLeitosOcupados = int(input("Quantidade de Leitos Ocupados: "))
            numeroPessoasComCovid = int(input("Número de pessoas com Covid-19: "))
            codRegiao = int(input("Código da Região: "))

            #Chama o método da classe que adiciona um ítem ao banco 
            Hospitais.AdicionaHospital(nome, cep, qtdLeitosDisponiveis, qtdLeitosOcupados, numeroPessoasComCovid, codRegiao)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar o Hospital.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um profissional da saúde
def AdicionarProfissional():

    while(True):
        try:
            #Pega os dados do profissional
            nome = str(input("Nome do Profissional da Saúde: "))
            cpf = str(input("CPF: "))
            profissao = str(input("Profissão: "))
            teve_covid = str(input("Já teve Covid-19 (sim/nao): "))

            #Caso o valor de teve_covid for diferente sim/nao, pedir um novo valor
            while(teve_covid != "sim" and teve_covid != "nao"):
                print("Sua resposta deve ser sim ou nao")
                teve_covid = str(input("Já teve Covid-19 (sim/nao): "))

            #Transforma sim para 1 e nao para 0 para armazenar no banco
            teve_covid_bool = 0
            if(teve_covid == "sim"):
                teve_covid_bool = 1

            #Chama o método da classe que adiciona um ítem ao banco 
            ProfissionaisSaude.AdicionaProfissionaisSaude(cpf, nome, profissao, teve_covid_bool)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar o profissional da saúde.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um paciente
def AdicionarPaciente():
    while(True):
        try:
            #Pega os dados do Paciente
            nome = str(input("Nome do Paciente: "))
            cpf = str(input("CPF: "))
            data_nasc = str(input("Data de nascimento (aaaa-mm-dd): "))
            cod_hospital = int(input("Código do Hospital: "))

            #Chama o método da classe que adiciona um ítem ao banco 
            Paciente.AdicionaPaciente(cpf, nome, data_nasc, cod_hospital)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar o paciente.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona uma medicação
def AdicionarMedicacao():
    while(True):
        try:
            #Pega os dados da medicação
            nome = str(input("Nome da medicação: "))

            #Chama o método da classe que adiciona um ítem ao banco 
            Medicacoes.AdicionaMedicacoes(nome)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar a medicação.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um teste
def AdicionarTeste():
    while(True):
        try:
            #Pega os dados do Teste
            nome = str(input("Nome do Teste: "))

            #Chama o método da classe que adiciona um ítem ao banco 
            Testes.AdicionaTestes(nome)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar o teste.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um Sintoa
def AdicionarSintoma():
    while(True):
        try:
            #Pega os dados do sintoma
            nome = str(input("Nome do Sintoma: "))
            tipo = str(input("Tipo do Sintoma (psicológico/físico): "))

            #Chama o método da classe que adiciona um ítem ao banco 
            Sintomas.AdicionaSintomas(nome, tipo)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar o sintoma.\nTente novamente.")

    return False
    
#---------------------------------------------------------------------------------------

#Função que adicina uma situação atual
def AdicionarSituacaoAtual():
    while(True):
        try:
            #Pega os dados da situação atual
            data          = str(input("Data (aaaa-mm-dd): "))
            cod_reg       = int(input("Código da Região: "))
            casos_leves   = int(input("Número de casos Leves: "))
            casos_graves  = int(input("Número de casos Graves: "))
            mortos        = int(input("Número de mortos: "))
            recuperados   = int(input("Número de recuperados: "))

            #Chama o método da classe que adiciona um ítem ao banco 
            SituacaoAtual.AdicionaSituacaoAtual(data, casos_leves, casos_graves, mortos, recuperados, cod_reg)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar a situação atual.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona uma Ação
def AdicionarAcao():
    while(True):
        try:
            #Pega os dados da ação
            cod_reg = str(input("Código da Região: "))
            tipo = str(input("Tipo de ação: "))
            eficiencia = str(input("Eficiência (0 a 5): "))

            #Chama o método da classe que adiciona um ítem ao banco 
            Acoes.AdicionaAcoes(eficiencia, tipo, cod_reg)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar a Ação.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------

#Função que adiciona um parente
def AdicionarParente():
    while(True):
        try:
            #Pega os dados do parente
            nome = str(input("Nome do Parente: "))
            cpf = str(input("CPF: "))
            data_nasc = str(input("Data de nascimento (aaaa-mm-dd): "))
            teve_contato = str(input("Teve contato com o paciente (sim/nao): "))

            #Caso o valor de teve_covid for diferente sim/nao, pedir um novo valor
            while(teve_contato != "sim" and teve_contato != "nao"):
                print("Sua resposta deve ser sim ou nao")
                teve_contato = str(input("Teve contato com o paciente (sim/nao): "))

            #Transforma sim para 1 e nao para 0 para armazenar no banco
            teve_contato_bool = 0
            if(teve_contato == "sim"):
                teve_contato_bool = 1

            #Chama o método da classe que adiciona um ítem ao banco 
            Parente.AdicionaParente(cpf, nome, data_nasc, teve_contato_bool)
            break
        except:
            #Caso não seja possível adicionar
            print("Não foi possivel adicionar o parente.\nTente novamente.")

    return False

#---------------------------------------------------------------------------------------
