import util.OpDb as OpDb

#cria Classe Acoes
class Acoes:
    #lista com os atirbutos de Acoes
    dicio = ['Codigo', 'Eficiencia', 'Tipo', 'codRegiao']
    def __init__(self, eficiencia, tipo, codRegiao):

        self.codigo = codigo
        self.eficiencia = eficiencia
        self.tipo = tipo
        self.codRegiao = codRegiao

    #Método que lista todos os ítens dessa classe presentes no banco
    def ListaTudoAcoes():
        return OpDb.SelecionaTudo('Acoes')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaAcoes(eficiencia, tipo, codRegiao):
        dicioAcoes = {}
        dicioAcoes['Eficiencia'] = eficiencia
        dicioAcoes['Tipo'] = tipo
        dicioAcoes['codRegiao'] = codRegiao
        OpDb.InsereTudo('Acoes', dicioAcoes)

    #Método que adiciona ítens dessa classe no banco
    def AtualizaAcoes(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Acoes', coluna1, valor1, coluna2, valor2)


