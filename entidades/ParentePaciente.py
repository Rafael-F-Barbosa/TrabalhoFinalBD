import util.OpDb as OpDb


class ParentePaciente:
    dicio = ['CpfPaciente', 'CpfParente']

    def __init__(self, cpfPaciente, cpfParente):
        self.cpfPaciente = cpfPaciente
        self.cpfParente = cpfParente

    def ListaParentePaciente():
        # Tá errado aqui e na tabela criada também, arrumar depois
        return OpDb.SelecionaTudo('ParentePaciente')

    def AdicionaParentePaciente(cpfPaciente, cpfParente):
        dicioParentePaciente = {}
        dicioParentePaciente['CpfPaciente'] = cpfPaciente
        dicioParentePaciente['CpfParente'] = cpfParente
        OpDb.InsereTudo('ParentePaciente', dicioParentePaciente)

    def AtualizaParentePaciente(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('ParentePaciente', coluna1, valor1, coluna2, valor2)