# app.py
from flask import Flask
from config import Config
from models.guia import db # Importe os novos modelos
from controllers.controller import guia_bjj, admin_bjj, interadm, avancadm, indexinter, indexavanc

app = Flask(__name__, template_folder='view')
app.config.from_object(Config)

# Inicializa o SQLAlchemy com o app
db.init_app(app)

# Cria as tabelas do banco de dados (se não existirem)
with app.app_context():
    db.create_all()

# Definição das rotas e seus respectivos controladores
app.add_url_rule('/', 'guiabjj_route', guia_bjj, methods=['GET', 'POST'])
app.add_url_rule('/indexinter', 'indexinter_route', indexinter, methods=['GET', 'POST'])
app.add_url_rule('/indexavanc', 'indexavanc_route', indexavanc, methods=['GET', 'POST'])
app.add_url_rule('/admin', 'admin_route', admin_bjj, methods=['GET', 'POST'])
app.add_url_rule('/interadm', 'interadm_route', interadm, methods=['GET', 'POST'])
app.add_url_rule('/avancadm', 'avancadm_route', avancadm, methods=['GET', 'POST'])
# app.add_url_rule('/add', 'form_book_route', form_book, methods=['GET', 'POST'])
# app.add_url_rule('/edit/<int:book_id>', 'form_book_route', form_book, methods=['GET', 'POST'])
# app.add_url_rule('/delete/<int:book_id>', 'delete_book_route', delete_book)

# app.add_url_rule('/positions/<level>', 'list_positions_by_level_route', list_positions_by_level)
# app.add_url_rule('/position/<int:position_id>', 'show_position_details_route', show_position_details)
# app.add_url_rule('/positions/add', 'add_position_route', form_position, methods=['GET', 'POST'])
# app.add_url_rule('/positions/<int:position_id>/edit', 'edit_position_route', form_position, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)