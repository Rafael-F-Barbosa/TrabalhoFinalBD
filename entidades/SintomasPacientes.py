import util.OpDb as OpDb


class SintomasPacientes:
    dicio = ['DataSintoma', 'CodSintoma', 'CpfPaciente']

    def __init__(self, dataSintoma, codSintoma, cpfPaciente):
        self.dataSintoma = dataSintoma
        self.codSintoma = codSintoma
        self.cpfPaciente = cpfPaciente

    def ListaSintomasPacientes():
        return OpDb.SelecionaTudo('SintomasPacientes')

    def AdicionaSintomasPacientes(dataSintoma, codSintoma, cpfPaciente):
        dicioSintomasPacientes = {}
        dicioSintomasPacientes['DataSintoma'] = dataSintoma
        dicioSintomasPacientes['CodSintoma'] = codSintoma
        dicioSintomasPacientes['CpfPaciente'] = cpfPaciente
        OpDb.InsereTudo('SintomasPacientes', dicioSintomasPacientes)

    def AtualizaSintomasPacientes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('SintomasPacientes', coluna1, valor1, coluna2, valor2)