import util.OpDb as OpDb

#Cria a classe ProfTrabalhaHospital, que relaciona os profissionais da saúde e os hospitais
class ProfTrabalhaHospital:
    #lista com todos os atrinutos de ProfTrabalhaHospital
    dicio = ['CodHospital', 'CpfProfissional']

    def __init__(self, codHospital, cpfProfissional):
        self.codHospital = codHospital
        self.codProfissional = cpfProfissional

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaProfTrabalhaHospital():
        return OpDb.SelecionaTudo('ProfTabalhaHospital')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaProfTrabalhaHospital(codHospital, cpfProfissional):
        dicioProfTrabalhaHospital = {}
        dicioProfTrabalhaHospital['CodHospital'] = codHospital
        dicioProfTrabalhaHospital['CpfProfissional'] = cpfProfissional
        OpDb.InsereTudo('ProfTabalhaHospital', dicioProfTrabalhaHospital)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaProfissionalHospital(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('ProfTrabalhaHospital', coluna1, valor1, coluna2, valor2)