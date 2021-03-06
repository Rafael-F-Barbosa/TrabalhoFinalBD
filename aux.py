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
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-25', 100, 45, 245, 5, 4)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-12', 2000, 35, 445, 5, 4)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-26', 50, 15, 465, 5, 6)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-25', 155, 5, 415, 5, 5)

    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 105, 30, 145, 10, 2)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 10, 145, 450, 15, 1)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 150, 535, 445, 5, 3)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 105, 105, 200, 4, 4)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 140, 45, 307, 20, 5)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 2000, 35, 445, 25, 6)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 50, 15, 465, 50, 7)
    SituacaoAtual.AdicionaSituacaoAtual('2020-11-29', 155, 52, 415, 55, 8)

     

    # Acoes # Se pá não faz sentido desse jeito que tá relacionado preferia que tivesse um código na região que executa a ação
    # AdicionaAcoes(eficiencia, tipo, codRegiao) 
    Acoes.AdicionaAcoes(5, "Fechamento de comércios", 4)
    Acoes.AdicionaAcoes(4, "Auxílio alimentação", 5)
    Acoes.AdicionaAcoes(5, "Testagem em massa", 4)
    Acoes.AdicionaAcoes(3, "Campanhas de conscientização", 3)
    Acoes.AdicionaAcoes(4, "Rastreamento de contatos", 2)


    # Hospitais
    # AdicionaHospital(nome, cep, qtdLeitosDisponiveis, qtdLeitosOcupados, numeroPessoasComCovid, codRegiao)
    Hospital.AdicionaHospital("HRAN", "73365456", 10, 20, 12, 4)
    Hospital.AdicionaHospital("HRP", "73365457", 20, 22, 27, 5)
    Hospital.AdicionaHospital("Hospital de Base", "73365458", 45, 50, 45, 4)
    Hospital.AdicionaHospital("HRT", "73365459", 55, 30, 60, 3)
    Hospital.AdicionaHospital("HRG", "73365433", 45, 45, 15, 8)
    Hospital.AdicionaHospital("HUB", "73365459", 0, 60 , 25, 4)
    Hospital.AdicionaHospital("Santa Helena", "73365433", 0, 45, 35, 4)

    # Pacientes
    # AdicionaPaciente(cpf, nome, dataNascimento, codHospital)
    Paciente.AdicionaPaciente("18229735114", "Joãozinho da Silva", "1993-02-21", 1) 
    Paciente.AdicionaPaciente("18229744112", "Maria das Luzes", "1988-09-23", 2) 
    Paciente.AdicionaPaciente("28229735118", "Marquinhos Lightning", "1998-08-21", 3) 
    Paciente.AdicionaPaciente("18229735113", "Mariana Fagundes", "1978-12-21", 4) 
    Paciente.AdicionaPaciente("18229735119", "Wilson dos Santos", "2000-05-22", 5) 
    Paciente.AdicionaPaciente("18229735111", "Juliana Freitas", "1950-12-21", 4) 
    Paciente.AdicionaPaciente("18229735122", "Daniel dos Santos", "1942-07-23", 2) 


    # Testes
    # AdicionaTestes(nome)
    Testes.AdicionaTestes("RT-PCR")
    Testes.AdicionaTestes("Sorologia")
    Testes.AdicionaTestes("Testes Rápidos")
    Testes.AdicionaTestes("Raio X - Pulmão")
    Testes.AdicionaTestes("Hemograma")

    # TestesPacientes
    # AdicionaTestesPacientes(dataTestes, resultados, codTeste, cpfPaciente)
    TestesPacientes.AdicionaTestesPacientes("2020-11-17", 1, 1, '18229735114')
    TestesPacientes.AdicionaTestesPacientes("2020-10-19", 1, 2, '18229744112')
    TestesPacientes.AdicionaTestesPacientes("2020-11-12", 1, 3, '28229735118')
    TestesPacientes.AdicionaTestesPacientes("2020-10-15", 1, 2, '18229735113')
    TestesPacientes.AdicionaTestesPacientes("2020-11-14", 1, 3, '18229735119')
    TestesPacientes.AdicionaTestesPacientes("2020-11-24", 0, 5, '18229735114')
    TestesPacientes.AdicionaTestesPacientes("2020-10-17", 0, 1, '18229735114')

    # Sintomas 
    Sintomas.AdicionaSintomas("Febre", "Físico")
    Sintomas.AdicionaSintomas("Tosse seca", "Físico")
    Sintomas.AdicionaSintomas("Cansaço", "Físico")
    Sintomas.AdicionaSintomas("Perda de olfato", "Físico")
    Sintomas.AdicionaSintomas("Dor ou pressão no peito", "Físico")

    # SintomasPacientes
    # AdicionaSintomasPacientes(dataSintoma, codSintoma, cpfPaciente)
    SintomasPacientes.AdicionaSintomasPacientes("2020-10-17", 1, '18229735114')
    SintomasPacientes.AdicionaSintomasPacientes("2020-10-18", 2, '18229744112')
    SintomasPacientes.AdicionaSintomasPacientes("2020-10-19", 3, '28229735118')
    SintomasPacientes.AdicionaSintomasPacientes("2020-10-15", 4, '18229735113')
    SintomasPacientes.AdicionaSintomasPacientes("2020-10-14", 2, '18229735119')
    SintomasPacientes.AdicionaSintomasPacientes("2020-11-11", 1, '18229735114')
    SintomasPacientes.AdicionaSintomasPacientes("2020-11-20", 5, '18229735114')


    # Medicacoes
    Medicacoes.AdicionaMedicacoes("Ozônio")
    Medicacoes.AdicionaMedicacoes("Dexametasona")
    Medicacoes.AdicionaMedicacoes("Remdesivir")
    Medicacoes.AdicionaMedicacoes("Heparina")
    Medicacoes.AdicionaMedicacoes("Corticoides")

    # Medicacoes Pacientes
    # AdicionaMedicacoesPacientes(dataMed, Dosagem, codMedicacao, cpfPaciente)
    MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-10-17", '50g',1,'18229735114')
    MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-10-27", '10 gotas',2,'18229735114')
    MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-11-22", '3 comprimidos',3,'18229735114')
    MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-10-18", '75g',4,'18229744112')
    MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-10-19", '100g',2,'28229735118')
    MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-10-20", '10 gotas',2,'18229735113')
    MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-10-02", '50g',3,'18229735119')


    # ProfissionaisSaude
    # AdicionaProfissionaisSaude(cpf, nome, profissao, teveCovid)
    ProfissionaisSaude.AdicionaProfissionaisSaude("18229335112", "Marina Pinho", "Médica", 1)
    ProfissionaisSaude.AdicionaProfissionaisSaude("18221135114", "Larissa Cosa", "Segurança", 0)
    ProfissionaisSaude.AdicionaProfissionaisSaude("18229710115", "Jonas Silva", "Enfermeiro", 0)
    ProfissionaisSaude.AdicionaProfissionaisSaude("18129735317", "Eduardo Pereira", "Médico", 1)
    ProfissionaisSaude.AdicionaProfissionaisSaude("14229735111", "Mariana Garcia", "Médica", 1)

    # ProfTrabalhaHospital
    # AdicionaProfTrabalhaHospital(codHospital, cpfProfissional)
    ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(1, '18229335112')
    ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(2, '18221135114')
    ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(3, '18229710115')
    ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(4, '18129735317')
    ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(5, '14229735111')

    # ProfAtendePaciente
    # AdicionaProfAtendePaciente(cpfPaciente, cpfProfissional)
    ProfAtendePaciente.AdicionaProfAtendePaciente('18229735114', '18229335112')
    ProfAtendePaciente.AdicionaProfAtendePaciente('18229735114', '18229710115')
    ProfAtendePaciente.AdicionaProfAtendePaciente('18229744112', '18221135114')
    ProfAtendePaciente.AdicionaProfAtendePaciente('28229735118', '18229710115')
    ProfAtendePaciente.AdicionaProfAtendePaciente('18229735113', '18129735317')
    ProfAtendePaciente.AdicionaProfAtendePaciente('18229735119', '14229735111')


    # Parente
    # AdicionaParente(cpf, nome, dataNascimento, teveContato)
    Parente.AdicionaParente("18229755541", "Matheus Souza", "1990-04-05", 1)
    Parente.AdicionaParente("18229755542", "Maísa da Silva", "1955-04-05", 1)
    Parente.AdicionaParente("18229755543", "Pedro Fagundes", "1979-04-05", 0)
    Parente.AdicionaParente("18229755544", "Carla das Luzes", "1970-04-05", 1)
    Parente.AdicionaParente("18229755545", "Edson dos Santos", "1995-04-05", 0)

    # ParentePacientes
    # AdicionaParentePaciente(cpfPaciente, cpfParente)
    ParentePaciente.AdicionaParentePaciente('28229735118', '18229755541')
    ParentePaciente.AdicionaParentePaciente('18229735113', '18229755542')
    ParentePaciente.AdicionaParentePaciente('18229744112', '18229755543')
    ParentePaciente.AdicionaParentePaciente('18229735119', '18229755544')
    ParentePaciente.AdicionaParentePaciente('18229735114', '18229755545')
    ParentePaciente.AdicionaParentePaciente('18229735114', '18229755544')
