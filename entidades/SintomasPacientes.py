import util.OpDb as OpDb

#Cria classe SintomasPacientes, que relaciona os pacientes e os sintomas
class SintomasPacientes:
    #Lista com todos os atrinutos de SintomasPacientes
    dicio = ['DataSintoma', 'CodSintoma', 'CpfPaciente']

    def __init__(self, dataSintoma, codSintoma, cpfPaciente):
        self.dataSintoma = dataSintoma
        self.codSintoma = codSintoma
        self.cpfPaciente = cpfPaciente

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaSintomasPacientes():
        return OpDb.SelecionaTudo('SintomasPacientes')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaSintomasPacientes(dataSintoma, codSintoma, cpfPaciente):
        dicioSintomasPacientes = {}
        dicioSintomasPacientes['DataSintoma'] = dataSintoma
        dicioSintomasPacientes['CodSintoma'] = codSintoma
        dicioSintomasPacientes['CpfPaciente'] = cpfPaciente
        OpDb.InsereTudo('SintomasPacientes', dicioSintomasPacientes)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaSintomasPacientes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('SintomasPacientes', coluna1, valor1, coluna2, valor2)