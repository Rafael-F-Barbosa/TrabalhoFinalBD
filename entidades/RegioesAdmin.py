import util.OpDb as OpDb

class RegioesAdmin:
    def __init__(self, codigo, nome, populacao):
        self.codigo = codigo
        self.nome = nome
        self.populacao = populacao
    def ListaTodasRegioesAdmin():
        return OpDb.SelecionaTudo('RegiaoAdmin')

    def AdicionaRegiaoAdmin(nome, populacao):
        dicioRegiao = {}
        dicioRegiao['nome'] = nome
        dicioRegiao['populacao'] = populacao
        OpDb.InsereTudo('RegiaoAdmin', dicioRegiao)

