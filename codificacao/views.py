from flask import render_template, redirect, request
from main import app
from dbquery import *



# ROTA PRODUTOS ###################################
@app.route('/')
def produtos():
    createCarrinho()
    idCarrinho = readCarrinho()[0]
    produtos = readProdutos()
    produtosFormatados = formatarValorUnitarioProd(produtos)
    return render_template('produtos.html', produtos=produtosFormatados, idCarrinho=idCarrinho)

# ROTA CARRINHO ###################################
@app.route('/carrinho')
def carrinho():
    num = request.form.get("numero")
    id = readCarrinho()[0]
    listaItem = readItensCarrinho(id)
    soma = 0
    for item in listaItem:
            print(item[2])
            print(item[4])
            soma = soma + item[2]*item[4]
    listaFormatada = formatarValorUnitarioItem(listaItem)
    print(soma)
    return render_template('carrinho.html', itens = listaFormatada, numero=num, total=soma)

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

#Rota atualizar qtd do item
@app.route("/update/<int:idProduto>", methods=['GET', 'POST'])
def atualizarQuantidade(idProduto):
    qtdStr = request.form.get("numero")
    if qtdStr is not None:
        qtd = int(qtdStr)
        if qtd > 0:
            updateItem(qtd, idProduto)
        else:
            deleteItemCarrinho(idProduto)
    return redirect("/carrinho")
