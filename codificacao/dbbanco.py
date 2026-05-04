from conexao import conexao
class produtoCarrinho:
    def __init__(self, idProduto = None, nomeProduto = None, descricaoProduto = None, precoProduto = None, estoqueProduto = None):
        self.idProduto = idProduto
        self.nomeProduto = nomeProduto
        self.descricaoProduto = descricaoProduto
        self.precoProduto = precoProduto
        self.estoqueProduto = estoqueProduto

# CREATE
def Create(self):
    conex = conexao()
    pass

# READ FETCHALL
def readFetchall():
    conex = conexao()
    cursor = conex.cursor()
    cursor.execute("select * from produto")
    resultado = cursor.fetchall()
    conex.close()
    return resultado

# READ FETCHONE
def readFetchone():
    conex = conexao()
    cursor = conex.cursor()
    cursor.execute("select * from produto")
    resultado = cursor.fetchone()
    conex.close()
    return resultado

# UPDATE
def Update(self, idProduto):
    conex = conexao()
    cursor = conex.cursor()
    sql = ("update produto set estoqueProduto where idProduto = ", idProduto)
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