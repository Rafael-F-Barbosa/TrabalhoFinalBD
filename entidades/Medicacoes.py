import util.OpDb as OpDb


class Medicacoes:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def ListaMedicacoes():
        return OpDb.SelecionaTudo('Medicacoes')

    def AdicionaMedicacoes(nome):
        dicioMedicacoes = {}
        dicioMedicacoes['Nome'] = nome
        OpDb.InsereTudo('Medicacoes', dicioMedicacoes)
