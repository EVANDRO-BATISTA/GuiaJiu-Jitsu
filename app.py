import os
from flask import Flask
from config import Config
from controllers.user_controller import UserController
from models.user import db

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

# Inicializa o banco de dados
db.init_app(app)

# Criar as tabelas
with app.app_context():
    db.create_all()

#Rotas
app.add_url_rule('/', 'index', UserController.index)
app.add_url_rule('/contact', 'contact', UserController.contact, methods=['GET', 'POST'])
app.add_url_rule('/delete/<int:user_id>', 'delete_user', UserController.delete_user, methods=['POST'])
app.add_url_rule('/update/<int:user_id>', 'update_user', UserController.update_user, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)