from flask import render_template, redirect
from main import app
from codificacao.dbquery import *

# ROTA PRODUTOS ###################################
@app.route('/')
def produtos():
    createCarrinho()
    idCarrinho = readCarrinho()[0]
    produtos = readProdutos()
    return render_template('produtos.html', produtos=produtos, idCarrinho=idCarrinho)

# ROTA CARRINHO ###################################
@app.route('/carrinho')
def carrinho():
    id = readCarrinho()[0]
    listaItem = readItensCarrinho(id)
    return render_template('carrinho.html', itens = listaItem)

# Rota adicionar ao item carrinho
@app.route('/carrinho/<int:idProduto>')
def adicionarAoCarrinho(idProduto):
    idCarrinho = readCarrinho()[0]
    item = readItemCarrinho(idProduto)
    if not item:
        addItemCarrinho(idProduto, idCarrinho)
    else:
        updateItem(item[0][3]+1, idProduto)
    return redirect('/carrinho')

# Rota deletar item ao carrinho
@app.route("/delete/<int:idProduto>")
def deletarCarrinho(idProduto):
    idProduto = readItemCarrinho(idProduto)[0][1]
    deleteItemCarrinho(idProduto)
    return redirect("/carrinho")
