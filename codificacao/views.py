from flask import render_template, request, redirect,  session, flash, url_for
from main import app

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')

