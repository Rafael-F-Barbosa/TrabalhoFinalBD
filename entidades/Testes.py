import util.OpDb as OpDb

class Testes:
    def __init__(self, Codigo, Nome):
        self.Codigo = Codigo
        self.Nome = Nome

    def ListaTestes():
        return OpDb.SelecionaTudo('Testes')

    def AdicionaTestes(nome):
        dicioRegiao = {}
        dicioRegiao['Nome'] = nome
        OpDb.InsereTudo('Testes', dicioRegiao)
