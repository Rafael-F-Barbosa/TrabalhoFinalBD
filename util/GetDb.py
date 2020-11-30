import mysql.connector

def CreatePool():
    dbconfig = {
        "host": "localhost",
        "user": "root",
        "password": "gera2908",
        "database": "BancoCovid",
    }
    try:
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="my_pool",
            pool_size=1,
            pool_reset_session=True,
            **dbconfig)
        return pool
    except:
        print('Falha ao conectar ao banco dados.')
    
    return False