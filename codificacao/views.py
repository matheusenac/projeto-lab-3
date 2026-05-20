from flask import render_template, redirect, url_for
from main import app
from dbbanco import *

@app.route('/produtos')
def produtos():
    createCarrinho()
    idCarrinho = readCarrinho()[0]
    produtos = readProdutos()
    return render_template('produtos.html', produtos=produtos, idCarrinho=idCarrinho)

# OU FICOU COMO ADICIONAR CASO FUTURAMENTE VITIN PRECISE CRIAR A DEF CARRINHO 
@app.route('/carrinho/<int:idProduto>')
def adicionarAoCarrinho(idProduto):
    idCarrinho = readCarrinho()[0]
    print(idCarrinho)
    print(idProduto)
    addProdCarrinho(idProduto, idCarrinho)
    return redirect(url_for('carrinho'))    
    #TIVE QUE IMPORTAR ISSO PRA FUNCIONAR, AGR TÁ REDIRECIONANDO PRA ROTA DA DEF 

#FAZER PASSAR O ID AQUI DPS - VITIN
@app.route('/carrinho')
def carrinho():
    id = readCarrinho()[0]
    listaItem = buscarProdutosNoCarrinho(id)
    return render_template('carrinho.html', itens = listaItem)
    
@app.route("/delete/<int:idProduto>")
def deletarCarrinho(idProduto):
    id = readItemCarrinho()[0]
