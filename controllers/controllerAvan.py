# controllers/book_controller.py

from flask import render_template, request, jsonify, redirect, url_for, flash
from models.guia import db, Position, Variation, Step
from flask import flash, get_flashed_messages # Adicione este import

# Rotas de Criação de novas posições
def add_position_advanced():
    if request.method == 'POST':
        try:
            # 1. Obter dados da Posição
            position_name = request.form['position_name']
            position_desc = request.form['position_description']
            position_img = request.form.get('position_image')
            position_level = 'advanced'

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
            return redirect(url_for('add_position_advanced'))

        except Exception as e:
            # Este bloco só será executado se algo falhar ANTES do commit
            # ou durante o redirecionamento (caso o redirect() falhe).
            db.session.rollback()
            print(f"Erro ao salvar a posição: {e}")
            return f"Erro ao salvar a posição: {e}. Por favor, tente novamente."

    return render_template('adm/posicoes/posicao_avan.html')

# DELETE
def delete_position_advanced(position_id):
    try:
        position = Position.query.filter_by(id=position_id, level='advanced').first_or_404()
        
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
        
        return redirect(url_for('admin_route'))

# Atualizar
def edit_position_advanced(position_id):
    position = Position.query.filter_by(id=position_id, level='advanced').first_or_404()

    if request.method == 'POST':
        try:
            position.name = request.form['position_name']
            position.description = request.form['position_description']
            position.image = request.form.get('position_image')

            # --- Lógica de atualização de Variações e Passos ---

            # 1. Coletar os IDs das variações e passos que NÃO devem ser deletados
            # Isso requer que você adicione um campo oculto no HTML para os IDs existentes.
            # Por simplicidade, vou manter a abordagem de deletar e recriar,
            # que é mais fácil de gerenciar com o formulário dinâmico.

            # Deletar todas as variações e passos existentes para esta posição
            # antes de adicionar as novas do formulário.
            # É importante fazer isso em uma ordem que respeite as chaves estrangeiras.
            for variation in position.variations:
                # Deletar passos primeiro
                for step in variation.steps:
                    db.session.delete(step)
                # Depois deletar a variação
                db.session.delete(variation)
            db.session.flush() # Para garantir que as exclusões sejam processadas antes de adicionar novas

            # 2. Adicionar as novas variações e passos com base nos dados do formulário
            variation_names = request.form.getlist('variation_name[]')
            variation_descs = request.form.getlist('variation_desc[]')
            
            num_variations = len(variation_names) # Use o comprimento real das listas

            for i in range(num_variations):
                new_variation = Variation(
                    name=variation_names[i],
                    description=variation_descs[i],
                    position=position
                )
                db.session.add(new_variation)
                db.session.flush() # Flushes para que new_variation tenha um ID antes de criar Steps

                # Note que os nomes dos campos de passo agora são 'step_img_X[]' e 'step_desc_X[]'
                # onde X é o índice da variação + 1
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
            # Renderiza novamente o formulário com os dados que o usuário tentou enviar,
            # ou redireciona para a rota GET da edição para recarregar os dados do banco
            return redirect(url_for('edit_position_advanced', position_id=position_id))

    # Método GET: Renderiza o formulário pré-preenchido
    return render_template('adm/posicoes/posicao_avan_update.html', position=position)