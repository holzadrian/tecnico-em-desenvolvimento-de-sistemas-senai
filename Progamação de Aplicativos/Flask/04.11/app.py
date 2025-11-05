from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, sqlite3

app = Flask(__name__)

# --- Função auxiliar para conectar ao banco ---
def conectar_banco():
    return mysql.connector.connect(
        host='localhost',
        port='3406',
        user='root',
        password='',
        database='cinema_flask'
    )


# --- Página inicial ---
@app.route('/')
def index():
    return render_template('index.html')


# --- Listar filmes ---
@app.route("/filmes")
def listar_filmes():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()
    cursor.close()
    conexao.close()

    return render_template('filmes.html', filmes=filmes)


# --- Listar salas ---
@app.route("/salas")
def listar_salas():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM salas")
    salas = cursor.fetchall()
    cursor.close()
    conexao.close()

    return render_template('salas.html', salas=salas)


# --- Exibir formulário e processar envio ---
@app.route('/enviar', methods=['GET', 'POST'])
def enviar_filme():
    if request.method == 'POST':
        titulo = request.form.get("titulo")
        genero = request.form.get("genero")
        ano = request.form.get("ano")
        avaliacao = request.form.get("avaliacao")

        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
            (titulo, genero, ano, avaliacao)
        )
        conexao.commit()
        cursor.close()
        conexao.close()

        # Redireciona para a lista de filmes após inserir
        return redirect(url_for('listar_filmes'))

    # Se for GET, apenas exibe o formulário
    return render_template('enviar.html')


# --- Inicialização ---
if __name__ == '__main__':
    app.run(debug=True)
