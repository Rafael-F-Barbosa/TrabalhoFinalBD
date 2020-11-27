import util.OpDb as OpDb

class TestesPacientes:
    dicio = ['DataTeste', 'Resultado', 'CodTeste', 'CpfPaciente']

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

    def AtualizaTestesPacientes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('TestesPacientes', coluna1, valor1, coluna2, valor2)