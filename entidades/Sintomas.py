import util.OpDb as OpDb


class Sintomas:
    dicio = ['Codigo', 'Nome', 'Tipo']

    def __init__(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo

    def ListaSintomas():
        return OpDb.SelecionaTudo('Sintomas')

    def AdicionaSintomas(nome, tipo):
        dicioSintomas = {}
        dicioSintomas['Nome'] = nome
        dicioSintomas['Tipo'] = tipo
        OpDb.InsereTudo('Sintomas', dicioSintomas)

    def AtualizaSintomas(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Sintomas', coluna1, valor1, coluna2, valor2)