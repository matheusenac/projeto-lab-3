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
    itens = readItemCarrinho(idProduto)
    print(itens[0][3])
    idCarrinho = readCarrinho()[0]
    if itens:
        for item in itens:
            if item[0] == idProduto:
                somaItem = item[3]+1
                print(somaItem)
                updateItem(somaItem,idProduto)
    else:
        addProdCarrinho(idProduto, idCarrinho)
    return redirect(url_for('carrinho'))

#FAZER PASSAR O ID AQUI DPS - VITIN
@app.route('/carrinho')
def carrinho():
    id = readCarrinho()[0]
    listaItem = buscarProdutosNoCarrinho(id)
    print(listaItem)
    return render_template('carrinho.html', itens = listaItem)
    
@app.route("/delete/<int:idProduto>")
def deletarCarrinho(idProduto):
    idProduto = readItemCarrinho(idProduto)[0][1]
    print(idProduto)
    deleteItemCarrinho(idProduto)
    return redirect("/carrinho")
