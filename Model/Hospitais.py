class RegioesAdmin:
    def __init__(self, codigo, nome, populacao):
        self.codigo = codigo;
        self.nome = nome;
        self.populacao = populacao;
    

brasilia = RegioesAdmin(123, 'Brasilia', 3000000);

print(brasilia.nome)