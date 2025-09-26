# controllers/book_controller.py

from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from models.guia import db, Position, Variation, Step

# Define o diretório onde as imagens serão salvas.
# Recomenda-se criar essa pasta na raiz do seu projeto.
UPLOAD_FOLDER = 'static/imagens' # Exemplo: static/uploads/posicoes

# Rotas de Criação de novas posições
def add_position_advanced():
    if request.method == 'POST':
        try:
            # 1. Obter dados da Posição
            position_name = request.form['position_name']
            position_desc = request.form['position_description']
            position_level = 'advanced'

            # 2. Processar o upload da imagem
            if 'imagem_upload' in request.files:
                file = request.files['imagem_upload']
                if file.filename != '':
                    # Garante um nome de arquivo seguro
                    filename = secure_filename(file.filename)
                    
                    # Constrói o caminho completo para salvar a imagem
                    upload_path = os.path.join(UPLOAD_FOLDER, filename)
                    
                    # Salva o arquivo no diretório
                    file.save(upload_path)
                    
                    # Armazena apenas o caminho relativo ou nome do arquivo no banco de dados
                    position_image = os.path.join(filename)
                else:
                    position_image = None
            else:
                position_image = None

            # 3. Cria e adiciona a nova Posição no banco de dados
            new_position = Position(
                name=position_name,
                description=position_desc,
                image=position_image, # Use o caminho salvo
                level=position_level
            )
            db.session.add(new_position)
            db.session.flush()

            # 4. Obter dados das Variações e Passos (o restante do seu código)
            variation_names = request.form.getlist('variation_name[]')
            variation_descs = request.form.getlist('variation_desc[]')
            
            num_variations = len(variation_names)

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
                
                num_steps = len(step_imgs)
                
                for j in range(num_steps):
                    new_step = Step(
                        img=step_imgs[j] if step_imgs[j] else None,
                        description=step_descs[j],
                        variation=new_variation
                    )
                    db.session.add(new_step)

            db.session.commit()
            flash("Posição adicionada com sucesso!", 'success')
            return redirect(url_for('avancadm_route'))

        except Exception as e:
            db.session.rollback()
            print(f"Erro ao salvar a posição: {e}")
            flash(f"Erro ao salvar a posição: {e}. Por favor, tente novamente.", 'danger')
            return redirect(url_for('add_position_advanced'))

    return render_template('adm/posicoes/posicao_avanc.html')

# DELETE
def delete_position_advanced(position_id):
    try:
        position = Position.query.filter_by(id=position_id, level='advanced').first_or_404()
        
        # 1. Obter o caminho da imagem antes de deletar o registro do banco de dados
        # A posição.image já armazena o caminho relativo (ex: 'uploads/posicoes/imagem.jpg')
        image_path = position.image

        # 2. Deletar o registro do banco de dados
        db.session.delete(position)
        db.session.commit()
        
        # 3. Se a posição tinha uma imagem, tentar deletá-la do sistema de arquivos
        if image_path:
            # Constrói o caminho completo para o arquivo
            full_image_path = os.path.join('static/imagens', image_path)
            
            # 4. Verifica se o arquivo existe e o deleta
            if os.path.exists(full_image_path):
                os.remove(full_image_path)
                print(f"Imagem deletada: {full_image_path}")
            else:
                print(f"Atenção: A imagem não foi encontrada no caminho: {full_image_path}")

        # Armazena uma mensagem de sucesso na sessão
        flash(f'Posição "{position.name}" excluída com sucesso!', 'success')
        
        # Redireciona para a página de listagem
        return redirect(url_for('avancadm_route')) 

    except Exception as e:
        db.session.rollback()
        print(f"Erro ao excluir a posição ou a imagem: {e}")
        # Armazena uma mensagem de erro na sessão
        flash('Erro ao excluir a posição. Por favor, tente novamente.', 'danger')
        
        return redirect(url_for('avancadm_route'))
    
# Atualizar
def edit_position_advanced(position_id):
    position = Position.query.filter_by(id=position_id, level='advanced').first_or_404()

    if request.method == 'POST':
        try:
            position.name = request.form['position_name']
            position.description = request.form['position_description']
            # position.image = request.form.get('position_image')

            # --- Lógica de upload de imagem ---
            if 'imagem_upload' in request.files:
                file = request.files['imagem_upload']
                if file.filename != '':
                    # Deletar a imagem antiga, se existir
                    if position.image and os.path.exists(os.path.join('static', position.image)):
                        os.remove(os.path.join('static', position.image))

                    # Salvar a nova imagem
                    filename = secure_filename(file.filename)
                    upload_path = os.path.join(UPLOAD_FOLDER, filename)
                    file.save(upload_path)
                    
                    # Atualizar o caminho da imagem no banco de dados
                    position.image = os.path.join(filename)

            # --- Lógica de atualização de Variações e Passos ---

            # 1. Coletar os IDs das variações e passos que NÃO devem ser deletados
            # Isso requer que você adicione um campo oculto no HTML para os IDs existentes.
            # Por simplicidade, vou manter a abordagem de deletar e recriar,
            # que é mais fácil de gerenciar com o formulário dinâmico.

            # Deletar todas as variações e passos existentes para esta posição
            # antes de adicionar as novas do formulário.
            # É importante fazer isso em uma ordem que respeite as chaves estrangeiras.
            for variation in position.variations:
                for step in variation.steps:
                    db.session.delete(step)
                db.session.delete(variation)
            db.session.flush() # Para garantir que as exclusões sejam processadas antes de adicionar novas

            # 2. Adicionar as novas variações e passos com base nos dados do formulário
            variation_names = request.form.getlist('variation_name[]')
            variation_descs = request.form.getlist('variation_desc[]')
            
            num_variations = len(variation_names)

            for i in range(num_variations):
                new_variation = Variation(
                    name=variation_names[i],
                    description=variation_descs[i],
                    position=position
                )
                db.session.add(new_variation)
                db.session.flush()

                step_imgs = request.form.getlist(f'step_img_{i+1}[]')
                step_descs = request.form.getlist(f'step_desc_{i+1}[]')
                
                num_steps = len(step_imgs)

                for j in range(num_steps):
                    new_step = Step(
                        img=step_imgs[j] if step_imgs[j] else None,
                        description=step_descs[j],
                        variation=new_variation
                    )
                    db.session.add(new_step)

            db.session.commit()
            flash('Posição atualizada com sucesso!', 'success')
            return redirect(url_for('edit_position_advanced', position_id=position_id))

        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar a posição: {e}', 'danger')
            return redirect(url_for('edit_position_advanced', position_id=position_id))

    # Método GET: Renderiza o formulário pré-preenchido
    return render_template('adm/posicoes/posicao_avanc_update.html', position=position)