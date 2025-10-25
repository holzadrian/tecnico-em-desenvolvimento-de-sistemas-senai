from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    titulo = "Holz's Collection"
    return render_template("index.html", titulo=titulo)

@app.route("/produtos")
def listar_produtos():
    produtos = [
        {"nome": "Storm Grey Baggy Jeans", "preço": 319.90, "estoque": 9},
        {"nome": "Prime Baggy Jeans", "preço": 319.90, "estoque": 12},
        {"nome": "Black Baggy Jeans", "preço": 339.90, "estoque": 3},
        {"nome": "Horse Index Heavy", "preço": 219.00, "estoque": 6},
        {"nome": "Casal Cowboy", "preço": 109.90, "estoque": 1}
    ]
    return render_template("produtos.html", lista_produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)