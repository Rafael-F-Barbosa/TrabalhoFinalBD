import util.OpDb as OpDb

#Cria classe TestesPacientes, que relaciona os pacientes e os testes
class TestesPacientes:
    #Lista com todos os atributos de TestesPacientes
    dicio = ['DataTeste', 'Resultado', 'CodTeste', 'CpfPaciente']

    def __init__(self, dataTestes, resultados, codTeste, cpfPaciente):
        self.dataTestes = dataTestes
        self.resultados = resultados
        self.codTeste = codTeste
        self.cpfPaciente = cpfPaciente

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaTestesPacientes():
        return OpDb.SelecionaTudo('TestesPacientes')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaTestesPacientes(dataTestes, resultados, codTeste, cpfPaciente):
        dicioRegiao = {}
        dicioRegiao['DataTeste'] = dataTestes
        dicioRegiao['Resultado'] = resultados
        dicioRegiao['CodTeste'] = codTeste
        dicioRegiao['CpfPaciente'] = cpfPaciente
        OpDb.InsereTudo('TestesPacientes', dicioRegiao)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaTestesPacientes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('TestesPacientes', coluna1, valor1, coluna2, valor2)