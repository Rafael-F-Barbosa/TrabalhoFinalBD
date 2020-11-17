import mysql.connector

def findDb(dbconfig):
    pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="my_pool",
        pool_size=1,
        pool_reset_session=True,
        **dbconfig)
    return pool
