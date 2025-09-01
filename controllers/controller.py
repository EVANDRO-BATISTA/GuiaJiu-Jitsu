# controllers/book_controller.py

from flask import render_template, request, jsonify, redirect, url_for, flash
from models.guia import db, Position, Variation, Step
from flask import flash, get_flashed_messages # Adicione este import

# Rotas das View
def guia_bjj():
    positions = Position.query.filter_by(level='beginner').all()
    return render_template('index.html', positions=positions)

def indexinter():
    positions = Position.query.filter_by(level='intermediate').all()
    return render_template('index_inter.html', positions=positions)

def indexavanc():
    positions = Position.query.filter_by(level='advanced').all()
    return render_template('index_avanc.html', positions=positions)

def admin_bjj():
    positions = Position.query.filter_by(level='beginner').all()
    return render_template('adm/admin.html', positions=positions)

def interadm():
    positions = Position.query.filter_by(level='intermediate').all()
    return render_template('adm/inter_adm.html',positions=positions)

def avancadm():
    positions = Position.query.filter_by(level='advanced').all()
    return render_template('adm/avanc_adm.html',positions=positions)

# Rotas de Criação
def add_position_beginner():
    if request.method == 'POST':
        try:
            # 1. Obter dados da Posição
            position_name = request.form['position_name']
            position_desc = request.form['position_description']
            position_img = request.form.get('position_image')
            position_level = 'beginner'

            # Cria e adiciona a nova Posição
            new_position = Position(
                name=position_name,
                description=position_desc,
                image=position_img,
                level=position_level
            )
            db.session.add(new_position)
            db.session.flush()

            # 2. Obter dados das Variações e Passos
            variation_names = request.form.getlist('variation_name[]')
            variation_descs = request.form.getlist('variation_desc[]')
            
            num_variations = min(len(variation_names), len(variation_descs))

            for i in range(num_variations):
                new_variation = Variation(
                    name=variation_names[i],
                    description=variation_descs[i],
                    position=new_position
                )
                db.session.add(new_variation)
                db.session.flush()

                step_imgs = request.form.getlist(f'step_img_{i+1}[]')
                step_descs = request.form.getlist(f'step_desc_{i+1}[]')
                
                num_steps = min(len(step_imgs), len(step_descs))
                
                for j in range(num_steps):
                    new_step = Step(
                        img=step_imgs[j] if step_imgs[j] else None,
                        description=step_descs[j],
                        variation=new_variation
                    )
                    db.session.add(new_step)

            # 3. Commit no banco de dados
            db.session.commit()
            
            # Se chegarmos aqui sem erro, significa que os dados foram salvos.
            # O erro está no redirecionamento ou na página de sucesso.
            print("Dados salvos com sucesso. Tentando redirecionar...") 
            return redirect(url_for('add_position_beginner'))

        except Exception as e:
            # Este bloco só será executado se algo falhar ANTES do commit
            # ou durante o redirecionamento (caso o redirect() falhe).
            db.session.rollback()
            print(f"Erro ao salvar a posição: {e}")
            return f"Erro ao salvar a posição: {e}. Por favor, tente novamente."

    return render_template('adm/posicoes/posicao_iniciante.html')

# DELETE
def delete_position_beginner(position_id):
    try:
        position = Position.query.filter_by(id=position_id, level='beginner').first_or_404()
        
        db.session.delete(position)
        db.session.commit()
        
        # Armazena uma mensagem de sucesso na sessão
        flash(f'Posição "{position.name}" excluída com sucesso!', 'success')
        
        # Redireciona para a página de listagem
        return redirect(url_for('admin_route')) 

    except Exception as e:
        db.session.rollback()
        print(f"Erro ao excluir a posição: {e}")
        # Armazena uma mensagem de erro na sessão
        flash('Erro ao excluir a posição. Por favor, tente novamente.', 'danger')
        
        return redirect(url_for('sua_rota_de_listagem'))


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