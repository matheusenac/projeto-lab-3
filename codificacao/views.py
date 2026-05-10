from flask import render_template
from main import app
from dbbanco import *

@app.route('/produtos')
def produtos():
    createCarrinho()
    idCarrinho = readCarrinho()[0]
    produtos = readProdutos()
    return render_template('produtos.html', produtos=produtos, idCarrinho=idCarrinho)

@app.route('/carrinho/<int:idProduto>', methods=["GET","POST"])
def carrinho(idProduto):
    idCarrinho = readCarrinho()[0]
    print(idCarrinho)
    print(idProduto)
    addProdCarrinho(idProduto, idCarrinho)
    return render_template('carrinho.html')