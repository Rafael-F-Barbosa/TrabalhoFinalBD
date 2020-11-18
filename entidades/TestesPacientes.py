import util.OpDb as OpDb

class TestesPacientes:
    def __init__(self, dataTestes, resultados, codTeste, cpfPaciente):
        self.dataTestes = dataTestes
        self.resultados = resultados
        self.codTeste = codTeste
        self.cpfPaciente = cpfPaciente

    def ListaTestesPacientes():
        return OpDb.SelecionaTudo('TestesPacientes')

    def AdicionaTestesPacientes(dataTestes, resultados, codTeste, cpfPaciente):
        dicioRegiao = {}
        dicioRegiao['DataTeste'] = dataTestes
        dicioRegiao['Resultado'] = resultados
        dicioRegiao['CodTeste'] = codTeste
        dicioRegiao['CpfPaciente'] = cpfPaciente
        OpDb.InsereTudo('TestesPacientes', dicioRegiao)
