import mysql.connector
from model.RegioesAdmin import RegioesAdmin
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qaz1234!",
    database="mydatabase"
)


mycursor = mydb.cursor()


brasilia = RegioesAdmin(1, 'Brasilia',30000)
print(brasilia.nome)


# CREATING A DATABASE
# mycursor.execute("CREATE DATABASE mydatabase")

# SHOWING ALL DATABASES IN THIS SERVER
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# # CREATING A TABLE IN MYSQL
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)
# mycursor.execute(
#     "CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute(
#     "CREATE TABLE IF NOT EXISTS owners (name VARCHAR(255), address VARCHAR(255))")
