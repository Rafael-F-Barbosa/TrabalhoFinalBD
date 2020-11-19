import util.OpDb as OpDb


class ProfTrabalhaHospital:
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
