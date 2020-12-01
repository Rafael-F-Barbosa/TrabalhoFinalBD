import mysql.connector.pooling
from mysql.connector import Error
from .GetDb import CreatePool


def SelecionaTudo(tabela):
    # Conexão ao banco de dados
    conn = CreatePool().get_connection()
    cursor = conn.cursor()

    # Cria script sql básico
    sql = "select * from "+ tabela
    print('Operacao: ', sql)

    # Faz a busca
    cursor.execute(sql)

    # Coloca items buscados em uma lista
    lista = cursor.fetchall()

    # Retorna a lista
    return lista

def InsereTudo(tabela, dicio):
    # Conexão ao banco de dados
    conn = CreatePool().get_connection()
    cursor = conn.cursor()

    # Cria script sql genérico
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
    # Comentados a impressão da operação e os dados inseridos
    #print('Operacao: ', sql)
    #print(val)
    # a = input("")

    # Inserção dos dados na tabela
    try: 
        cursor.execute(sql, tuple(val))
        conn.commit()
    except Error as err:
        print("Não foi possível realizar a operação: {}".format(err))
        a = input("")


def AtualizaTudo(tabela, coluna1, valor1, coluna2, valor2):
    # Conexão ao banco de dados
    conn = CreatePool().get_connection()
    cursor = conn.cursor()

    # Criando SQL genérico
    sql = "UPDATE "+ tabela + " SET " + coluna1 + " = '" + valor1 + "' WHERE " + coluna2 + " = " + valor2
    
    # Comentados a impressão da operação e os dados inseridos
    #print('Operacao: ', sql)
    #a = input("")
    # Inserindo na Tabela
    try: 
        cursor.execute(sql)
        conn.commit()
    except Error as err:
        print("Não foi possível realizar a operação: {}".format(err))
        a = input("")


def Deleta(tabela, coluna, valor):
    # Conexão ao banco de dados
    conn = CreatePool().get_connection()
    cursor = conn.cursor()

    # Criando SQL
    sql = "DELETE FROM "+ tabela + " WHERE " + coluna + " = " + valor
    #print('Operacao: ', sql)
    #a = input("")

    # Deletando da Tabela
    try: 
        cursor.execute(sql)
        conn.commit()
    except Error as err:
        print("Não foi possível realizar a operação: {}".format(err))
        a = input("")

def ChamaProcedure(nome, cpf):
    # Conexão ao banco de dados
    conn = CreatePool().get_connection()
    cursor = conn.cursor()

    # Chamando procedure e retornando a busca que a mesma retorna
    try:
        cursor.callproc(nome, [cpf])
        for result in cursor.stored_results():
            return result.fetchall()

    except Error as err:
        print("Não foi possível realizar a operação: {}".format(err))
        a = input("")
    
    return False
