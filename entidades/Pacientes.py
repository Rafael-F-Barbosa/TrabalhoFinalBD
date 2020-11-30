import util.OpDb as OpDb

#Cria a Classe Paciente
class Paciente:
    #Lista com todos os atributos de Paciente
    dicio = ['Cpf', 'Nome', 'DataNascimento', 'CodHospital']

    def __init__(self, cpf, nome, dataNascimento, codHospital):
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.codHospital = codHospital

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaTodosPacientes():
        return OpDb.SelecionaTudo('Pacientes')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaPaciente(cpf, nome, dataNascimento, codHospital):
        dicioPaciente = {}
        dicioPaciente['Cpf'] = cpf
        dicioPaciente['Nome'] = nome
        dicioPaciente['DataNascimento'] = dataNascimento
        dicioPaciente['CodHospital'] = codHospital
        OpDb.InsereTudo('Pacientes', dicioPaciente)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaPaciente(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Pacientes', coluna1, valor1, coluna2, valor2)
        