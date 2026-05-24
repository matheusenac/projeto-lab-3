from conexao import mysql

# TABELA CARRINHO #######################################

# Criar carrinho
def createCarrinho():
    cursor = mysql.connection.cursor()
    cursor.execute("insert into carrinho values(default)")
    mysql.connection.commit()
    cursor.close()

# Lê carrinho
def readCarrinho():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from carrinho")
    resultado = cursor.fetchone()
    mysql.connection.commit()
    cursor.close()
    return resultado

# TABELA PRODUTOS ####################################

# Lê todos os produtos
def readProdutos():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from produtos")
    resultado = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return resultado

# Lê um produto
def readUmProduto():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from produtos")
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

# TABELA ITEM_CARRINHO ####################################

# Adicionar item no carrinho 
def addItemCarrinho(idProduto, idCarrinho):
    cursor = mysql.connection.cursor()
    cursor.execute("insert into item_carrinho (fk_produto, fk_carrinho, data_item, qtd_item) values (%s, %s, now(), default)",(idProduto, idCarrinho))
    mysql.connection.commit()
    cursor.close()

# Lê os itens no carrinho e traz todas as suas caracteristicas da tabela produtos
def readItensCarrinho(idCarrinho):
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

# Lê um item de item-carrinho
def readItemCarrinho(idProduto):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from item_carrinho where fk_produto = %s",(idProduto,))
    resultado = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return resultado

# Attualiza o item na tabela item_carrinho
def updateItem(qtdItem, fk_produto):
    cursor = mysql.connection.cursor()
    cursor.execute("update item_carrinho set qtd_item = %s where fk_produto = %s",(qtdItem, fk_produto))
    mysql.connection.commit()
    cursor.close()

# Deleta um item na tabela item_cvarrinho
def deleteItemCarrinho(fk_produto):
    cursor = mysql.connection.cursor()
    sql = ("delete from item_carrinho where fk_produto = %s")
    cursor.execute(sql, (fk_produto,))
    mysql.connection.commit()
    cursor.close() 