import util.OpDb as OpDb

#Cria a Classe sintomas
class Sintomas:
    #Lista com todos os atrinutos de sintomas
    dicio = ['Codigo', 'Nome', 'Tipo']

    def __init__(self, codigo, nome, tipo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaSintomas():
        return OpDb.SelecionaTudo('Sintomas')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaSintomas(nome, tipo):
        dicioSintomas = {}
        dicioSintomas['Nome'] = nome
        dicioSintomas['Tipo'] = tipo
        OpDb.InsereTudo('Sintomas', dicioSintomas)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaSintomas(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Sintomas', coluna1, valor1, coluna2, valor2)