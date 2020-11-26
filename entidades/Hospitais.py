import util.OpDb as OpDb


class Hospitais:

    dicio = ['Codigo', 'Nome', 'Cep', 'QtdLeitosDisponiveis', 'QtdLeitosOcupados', 'NumeroPessoasComCovid', 'CodRegiao']

    def __init__(self, nome, cep, qtdLeitosDisponiveis, qtdLeitosOcupados, numeroPessoasComCovid, codRegiao):
        self.nome = nome
        self.cep = cep
        self.qtdLeitosDisponiveis = qtdLeitosDisponiveis
        self.qtdLeitosOcupados = qtdLeitosOcupados
        self.numeroPessoasComCovid = numeroPessoasComCovid
        self.codRegiao = codRegiao

    def ListaTudoHospitais():
        return OpDb.SelecionaTudo('Hospitais')

    def AdicionaHospital(nome, cep, qtdLeitosDisponiveis, qtdLeitosOcupados, numeroPessoasComCovid, codRegiao):
        dicioHospital = {}
        dicioHospital['Nome'] = nome
        dicioHospital['Cep'] = cep
        dicioHospital['QtdLeitosDisponiveis'] = qtdLeitosDisponiveis
        dicioHospital['QtdLeitosOcupados'] = qtdLeitosOcupados
        dicioHospital['NumeroPessoasComCovid'] = numeroPessoasComCovid
        dicioHospital['CodRegiao'] = codRegiao
        OpDb.InsereTudo('Hospitais', dicioHospital)

    def AtualizaHospital(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('Hospitais', coluna1, valor1, coluna2, valor2)