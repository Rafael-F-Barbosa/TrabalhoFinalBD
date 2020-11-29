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
from aux import preenche_banco_inicialmente

# ------------------------------------------------------------------------- 

# Coisas para fazer no trabalho 
# - Dentro de ver informações informações personalizadas
#   - Rastrear contatos(Implementado)
#   - View(Ver hospitais que estão cheios)
#   - Ver informações do DF geral
#   - Ver um relatório geral de 1 Paciente(pelo CPF)
# - Colocar IF em alguma procedure ou view 
# Coisas do Relatório 
# - Introdução 
# - 5 Consultas envolvendo 3 tabelas
# - 5 Avaliações das formas normais
# - ????? A construção da camada de persistência. Enviar os códigos fontes e um diagrama apresentando como a interface gráfica do programa acessa a camada de persistência. ??????? 

# preenche_banco_inicialmente()
main()




