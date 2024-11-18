from flask import Blueprint, render_template, request, redirect, flash
from models import Artigo, Autor
from database import db

bp_artigo = Blueprint('artigos', __name__, template_folder="templates")

@bp_artigo.route('/')
def index():
    dados = Artigo.query.all()
    return render_template('artigos.html', artigo = dados)

@bp_artigo.route('/add')
def add():
    dados = Autor.query.all()
    return render_template('artigos_add.html', autor = dados)

@bp_artigo.route('/save', methods=['POST'])
def save():
    titulo = request.form.get('titulo')
    ano_publicacao = request.form.get('ano_publicacao')
    id_autor = request.form.get('id_autor')
    
    if  titulo and ano_publicacao and id_autor:
        bp_artigo = Artigo(titulo, ano_publicacao, id_autor)
        db.session.add(bp_artigo)
        db.session.commit()
        flash('Artigo salvo com sucesso!!!')
        return redirect('/artigos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/artigos/add')
