import util.OpDb as OpDb


class ProfAtendePaciente:
    dicio = ['CpfPaciente', 'CpfProfissional']

    def __init__(self, cpfPaciente, cpfProfissional):
        self.cpfPaciente = cpfPaciente
        self.codProfissional = cpfProfissional

    def ListaProfAtendePaciente():
        # Tá errado aqui e na tabela criada também, arrumar depois
        return OpDb.SelecionaTudo('ProfAtendePaciente')

    def AdicionaProfAtendePaciente(cpfPaciente, cpfProfissional):
        dicioProfAtendePaciente = {}
        dicioProfAtendePaciente['CpfPaciente'] = cpfPaciente
        dicioProfAtendePaciente['CpfProfissional'] = cpfProfissional
        OpDb.InsereTudo('ProfAtendePaciente', dicioProfAtendePaciente)

    def AtualizaProfissionalPaciente(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('ProfAtendePaciente', coluna1, valor1, coluna2, valor2)