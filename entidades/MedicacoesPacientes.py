import util.OpDb as OpDb


class MedicacoesPacientes:
    def __init__(self, dataMed, dosagem, codMedicacao, cpfPaciente):
        self.dataMed = dataMed
        self.dosagem = dosagem
        self.codMedicacao = codMedicacao
        self.cpfPaciente = cpfPaciente

    def ListaMedicacoesPacientes():
        return OpDb.SelecionaTudo('MedicacoesPacientes')

    def AdicionaMedicacoesPacientes(dataMed, Dosagem, codMedicacao, cpfPaciente):
        dicioRegiao = {}
        dicioRegiao['DataMed'] = dataMed
        dicioRegiao['Dosagem'] = Dosagem
        dicioRegiao['CodMedicacao'] = codMedicacao
        dicioRegiao['CpfPaciente'] = cpfPaciente
        OpDb.InsereTudo('MedicacoesPacientes', dicioRegiao)
