import mysql.connector

def CreatePool():
    dbconfig = {
        "host": "localhost",
        "user": "root",
        "password": "Qaz1234!",
        "database": "BancoCovid",
    }
    pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="my_pool",
        pool_size=1,
        pool_reset_session=True,
        **dbconfig)
    return pool
