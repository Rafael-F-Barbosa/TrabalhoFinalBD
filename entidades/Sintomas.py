import util.OpDb as OpDb


class Sintomas:
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
