from flask import Flask, request, jsonify  # Importamos a classe Flask do módulo flask para criar nossa aplicação web
import sqlite3  # Importamos o módulo sqlite3 para manipulação do banco de dados SQLite

# Criamos uma instância do Flask e armazenamos na variável "app"
# O parâmetro __name__ indica que este arquivo será reconhecido como o principal da aplicação
app = Flask(__name__)

# Aqui estamos criando uma rota para o endpoint "/"
# Ou seja, quando acessarmos http://127.0.0.1:5000/, a função abaixo será executada
@app.route("/")
def pagar_pessoas():
    # Retorna uma mensagem formatada em HTML para ser exibida na página principal
    return "<h1>Começar a semana, pagando suas dívidas, é bom demais</h1>"


# Função para inicializar o banco de dados SQLite
# Criamos uma conexão com o banco de dados chamado 'database.db'
# Se o banco de dados ainda não existir, ele será criado automaticamente
def init_db():
    # Conectamos ao banco de dados SQLite e usamos "with" para garantir que a conexão seja fechada corretamente após a execução
    with sqlite3.connect("database.db") as conn:
        # Executamos um comando SQL para criar a tabela LIVROS, caso ela ainda não exista
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
        )  # A execução desse comando cria a tabela caso ela ainda não exista, garantindo que nossa estrutura de banco esteja configurada

# Chamamos a função para inicializar o banco de dados quando o programa for executado
init_db()

@app.route("/doar", methods=["POST"])
def doar():

    try:
        # Tenta obter os dados como JSON
        dados = request.get_json(force=True)  # Força a leitura do corpo como JSON mesmo sem o cabeçalho correto
    except Exception as e:
        return jsonify({"erro": "Não foi possível processar os dados enviados. Certifique-se de que estão em formato JSON."}), 400

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not all([titulo, categoria, autor, image_url]):
        return jsonify({"erro": "Todos os campos (titulo, categoria, autor, image_url) são obrigatórios."}), 400

    with sqlite3.connect("database.db") as conn:  # faz a conexão com o banco de dados
        conn.execute("""
        INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
        VALUES (?, ?, ?, ?)
        """, (titulo, categoria, autor, image_url))
        conn.commit()
    return jsonify({"mensagem": "Livro Cadastrado com sucesso"}), 201


@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []

        for item in livros:
          dicionario_livros ={
              "id":item[0],
              "titulo":item[1],
              "categoria":item[2],
              "autor":item[3],
              "image_url":item[4]
          }
          livros_formatados.append(dicionario_livros)

    return jsonify(livros_formatados)
# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração
    # Nesse modo nossa API responde automaticamente a qualquer atualização que fizermos no código
    app.run(debug=True)
