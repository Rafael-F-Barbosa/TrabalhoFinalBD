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

# RegioesAdmin
# RegioesAdmin.AdicionaRegiaoAdmin('Aguas Claras', 50000)
# print(RegioesAdmin.ListaTodasRegioesAdmin())


# SituacaoAtual
# SituacaoAtual.AdicionaSituacaoAtual('2020-11-11', 10, 45, 45, 5, 1)
# print(SituacaoAtual.ListaTudoSituacaoAtual())

# Acoes
# Acoes.AdicionaAcoes(45, "Auxilio", 1)
# print(Acoes.ListaTudoAcoes())


# Hospitais
# Hospital.AdicionaHospital("73365456", "HRAN", 45,45,45, 1)
# print(Hospital.ListaTudoHospitais())


# Pacientes
# Paciente.AdicionaPaciente("18229735114", "Reifael", "1998-09-21", 1) # tentando inserir o mesmo CPF pra testar erros
# print(Paciente.ListaTodosPacientes())

# Testes
# Testes.AdicionaTestes("PCR")
# print(Testes.ListaTestes())

# TestesPacientes
TestesPacientes.AdicionaTestesPacientes("2020-11-17", 0, 1, '18229735114')
print(TestesPacientes.ListaTestesPacientes())

# Sintomas
Sintomas.AdicionaSintomas("Febre", "Fisico")
print(Sintomas.ListaSintomas())

# SintomasPacientes
SintomasPacientes.AdicionaSintomasPacientes("2020-10-17", 1, '18229735114')
print(SintomasPacientes.ListaSintomasPacientes())

# Medicacoes
Medicacoes.AdicionaMedicacoes("Ozônio")
print(Medicacoes.ListaMedicacoes())

# Medicacoes Pacientes
MedicacoesPacientes.AdicionaMedicacoesPacientes("2020-10-17", '50g',1,'18229735114')
print(MedicacoesPacientes.ListaMedicacoesPacientes())

# ProfissionaisSaude
ProfissionaisSaude.AdicionaProfissionaisSaude("18229735115", "Nina Pinho", "Médica", 0) 
print(ProfissionaisSaude.ListaProfissionaisSaude())

# ProfTrabalhaHospital
ProfTrabalhaHospital.AdicionaProfTrabalhaHospital(1, '18229735115')
print(ProfTrabalhaHospital.ListaProfTrabalhaHospital())

# ProfAtendePaciente
ProfAtendePaciente.AdicionaProfAtendePaciente('18229735114', '18229735115')
print(ProfAtendePaciente.ListaProfAtendePaciente())


# Parente
Parente.AdicionaParente("18229755545", "Nina", "1999-04-05", 0) 
print(Parente.ListaTodosParentes())

# ParentePacientes
ParentePaciente.AdicionaParentePaciente('18229735114', '18229755545')
print(ParentePaciente.ListaParentePaciente())

# --------------------

# Estou triste com isso, mas acho que é melhor não fazer interface gráfica
# por enquanto, vai dar muito trabalho, principalmente pq a gente não  
# manja disso em python

# Aí o que eu estava pensando era algo assim:
# A gente roda o programa e aparece um menuzinho com as opções

# aí nisso vai ter as opções pra digitar no terminal: 
# 1 - Vizualizar dados
# Nesse você vai poder navegar e obter dados sobre a pandemia, aí vai 
# entrar umas consultas personalizadas que a gente pode ir pensando em
# ao longo do trabalho, por exemplo:
# - Listar hospitais mostrando só os que tem vagas de uti
# - Ver pacientes em um hospital, para cada paciente ver com quem ele 
# teve contato.

# 2 - Adicionar dados
# Aí nesse de adicionar vai poder adicionar simplesmente tudo, 
# como é no terminal acho bom separar em 2 grupos uma mais geral, 
# e um focado nos pacientes

# Separar em grupos == fazer menus dentro de menus pra ficar melhorzinho



