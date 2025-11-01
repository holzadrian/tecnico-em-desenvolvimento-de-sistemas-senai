from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/produtos")
def listar_produtos():
    conexao = mysql.connector.connect(host='localhost', port='3406', user='root', password='', database='holzs_collection')
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)