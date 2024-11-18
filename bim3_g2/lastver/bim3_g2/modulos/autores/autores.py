from flask import Blueprint, render_template, request, redirect, flash
from models import Autor
from database import db

bp_autor = Blueprint('autores', __name__, template_folder="templates")

@bp_autor.route('/')
def index():
    dados = Autor.query.all()
    return render_template('autores.html', autor = dados)

@bp_autor.route('/add')
def add():
    return render_template('autores_add.html')

@bp_autor.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    instituicao = request.form.get('instituicao')
    if nome and instituicao:
        bd_autor = Autor(nome, instituicao)
        db.session.add(bd_autor)
        db.session.commit()
        flash('Autor salvo com sucesso!!!')
        return redirect('/autores')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/autores/add')
