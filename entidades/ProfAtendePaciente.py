import util.OpDb as OpDb

#Cria a classe ProfAtendePaciente, que relaciona os profissionais da saúde e os pacientes
class ProfAtendePaciente:
    #Lista com todos os atributos de ProfAtendePaciente
    dicio = ['CpfPaciente', 'CpfProfissional']

    def __init__(self, cpfPaciente, cpfProfissional):
        self.cpfPaciente = cpfPaciente
        self.codProfissional = cpfProfissional

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaProfAtendePaciente():
        return OpDb.SelecionaTudo('ProfAtendePaciente')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaProfAtendePaciente(cpfPaciente, cpfProfissional):
        dicioProfAtendePaciente = {}
        dicioProfAtendePaciente['CpfPaciente'] = cpfPaciente
        dicioProfAtendePaciente['CpfProfissional'] = cpfProfissional
        OpDb.InsereTudo('ProfAtendePaciente', dicioProfAtendePaciente)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaProfissionalPaciente(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('ProfAtendePaciente', coluna1, valor1, coluna2, valor2)