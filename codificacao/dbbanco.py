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
    cursor.execute("insert into item_carrinho (fk_produto, fk_carrinho, data_item, qtd_item) values (%s, %s, now(), default)",(idProduto, idCarrinho))
    mysql.connection.commit()
    cursor.close()

# BUSCA PARA A EXIBIR OS ITENS NO CARRINHO 
def buscarProdutosNoCarrinho(idCarrinho):
    cursor = mysql.connection.cursor()
    sql = ("""
           select p.id_produto, p.nome_produto, p.preco_produto, p.img_produto, i.qtd_item
           from produtos p 
           inner join item_carrinho i on p.id_produto = i.fk_produto
           where i.fk_carrinho = %s
           """)
    cursor.execute(sql,(idCarrinho,))
    resposta = cursor.fetchall()
    cursor.close()
    return resposta

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
    cursor = mysql.connection.cursor()
    cursor.execute("select * from produtos")
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

# READ PRODUTO CARRINHO
def readItemCarrinho(fk_produto):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from item_carrinho where fk_produto = %s",(fk_produto,))
    resultado = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    if resultado:
        return resultado
    return False;

# UPDATE ITEM_CARRINHO
def updateItem(qtdItem, fk_produto):
    cursor = mysql.connection.cursor()
    cursor.execute("update item_carrinho set qtd_item = %s where fk_produto = %s",(qtdItem, fk_produto))
    mysql.connection.commit()
    cursor.close()

# DELETE ITEM_CARRINHO
def deleteItemCarrinho(fk_produto):
    cursor = mysql.connection.cursor()
    sql = ("delete from item_carrinho where fk_produto = %s")
    cursor.execute(sql, (fk_produto,))
    mysql.connection.commit()
    cursor.close() 