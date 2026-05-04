import mysql.connector
from mysql.connector import Error

def conexao():
    try:
        conex = mysql.connector.connect(
        host = "localhost",
        database = "dbloja",
        user = "root",
        password = "senac"
    )

        if conex.is_connected():
            cursor = conex.cursor()

    except Error:
        print(Error)

    finally:
        if conex.is_connected():
            cursor.close()
            conex.close()