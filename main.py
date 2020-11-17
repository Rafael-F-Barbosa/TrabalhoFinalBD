import mysql.connector.pooling

from model.RegioesAdmin import RegioesAdmin

dbconfig = {
    "host": "localhost",
    "user": "root",
    "password": "Qaz1234!",
    "database": "BancoCovid",
}

RegioesAdmin.AdicionaRegiaoAdmin(dbconfig, 'Brasilia', 500)

RegioesAdmin.AdicionaRegiaoAdmin(dbconfig, 'Planaltina', 30000)

RegioesAdmin.AdicionaRegiaoAdmin(dbconfig, 'Sobral', 30000)

print(RegioesAdmin.ListaTodasRegioesAdmin(dbconfig))
