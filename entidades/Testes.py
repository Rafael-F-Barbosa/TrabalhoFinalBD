import util.OpDb as OpDb

#Cria a Classe Testes
class Testes:
    #Lista com todos os atributos de Testes
    dicio = ['codigo', 'Nome']

    def __init__(self, Codigo, Nome):
        self.Codigo = Codigo
        self.Nome = Nome

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaTestes():
        return OpDb.SelecionaTudo('Testes')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaTestes(nome):
        dicioRegiao = {}
        dicioRegiao['Nome'] = nome
        OpDb.InsereTudo('Testes', dicioRegiao)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaTestes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Testes', coluna1, valor1, coluna2, valor2)