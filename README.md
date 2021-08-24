# CRUD com Flask
<p> Demonstração de CRUD utilizando Python, Flask e SQLAlchemy. Há 5 endpoints: </p>

- GET /usuarios: Retorna todos os usuários cadastrados.
- GET /usuario/{id}: Busca um usuário específico com base no id informado.
- POST /usuario: Cadastra um usuário, o corpo da requisição deve conter o nome e e-mail.
- PUT /usuario/{id}: Atualiza os dados do usuario do id informado com as informações contidas no corpo da requisição.
- DELETE /usuario/{id}: Deleta um usuário com base no id informado.

<h2>🛠 Tecnologias</h2>

  - Python 3
  - Flask
  - MySQL
  
<h2>▶️ Como executar o projeto</h2>

Pré-requisitos: Git, Python e MySQL.

```bash
# Clonar o repositório
git clone https://github.com/GlauciaLS/crud-flask.git

# Entrar dentro do repositório
cd crud-flask

# Acessar console do Python
python

# Criar tabelas
db.create_all()

# Instalar requisitos
pip install -r requirements.txt

# Rodar o app
python app.py
```
