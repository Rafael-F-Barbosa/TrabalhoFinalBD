import util.OpDb as OpDb

class Paciente:
    def __init__(self, cpf, nome, dataNascimento, codHospital):
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.codHospital = codHospital

    def ListaTodosPacientes():
        return OpDb.SelecionaTudo('Pacientes')

    def AdicionaPaciente(cpf, nome, dataNascimento, codHospital):
        dicioRegiao = {}
        dicioRegiao['Cpf'] = cpf
        dicioRegiao['Nome'] = nome
        dicioRegiao['DataNascimento'] = dataNascimento
        dicioRegiao['CodHospital'] = codHospital
        OpDb.InsereTudo('Pacientes', dicioRegiao)