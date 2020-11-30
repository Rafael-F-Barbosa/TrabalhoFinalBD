import util.OpDb as OpDb

#Cria a Calsse Medicações
class Medicacoes:
    #Lista com todos os atributos dessa classe
    dicio = ['Codigo', 'Nome']

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    #Método que lista todos os ítens dessa classe presentes no banco
    def ListaMedicacoes():
        return OpDb.SelecionaTudo('Medicacoes')

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaMedicacoes(nome):
        dicioMedicacoes = {}
        dicioMedicacoes['Nome'] = nome
        OpDb.InsereTudo('Medicacoes', dicioMedicacoes)

    #Método que atualiza um ítem dessa classe no banco
    def AtualizaMedicacao(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Medicacoes', coluna1, valor1, coluna2, valor2)