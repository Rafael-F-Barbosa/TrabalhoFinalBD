from entidades.RegioesAdmin import RegioesAdmin
from entidades.SituacaoAtual import SituacaoAtual
from entidades.Acoes import Acoes
from entidades.Hospitais import Hospitais as Hospital
from entidades.Pacientes import Paciente

# RegioesAdmin
# RegioesAdmin.AdicionaRegiaoAdmin('Aguas Claras', 50000)
# print(RegioesAdmin.ListaTodasRegioesAdmin())


# SituacaoAtual
# SituacaoAtual.AdicionaSituacaoAtual('2020-11-11', 10, 45, 45, 5, 8)
# print(SituacaoAtual.ListaTudoSituacaoAtual())

# Acoes
# Acoes.AdicionaAcoes(45, "Distanciamento social", 5)
# print(Acoes.ListaTudoAcoes())


# Acoes
# Hospital.AdicionaHospital("73365456", "HRAN", 45,45,45, 3)
# print(Hospital.ListaTudoHospitais())


# # Pacientes
Paciente.AdicionaPaciente("18229735114", "Reifael", "1998-09-21", 1)
print(Paciente.ListaTodosPacientes())
