import util.OpDb as OpDb


class SintomasPacientes:
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
