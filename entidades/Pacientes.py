import util.OpDb as OpDb

class Paciente:

    dicio = ['Cpf', 'Nome', 'DataNascimento', 'CodHospital']

    def __init__(self, cpf, nome, dataNascimento, codHospital):
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.codHospital = codHospital

    def ListaTodosPacientes():
        return OpDb.SelecionaTudo('Pacientes')

    def AdicionaPaciente(cpf, nome, dataNascimento, codHospital):
        dicioPaciente = {}
        dicioPaciente['Cpf'] = cpf
        dicioPaciente['Nome'] = nome
        dicioPaciente['DataNascimento'] = dataNascimento
        dicioPaciente['CodHospital'] = codHospital
        OpDb.InsereTudo('Pacientes', dicioPaciente)

    def AtualizaPaciente(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Paciente', coluna1, valor1, coluna2, valor2)