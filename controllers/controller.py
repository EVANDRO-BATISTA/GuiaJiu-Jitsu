# controllers/book_controller.py

from flask import render_template, request, redirect, url_for, flash
from models.guia import db, Position, Variation, Step

# Rota para ler (Read) todos os livros
def guia_bjj():
    return render_template('index.html')

def admin_bjj():
    return render_template('admin.html')

# def list_positions_by_level(level):
#     positions = Position.query.filter_by(level=level).all()
#     return render_template('positions_list.html', positions=positions, level=level)

# def show_position_details(position_id):
#     position = Position.query.get_or_404(position_id)
#     return render_template('position_details.html', position=position)

# # Nova função para criar e editar posições
# def form_position(position_id=None):
#     position = None
#     if position_id:
#         position = Position.query.get_or_404(position_id)

#     if request.method == 'POST':
#         name = request.form['name']
#         description = request.form['description']
#         level = request.form['level']
#         image = request.form.get('image') # .get() retorna None se não houver

#         if position:
#             # Lógica de Edição (Update)
#             position.name = name
#             position.description = description
#             position.level = level
#             position.image = image
#         else:
#             # Lógica de Criação (Create)
#             new_position = Position(
#                 name=name,
#                 description=description,
#                 level=level,
#                 image=image
#             )
#             db.session.add(new_position)
        
#         db.session.commit()
        
#         # Redireciona para a lista do nível correto
#         flash(f'Posição "{name}" salva com sucesso!', 'success')
#         return redirect(url_for('list_positions_by_level_route', level=level))

#     return render_template('position_form.html', position=position)



# # Rota para criar (Create) e atualizar (Update) um livro
# def form_book(book_id=None):
#     book = None
#     if book_id:
#         book = Book.query.get_or_404(book_id)

#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']

#         if book:
#             # Atualizar
#             book.title = title
#             book.author = author
#         else:
#             # Criar
#             book = Book(title=title, author=author)
#             db.session.add(book)
        
#         db.session.commit()
#         return redirect(url_for('list_books_route'))

#     return render_template('form.html', book=book)

# # Rota para deletar (Delete) um livro
# def delete_book(book_id):
#     book = Book.query.get_or_404(book_id)
#     db.session.delete(book)
#     db.session.commit()
#     return redirect(url_for('list_books_route'))