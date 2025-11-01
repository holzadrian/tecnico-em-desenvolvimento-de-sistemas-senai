from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/filmes")
def listar_filmes():
    conexao = mysql.connector.connect(host='localhost', port='3406', user='root', password='', database='cinema_flask')
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template('filmes.html', filmes=filmes)

@app.route("/salas")
def listar_salas():
    conexao = mysql.connector.connect(host='localhost', port='3406', user='root', password='', database='cinema_flask')
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM salas")
    salas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template('salas.html', salas=salas)

if __name__ == '__main__':
    app.run(debug=True)