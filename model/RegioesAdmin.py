import mysql.connector

def findDb(dbconfig):
    pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="my_pool",
        pool_size=1,
        pool_reset_session=True,
        **dbconfig)
    return pool

class RegioesAdmin:
    def __init__(self, codigo, nome, populacao):
        self.codigo = codigo
        self.nome = nome
        self.populacao = populacao
    def ListaTodasRegioesAdmin(dbconfig):
        conn = findDb(dbconfig).get_connection()
        cursor = conn.cursor();

        cursor.execute('select * from RegiaoAdmin')
        regioes = cursor.fetchall()
        return regioes

    def AdicionaRegiaoAdmin(dbconfig, nome, populacao):
        conn = findDb(dbconfig).get_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO RegiaoAdmin (nome, populacao) VALUES (%s, %s)"
        val = (nome, populacao)
        cursor.execute(sql, val)      
        conn.commit()

