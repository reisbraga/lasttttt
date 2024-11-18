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
    artigo_id = request.form.get('artigo_id')
    autor_id = request.form.get('autor_id')
    titulo = request.form.get('titulo')
    ano_publicacao = request.form.get('ano_publicacao')
    if artigo_id and autor_id and titulo and ano_publicacao:
        bp_artigo = Artigo(artigo_id, autor_id, titulo, ano_publicacao)
        db.session.add(bp_artigo)
        db.session.commit()
        flash('Artigo salvo com sucesso!!!')
        return redirect('/artigos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/artigos/add')
