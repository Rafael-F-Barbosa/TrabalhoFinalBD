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

from views.telas import main







# -----------------------------------------------------------------------

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

# -----------------------------------------------------------------------

# MAIN

# RegioesAdmin.AdicionaRegiaoAdmin('Aguas Claras', 50000)
print(RegioesAdmin.ListaTodasRegioesAdmin())
a = input('')
main()



