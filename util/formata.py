import datetime

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

def formata_lista(lista):
    lista_final = []
    for x in lista:
        lista_final.append(list(x))
    return lista_final

def formata_data(data):
    ano, mes, dia = data[:4], data[5:7], data[8:]
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    return str(dia + '-' + meses[int(mes)-1] + '-' + ano)
def formata_texto(texto):
    texto_final = ' ' + texto 
    if(len(texto_final)>20):
        texto_final = texto_final[:20]
    elif(len(texto_final) < 20):
        texto_final = texto_final + (20-len(texto_final))*' '

    return texto_final

def imprime_lista_tabela_formatado(lista_tabelas, colunas):
    try:     
        tam = len(lista_tabelas[0])
    except:
        print("Não há dados nessa tabela.")
        return

    linha = (20 * tam) *'-'
    linha = RED + linha + RESET
    
    print(linha)
    
    for c in colunas:
        print(formata_texto(c), end=' ')
    print('')
    print(linha)

    for i in lista_tabelas:
        for j in i:
            if(isinstance(j, datetime.date)):
                data = formata_data(str(j))
                print(formata_texto(data), end=' ')
            else:
                print(formata_texto(str(j)), end=' ')
        print('')

    print(linha)
