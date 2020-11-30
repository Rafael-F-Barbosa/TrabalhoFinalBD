import util.OpDb as OpDb

#Cria classe ParentePaciente, que relaciona os parentes e os pacientes
class ParentePaciente:
    #lista com todos os atributos de ParentePaciente
    dicio = ['CpfPaciente', 'CpfParente']

    def __init__(self, cpfPaciente, cpfParente):
        self.cpfPaciente = cpfPaciente
        self.cpfParente = cpfParente

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaParentePaciente():
        return OpDb.SelecionaTudo('ParentePaciente')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaParentePaciente(cpfPaciente, cpfParente):
        dicioParentePaciente = {}
        dicioParentePaciente['CpfPaciente'] = cpfPaciente
        dicioParentePaciente['CpfParente'] = cpfParente
        OpDb.InsereTudo('ParentePaciente', dicioParentePaciente)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaParentePaciente(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('ParentePaciente', coluna1, valor1, coluna2, valor2)