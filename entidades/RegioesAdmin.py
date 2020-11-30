import util.OpDb as OpDb

#Cria a classe RegioesAdmin
class RegioesAdmin:
    #lista com todos os atributos de RegioesAdmin
    dicio = ['Codigo', 'Nome', 'Populacao']

    def __init__(self, codigo, nome, populacao):
        self.codigo = codigo
        self.nome = nome
        self.populacao = populacao

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaTodasRegioesAdmin():
        return OpDb.SelecionaTudo('RegiaoAdmin')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaRegiaoAdmin(nome, populacao):
        dicioRegiao = {}
        dicioRegiao['Nome'] = nome
        dicioRegiao['Populacao'] = populacao
        OpDb.InsereTudo('RegiaoAdmin', dicioRegiao)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaRegiao(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('RegioesAdmin', coluna1, valor1, coluna2, valor2)