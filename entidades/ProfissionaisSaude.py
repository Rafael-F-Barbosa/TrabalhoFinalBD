import util.OpDb as OpDb

#Cria Classe ProfissionaisSaude
class ProfissionaisSaude:
    #Lista com todos os atributos de ProfissionaisSaude
    dicio = ['Cpf', 'Nome', 'Profissao', 'TeveCovid']

    def __init__(self, cpf, nome, profissao, teveCovid):
        self.cpf = cpf
        self.nome = nome
        self.profissao = profissao
        self.teveCovid = teveCovid

    #Métodos que lista todos os ítens dessa classe presentes no banco
    def ListaProfissionaisSaude():
        lista = OpDb.SelecionaTudo('ProfissionaisSaude')
        lista_editada = []
        for x in range(len(lista)):
            lista_editada.append(list(lista[x]))
            if (int(lista_editada[x][3]) == 0):
                lista_editada[x][3] = 'Não'
            else:
                lista_editada[x][3] = 'Sim'

        return lista_editada

    #Método que adiciona um ítem dessa classe ao banco
    def AdicionaProfissionaisSaude(cpf, nome, profissao, teveCovid):
        dicioProfissionaisSaude = {}
        dicioProfissionaisSaude['CPF'] = cpf
        dicioProfissionaisSaude['Nome'] = nome
        dicioProfissionaisSaude['Profissao'] = profissao
        dicioProfissionaisSaude['TeveCovid'] = teveCovid
        OpDb.InsereTudo('ProfissionaisSaude', dicioProfissionaisSaude)

    #Método que atualiza um ítem dessa lista no banco
    def AtualizaProfissional(coluna1, valor1, coluna2, valor2):
        OpDb.AtualizaTudo('ProfissionaisSaude', coluna1, valor1, coluna2, valor2)
