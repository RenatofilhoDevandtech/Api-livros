from flask import Flask, request, jsonify  # Importamos a classe Flask do módulo flask para criar nossa aplicação web
from flask_cors import CORS
import sqlite3  # Importamos o módulo sqlite3 para manipulação do banco de dados SQLite

# Criamos uma instância do Flask e armazenamos na variável "app"
# O parâmetro __name__ indica que este arquivo será reconhecido como o principal da aplicação
app = Flask(__name__)
CORS(app)

# Aqui estamos criando uma rota para o endpoint "/"
@app.route("/")
def pagar_pessoas():
    # Retorna uma mensagem formatada em HTML para ser exibida na página principal
    return "<h1>Começar a semana, pagando suas dívidas, é bom demais</h1>"

# Função para inicializar o banco de dados SQLite
def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS LIVROS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                titulo TEXT NOT NULL, 
                categoria TEXT NOT NULL, 
                autor TEXT NOT NULL,  
                image_url TEXT NOT NULL  
            )
            """
        )

# Inicializa o banco de dados
init_db()

# Rota para cadastrar livros
@app.route("/doar", methods=["POST"])
def doar():
    try:
        # Obtém os dados enviados como JSON
        dados = request.get_json(force=True)
    except Exception as e:
        return jsonify({"erro": "Não foi possível processar os dados enviados. Certifique-se de que estão em formato JSON."}), 400

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not all([titulo, categoria, autor, image_url]):
        return jsonify({"erro": "Todos os campos (titulo, categoria, autor, image_url) são obrigatórios."}), 400

    with sqlite3.connect("database.db") as conn:
        conn.execute("""
            INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
            VALUES (?, ?, ?, ?)
        """, (titulo, categoria, autor, image_url))
        conn.commit()
    return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

# Rota para listar livros
@app.route("/livros", methods=["GET"])
def listar_livros():
    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = [
            {
                "id": item[0],
                "titulo": item[1],
                "categoria": item[2],
                "autor": item[3],
                "image_url": item[4]
            } for item in livros
        ]

    return jsonify(livros_formatados)

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    app.run(debug=True)
