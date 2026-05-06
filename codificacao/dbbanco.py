from conexao import mysql

# CREATE
def Create(self):
    conex = conexao()
    pass

# READ FETCHALL
def readFetchall():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from produtos")
    resultado = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return resultado

# READ FETCHONE
def readFetchone():
    cursor = conex.cursor()
    cursor.execute("select * from produtos")
    resultado = cursor.fetchone()
    conex.close()
    return resultado

# UPDATE
def Update(self, idProduto):
    conex = conexao()
    cursor = conex.cursor()
    sql = ("update produtos set estoque_Produto where id_produto = ", idProduto)
    cursor.execute(sql)
    conex.commit()
    conex.close()

# DELETE
def Delete(self, idProduto):
    conex = conexao()
    cursor = conex.cursor()
    sql = ("delete from produtos where id = ", idProduto)
    cursor.execute(sql)
    conex.commit()
    conex.close()