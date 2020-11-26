import util.OpDb as OpDb

class RegioesAdmin:
    dicio = ['Codigo', 'Nome', 'Populacao']

    def __init__(self, codigo, nome, populacao):
        self.codigo = codigo
        self.nome = nome
        self.populacao = populacao
    def ListaTodasRegioesAdmin():
        return OpDb.SelecionaTudo('RegiaoAdmin')

    def AdicionaRegiaoAdmin(nome, populacao):
        dicioRegiao = {}
        dicioRegiao['Nome'] = nome
        dicioRegiao['Populacao'] = populacao
        OpDb.InsereTudo('RegiaoAdmin', dicioRegiao)

    def AtualizaRegiao(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('RegioesAdmin', coluna1, valor1, coluna2, valor2)