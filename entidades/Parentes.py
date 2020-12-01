import util.OpDb as OpDb

#Cria a Classe Parente
class Parente:
    #Lista com todos os atributos de Parente
    dicio = ['Cpf', 'Nome', 'DataNascimento', 'TeveContato']

    def __init__(self, cpf, nome, dataNascimento, teveContato):
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.teveContato = teveContato

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaTodosParentes():
        lista = OpDb.SelecionaTudo('Parentes')
        lista_editada = []
        for x in range(len(lista)):
            lista_editada.append(list(lista[x]))
            if (int(lista_editada[x][3]) == 0):
                lista_editada[x][3] = 'Não'
            else:
                lista_editada[x][3] = 'Sim'
        return lista_editada

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaParente(cpf, nome, dataNascimento, teveContato):
        dicioParente = {}
        dicioParente['Cpf'] = cpf
        dicioParente['Nome'] = nome
        dicioParente['DataNascimento'] = dataNascimento
        dicioParente['TeveContato'] = teveContato
        OpDb.InsereTudo('Parentes', dicioParente)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaParente(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Parentes', coluna1, valor1, coluna2, valor2)
