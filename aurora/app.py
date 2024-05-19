from flask import Flask, render_template, url_for, request, redirect
from data import varios, Contatos

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", fontes = varios)

@app.route("/loja")
def store():
    return render_template("loja.html")

@app.route("/sobre")
def about():
    return render_template("sobre.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contato", methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        Contatos.append_row([request.form['nome'],request.form['email'], request.form['telf'], request.form['assunto'], request.form['mensagem']])
        return redirect('/')
    else:
        return render_template('contato.html')

app.run(debug=True)