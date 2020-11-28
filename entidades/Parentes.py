import util.OpDb as OpDb


class Parente:
    dicio = ['Cpf', 'Nome', 'DataNascimento', 'TeveContato']

    def __init__(self, cpf, nome, dataNascimento, teveContato):
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.teveContato = teveContato

    def ListaTodosParentes():
        return OpDb.SelecionaTudo('Parentes')

    def AdicionaParente(cpf, nome, dataNascimento, teveContato):
        dicioParente = {}
        dicioParente['Cpf'] = cpf
        dicioParente['Nome'] = nome
        dicioParente['DataNascimento'] = dataNascimento
        dicioParente['TeveContato'] = teveContato
        OpDb.InsereTudo('Parentes', dicioParente)

    def AtualizaParente(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Parentes', coluna1, valor1, coluna2, valor2)