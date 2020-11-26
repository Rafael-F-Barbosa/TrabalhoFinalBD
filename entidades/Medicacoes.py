import util.OpDb as OpDb


class Medicacoes:
    dicio = ['Codigo', 'Nome']

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def ListaMedicacoes():
        return OpDb.SelecionaTudo('Medicacoes')

    def AdicionaMedicacoes(nome):
        dicioMedicacoes = {}
        dicioMedicacoes['Nome'] = nome
        OpDb.InsereTudo('Medicacoes', dicioMedicacoes)

    def AtualizaMedicacao(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Medicacoes', coluna1, valor1, coluna2, valor2)