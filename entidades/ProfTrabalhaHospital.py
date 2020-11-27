import util.OpDb as OpDb


class ProfTrabalhaHospital:
    dicio = ['CodHospital', 'CpfProfissional']

    def __init__(self, codHospital, cpfProfissional):
        self.codHospital = codHospital
        self.codProfissional = cpfProfissional

    def ListaProfTrabalhaHospital():
        return OpDb.SelecionaTudo('ProfTabalhaHospital') # Tá errado aqui e na tabela criada também, arrumar depois 

    def AdicionaProfTrabalhaHospital(codHospital, cpfProfissional):
        dicioProfTrabalhaHospital = {}
        dicioProfTrabalhaHospital['CodHospital'] = codHospital
        dicioProfTrabalhaHospital['CpfProfissional'] = cpfProfissional
        OpDb.InsereTudo('ProfTabalhaHospital', dicioProfTrabalhaHospital)

    def AtualizaProfissionalHospital(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('ProfTrabalhaHospital', coluna1, valor1, coluna2, valor2)