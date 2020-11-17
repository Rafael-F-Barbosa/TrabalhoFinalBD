import util.OpDb as OpDb

class SituacaoAtual:
    def __init__(self, dataSituacao, casosLeves, casosGraves, mortes, recuperados, codRegiao):
        self.dataSituacao = dataSituacao
        self.casosLeves = casosLeves
        self.casosGraves = casosGraves
        self.mortes = mortes
        self.recuperados = recuperados
        self.codRegiao = codRegiao

    def ListaTudoSituacaoAtual():
        return OpDb.SelecionaTudo('SituacaoAtual')

    def AdicionaSituacaoAtual(dataSituacao, casosLeves, casosGraves, mortes, recuperados, codRegiao):
        dicioRegiao = {}
        dicioRegiao['DataSituacao'] = dataSituacao
        dicioRegiao['CasosLeves'] = casosLeves
        dicioRegiao['CasosGraves'] = casosGraves
        dicioRegiao['Mortes'] = mortes
        dicioRegiao['Recuperados'] = recuperados
        dicioRegiao['CodRegiao'] = codRegiao
        OpDb.InsereTudo('SituacaoAtual', dicioRegiao)
