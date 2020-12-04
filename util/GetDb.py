import mysql.connector

def CreatePool():
    # Define as configurações para o acesso ao banco de dados
    dbconfig = {
        "host": "localhost",
        "user": "root",
        "password": "Qaz1234!",
        "database": "BancoCovid",
    }
    # Cria conecção de pool e retorna esta ao usuário
    try:
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="my_pool",
            pool_size=1,
            pool_reset_session=True,
            **dbconfig)
        return pool
    except:
        print('Falha ao conectar ao banco dados.')
    # Retorna caso ocorra algum erro.
    return False