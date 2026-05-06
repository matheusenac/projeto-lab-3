from flask import render_template
from main import app
from dbbanco import *

#dbEcommerce = dbEcommerce()

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/produtos', methods=["GET","POST"])
def produtos():
    produtos = readFetchall()
    print(produtos)
    return render_template('produtos.html', produtos=produtos)

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

