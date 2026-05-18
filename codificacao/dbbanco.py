from conexao import mysql

# CREATE
def createCarrinho():
    cursor = mysql.connection.cursor()
    cursor.execute("insert into carrinho values(default)")
    mysql.connection.commit()
    cursor.close()

def readCarrinho():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from carrinho")
    resultado = cursor.fetchone()
    mysql.connection.commit()
    cursor.close()
    return resultado

def addProdCarrinho(idProduto, idCarrinho):
    cursor = mysql.connection.cursor()
    cursor.execute("insert into item_carrinho (fk_produto, fk_carrinho, data_item) values (%s, %s, now())",(idProduto, idCarrinho))
    mysql.connection.commit()
    cursor.close()

# READ PRODUTOS FETCHALL
def readProdutos():
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
    sql = ("update produtos set estoque_Produto where id_produto = ", idProduto,)
    cursor.execute(sql)
    conex.commit()
    conex.close()

# DELETE
def Delete(self, idProduto):
    conex = conexao()
    cursor = conex.cursor()
    sql = ("delete from produtos where id = ", idProduto,)
    cursor.execute(sql)
    conex.commit()
    conex.close()

# UPDATE ITEM_CARRINHO
def UpdateCarrinho(self, fk_produto):
    conex = conexao()
    cursor = conex.cursor()
    sql = ("update produtos set item_carrinho where id_produto = ", fk_produto,)
    cursor.execute(sql)
    conex.commit()
    conex.close()

# DELETE ITEM_CARRINHO
def DeleteCarrinho(self, fk_produto):
    conex = conexao()
    cursor = conex.cursor()
    sql = ("delete from item_carrinho where id = ", fk_produto,)
    cursor.execute(sql)
    conex.commit()
    conex.close()