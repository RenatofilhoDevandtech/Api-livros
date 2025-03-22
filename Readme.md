# 📚 Sitelivros Vai na Web API

Uma API desenvolvida em Python utilizando Flask e SQLite para gerenciar o cadastro e listagem de livros, conectando-se a um frontend. Esta API permite a doação de livros e exibe uma lista completa de títulos cadastrados. 🚀

## 📦 **Recursos**
- **Listar Livros**: Obtenha uma lista com todos os livros cadastrados.
- **Cadastrar Livro**: Permita que usuários façam doações de livros com título, categoria, autor e URL da imagem.
- **Estrutura Simples**: Código limpo e fácil de entender.

## 🛠️ **Tecnologias Utilizadas**
- **Flask**: Framework web para Python.
- **SQLite**: Banco de dados leve e eficiente.
- **JSON**: Formato para troca de dados.

## 🚀 **Como Executar**
1. Clone este repositório:
    ```bash
    git clone [URL_DO_REPOSITORIO]
    ```
2. Instale as dependências necessárias:
    ```bash
    pip install flask
    ```
3. Inicie o servidor:
    ```bash
    python nome_do_arquivo.py
    ```
4. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:5000/
    ```

## 📝 **Endpoints**
- `GET /livros`: Retorna uma lista de todos os livros cadastrados.
- `POST /doar`: Cadastra um novo livro. Enviar os seguintes campos no corpo (JSON):
    - `titulo` (String): Título do livro.
    - `categoria` (String): Categoria do livro.
    - `autor` (String): Autor do livro.
    - `image_url` (String): URL da imagem do livro.

## 📌 **Exemplo de Requisição POST**
```json
{
  "titulo": "O Pequeno Príncipe",
  "categoria": "Ficção",
  "autor": "Antoine de Saint-Exupéry",
  "image_url": "https://linkdaimagem.com/capa.jpg"
}
