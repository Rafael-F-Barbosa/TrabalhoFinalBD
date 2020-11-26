import util.OpDb as OpDb

class Testes:
    dicio = ['codigo', 'Nome']

    def __init__(self, Codigo, Nome):
        self.Codigo = Codigo
        self.Nome = Nome

    def ListaTestes():
        return OpDb.SelecionaTudo('Testes')

    def AdicionaTestes(nome):
        dicioRegiao = {}
        dicioRegiao['Nome'] = nome
        OpDb.InsereTudo('Testes', dicioRegiao)

    def AtualizaTestes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Testes', coluna1, valor1, coluna2, valor2)