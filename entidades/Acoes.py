import util.OpDb as OpDb

class Acoes:
    def __init__(self, eficiencia, tipo, codRegiao):
        self.codigo = codigo
        self.eficiencia = eficiencia
        self.tipo = tipo
        self.codRegiao = codRegiao

    def ListaTudoAcoes():
        return OpDb.SelecionaTudo('Acoes')

    def AdicionaAcoes(eficiencia, tipo, codRegiao):
        dicioAcoes = {}
        dicioAcoes['Eficiencia'] = eficiencia
        dicioAcoes['Tipo'] = tipo
        dicioAcoes['codRegiao'] = codRegiao
        OpDb.InsereTudo('Acoes', dicioAcoes)


