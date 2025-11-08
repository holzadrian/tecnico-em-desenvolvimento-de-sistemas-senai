from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(host='localhost', user='root', password='', port='3406', database='cinema_0711')

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/filmes")
def mostrar_filmes():
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM filmes ORDER BY titulo")
    filmes = cursor.fetchall()
    return render_template("lista_filmes.html", filmes=filmes)

@app.route("/novo")
def novo_filme():
    return render_template("novo_filme.html")

@app.route("/salvar", methods=['POST'])
def salvar_filmes():
    titulo = request.form['titulo']
    genero = request.form['genero']
    ano = request.form['ano']
    avaliacao = request.form['avaliacao']

    cursor = conexao.cursor()
    sql = "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)"
    valores = (titulo, genero, ano, avaliacao)
    cursor.execute(sql, valores)
    conexao.commit()

    return redirect("/filmes")

@app.route("/editar/<int:id>")
def editar_filme(id):
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM filmes WHERE id = %s", (id,))
    filme = cursor.fetchone()
    return render_template("editar_filme.html", filme=filme)

@app.route("/atualizar/<int:id>", methods=['POST'])
def atualizar_filme(id):
    titulo = request.form['titulo']
    genero = request.form['genero']
    ano = request.form['ano']
    avaliacao = request.form['avaliacao']

    cursor = conexao.cursor()
    sql = "UPDATE filmes SET titulo = %s, genero = %s, ano = %s, avaliacao = %s WHERE id = %s"
    cursor.execute(sql, (titulo, genero, ano, avaliacao, id))
    conexao.commit()

    return redirect("/filmes")

@app.route("/excluir/<int:id>")
def deletar_filme(id):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM filmes WHERE id = %s", (id,))
    conexao.commit()
    return redirect("/filmes")

if __name__ == '__main__':
    app.run(debug=True)