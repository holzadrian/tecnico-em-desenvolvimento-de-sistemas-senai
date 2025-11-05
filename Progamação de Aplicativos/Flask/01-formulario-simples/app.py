from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/enviar', methods=['POST'])
def processar_formulario():
    nome = request.form["nome"]
    email = request.form["email"]
    mensagem = request.form["mensagem"]
    return f"<h2>Obrigado, {nome}! Sua mensagem foi recebida.</h2>"

if __name__ == "__main__":
    app.run(debug=True)