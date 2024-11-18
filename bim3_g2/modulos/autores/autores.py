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

@bp_autor.route("/remove/<int:id>")
def remove(id):
    dados = Autor.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Paciente removido com sucesso!')
        return redirect("/pacientes")
    else:
        flash("Caminho incorreto!")
        return redirect("/pacientes")

@bp_autor.route("/edita/<int:id>")
def edita(id_autor):
    autor = Autor.query.get(id_autor)
    return render_template("autor_edita.html", dados=autor)

@bp_autor.route("/editasave", methods=['POST'])
def editasave():
    id_artigo = request.form.get('id_artigo')
    titulo = request.form.get('titulo')
    ano_lancamento = request.form.get('ano_lancamento')
    if id and titulo and ano_lancamento:
        artigos = Autor.query.get(id)
        artigos.titulo = titulo
        artigos.ano_lancamento = ano_lancamento
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/autores')
    else:
        flash('Dados incompletos.')
        return redirect("/autores")