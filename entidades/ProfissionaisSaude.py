import util.OpDb as OpDb

class ProfissionaisSaude:
    dicio = ['Cpf', 'Nome', 'Profissao', 'TeveCovid']

    def __init__(self, cpf, nome, profissao, teveCovid):
        self.cpf = cpf
        self.nome = nome
        self.profissao = profissao
        self.teveCovid = teveCovid

    def ListaProfissionaisSaude():
        return OpDb.SelecionaTudo('ProfissionaisSaude')

    def AdicionaProfissionaisSaude(cpf, nome, profissao, teveCovid):
        dicioProfissionaisSaude = {}
        dicioProfissionaisSaude['CPF'] = cpf
        dicioProfissionaisSaude['Nome'] = nome
        dicioProfissionaisSaude['Profissao'] = profissao
        dicioProfissionaisSaude['TeveCovid'] = teveCovid
        OpDb.InsereTudo('ProfissionaisSaude', dicioProfissionaisSaude)

    def AtualizaProfissional(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('ProfissionaisSaude', coluna1, valor1, coluna2, valor2)