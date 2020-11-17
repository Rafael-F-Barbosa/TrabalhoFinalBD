import mysql.connector.pooling
from mysql.connector import Error

from .GetDb import CreatePool


# Aqui tem operações no banco de dados que podem ser reutilizadas.

def SelecionaTudo(tabela):
    # Banco de dados
    conn = CreatePool().get_connection()
    cursor = conn.cursor()
    
    # Faz a busca SQL
    sql = "select * from "+ tabela
    print('Operacao: ', sql)
    cursor.execute(sql);

    # Coloca items buscados em uma lista
    lista = cursor.fetchall()

    return lista

def InsereTudo(tabela, dicio):
    # Banco de dados
    conn = CreatePool().get_connection()
    cursor = conn.cursor()

    # Criando SQL
    colunas = "("
    valores = "("
    val = []
    for x in dicio:
        colunas+= (x+', ')
        valores+= ('%s, ')
        val.append(dicio[x])
    colunas = colunas[:-2] + ')'
    valores = valores[:-2] + ')'
    sql = "INSERT INTO "+ tabela + colunas + " VALUES " + valores
    print('Operacao: ', sql)
    
    # Inserindo na Tabela
    try: 
        cursor.execute(sql, tuple(val))
        conn.commit()
    except Error as err:
        print("Deu ruim: {}".format(err))
