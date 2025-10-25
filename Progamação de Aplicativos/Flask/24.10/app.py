from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/alunos")
def mostrar_alunos():
    alunos = [
        {"nome": "Lucas", "idade": 18, "nota": 10},
        {"nome": "Adrian", "idade": 17, "nota": 10},
        {"nome": "Lara", "idade": 16, "nota": 10},
        {"nome": "Gustavo", "idade": 16, "nota": 10},
        {"nome": "Emanuel", "idade": 16, "nota": 10}
    ]
    return render_template("alunos.html", lista_alunos=alunos)

if __name__ == "__main__":
    app.run(debug=True)