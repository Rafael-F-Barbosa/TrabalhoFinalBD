import util.OpDb as OpDb

class Acoes:
    dicio = ['Codigo', 'Eficiencia', 'Tipo', 'codRegiao']
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

    def AtualizaAcoes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Acoes', coluna1, valor1, coluna2, valor2)


