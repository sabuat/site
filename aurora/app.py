from flask import Flask, render_template, url_for

from data import fonte

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", fontes = fonte)

@app.route("/loja")
def store():
    return render_template("loja.html")

@app.route("/sobre")
def about():
    return render_template("sobre.html")

@app.route("/blog")
def blog():
    print(fonte)
    return render_template("blog.html")

@app.route("/contato")
def contact():
    return render_template("contato.html")

app.run(debug=True)