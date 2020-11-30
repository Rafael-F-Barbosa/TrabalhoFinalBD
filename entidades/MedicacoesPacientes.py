import util.OpDb as OpDb

#Cria classe MedicacoesPacientes, que relaciona os pacientes e as medicações
class MedicacoesPacientes:
    #lista com todos os atributos de MedicacoesPacientes
    dicio = ['DataMed', 'Dosagem', 'codMEdicacao', 'CpfPaciente']

    def __init__(self, dataMed, dosagem, codMedicacao, cpfPaciente):
        self.dataMed = dataMed
        self.dosagem = dosagem
        self.codMedicacao = codMedicacao
        self.cpfPaciente = cpfPaciente

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaMedicacoesPacientes():
        return OpDb.SelecionaTudo('MedicacoesPacientes')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaMedicacoesPacientes(dataMed, Dosagem, codMedicacao, cpfPaciente):
        dicioRegiao = {}
        dicioRegiao['DataMed'] = dataMed
        dicioRegiao['Dosagem'] = Dosagem
        dicioRegiao['CodMedicacao'] = codMedicacao
        dicioRegiao['CpfPaciente'] = cpfPaciente
        OpDb.InsereTudo('MedicacoesPacientes', dicioRegiao)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaMedicacoesPacientes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('MedicacoesPacientes', coluna1, valor1, coluna2, valor2)