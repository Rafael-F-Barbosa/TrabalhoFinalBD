# Preenche o banco de dados inicialmente
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

def preenche_banco_inicialmente():
    # RegioesAdmin
    # AdicionaRegiaoAdmin(nome, populacao)
    RegioesAdmin.AdicionaRegiaoAdmin('Ceilândia', 489351)
    RegioesAdmin.AdicionaRegiaoAdmin('Samambaia', 254439)
    RegioesAdmin.AdicionaRegiaoAdmin('Taguatinga', 222598)
    RegioesAdmin.AdicionaRegiaoAdmin('Plano Piloto', 50000)
    RegioesAdmin.AdicionaRegiaoAdmin('Planaltina', 189421)
    RegioesAdmin.AdicionaRegiaoAdmin('Águas Claras', 148940)
    RegioesAdmin.AdicionaRegiaoAdmin('Recanto das Emas', 145304)
    RegioesAdmin.AdicionaRegiaoAdmin('Gama', 141911)



    # SituacaoAtual
    # AdicionaSituacaoAtual(dataSituacao, casosLeves, casosGraves, mortes, recuperados, codRegiao)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-27', 100, 145, 450, 5, 1)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-28', 100, 435, 445, 5, 2)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 105, 15, 145, 5, 2)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-25', 100, 45, 245, 5, 4)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-12', 2000, 35, 445, 5, 4)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-26', 50, 15, 465, 5, 6)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-25', 155, 5, 415, 5, 5)

     

    # Acoes # Se pá não faz sentido desse jeito que tá relacionado preferia que tivesse um código na região que executa a ação
    # AdicionaAcoes(eficiencia, tipo, codRegiao) 
    Acoes.AdicionaAcoes(5, "Fechamento de comércios", 4)
    Acoes.AdicionaAcoes(4, "Auxílio alimentação", 5)
    Acoes.AdicionaAcoes(5, "Testagem em massa", 4)
    Acoes.AdicionaAcoes(3, "Campanhas de conscientização", 3)
    Acoes.AdicionaAcoes(4, "Rastreamento de contatos", 2)


    # Hospitais
    # AdicionaHospital(nome, cep, qtdLeitosDisponiveis, qtdLeitosOcupados, numeroPessoasComCovid, codRegiao)
    Hospital.AdicionaHospital("HRAN", "73365456", 45, 45, 45, 4)
    Hospital.AdicionaHospital("HRP", "73365457", 45, 45, 45, 5)
    Hospital.AdicionaHospital("Hospital de Base", "73365458", 45, 45, 45, 4)
    Hospital.AdicionaHospital("HRT", "73365459", 45, 45, 45, 3)
    Hospital.AdicionaHospital("HRG", "73365433", 45, 45, 45, 8)

    # Pacientes
    # AdicionaPaciente(cpf, nome, dataNascimento, codHospital)
    Paciente.AdicionaPaciente("18229735114", "Joãozinho da Silva", "1993-02-21", 1) # tentando inserir o mesmo CPF pra testar erros
    Paciente.AdicionaPaciente("18229744112", "Maria das Luzes", "1988-09-23", 2) # tentando inserir o mesmo CPF pra testar erros
    Paciente.AdicionaPaciente("28229735118", "Marquinhos Lightning", "1998-08-21", 3) # tentando inserir o mesmo CPF pra testar erros
    Paciente.AdicionaPaciente("18229735113", "Mariana Fagundes", "1978-12-21", 4) # tentando inserir o mesmo CPF pra testar erros
    Paciente.AdicionaPaciente("18229735119", "Wilson dos Santos", "2000-05-22", 5) # tentando inserir o mesmo CPF pra testar erros


    # Testes
    # AdicionaTestes(nome)
    Testes.AdicionaTestes("RT-PCR")
    Testes.AdicionaTestes("Sorologia")
    Testes.AdicionaTestes("Testes Rápidos")

    # TestesPacientes
    # TestesPacientes.AdicionaTestesPacientes("2020-11-17", 0, 1, '18229735114')
    # print(TestesPacientes.ListaTestesPacientes())

    # Sintomas # Mudar esse tipo físico ou psico pra gravidade do sintoma
    Sintomas.AdicionaSintomas("Febre", "Fisico")
    Sintomas.AdicionaSintomas("Tosse seca", "Fisico")
    Sintomas.AdicionaSintomas("Cansaço", "Fisico")
    Sintomas.AdicionaSintomas("Perda de olfato", "Fisico")
    Sintomas.AdicionaSintomas("Dor ou pressão no peito", "Físico")

    # SintomasPacientes
    # SintomasPacientes.AdicionaSintomasPacientes("2020-10-17", 1, '18229735114')
    # print(SintomasPacientes.ListaSintomasPacientes())

    # Medicacoes
    Medicacoes.AdicionaMedicacoes("Ozônio")
    Medicacoes.AdicionaMedicacoes("Dexametasona")
    Medicacoes.AdicionaMedicacoes("Remdesivir")
    Medicacoes.AdicionaMedicacoes("Heparina")
    Medicacoes.AdicionaMedicacoes("Corticoides")

    # Medicacoes Pacientes
    # MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-10-17", '50g',1,'18229735114')
    # print(MedicacoesPacientes.ListaMedicacoesPacientes())

    # ProfissionaisSaude
    # AdicionaProfissionaisSaude(cpf, nome, profissao, teveCovid)
    ProfissionaisSaude.AdicionaProfissionaisSaude("18229335112", "Marina Pinho", "Médica", 1)
    ProfissionaisSaude.AdicionaProfissionaisSaude("18221135114", "Larissa Cosa", "Segurança", 2)
    ProfissionaisSaude.AdicionaProfissionaisSaude("18229710115", "Jonas Silva", "Enfermeiro", 3)
    ProfissionaisSaude.AdicionaProfissionaisSaude("18129735317", "Eduardo Pereira", "Médico", 4)
    ProfissionaisSaude.AdicionaProfissionaisSaude("14229735111", "Mariana Garcia", "Médica", 5)

    # ProfTrabalhaHospital
    # ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(1, '18229735115')
    # print(ProfTrabalhaHospital.ListaProfTrabalhaHospital())

    # ProfAtendePaciente
    # ProfAtendePaciente.AdicionaProfAtendePaciente('18229735114', '18229735115')
    # print(ProfAtendePaciente.ListaProfAtendePaciente())


    # Parente
    # AdicionaParente(cpf, nome, dataNascimento, teveContato)
    Parente.AdicionaParente("18229755541", "Matheus Souza", "1990-04-05", 1)
    Parente.AdicionaParente("18229755542", "Maísa da Silva", "1955-04-05", 1)
    Parente.AdicionaParente("18229755543", "Pedro Fagundes", "1979-04-05", 0)
    Parente.AdicionaParente("18229755544", "Carla das Luzes", "1970-04-05", 1)
    Parente.AdicionaParente("18229755545", "Edson dos Santos", "1995-04-05", 0)
    # print(Parente.ListaTodosParentes())

    # ParentePacientes
    # ParentePaciente.AdicionaParentePaciente('18229735114', '18229755545')
    # print(ParentePaciente.ListaParentePaciente())
