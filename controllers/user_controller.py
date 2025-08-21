from flask import render_template, request, redirect, url_for, jsonify
from models import user
from models.user import User, db

class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)
    
    #criar
    @staticmethod
    def contact():        
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            # Validação se o email é igual no banco
            existing_email = User.query.filter_by(email = email).first()
            if existing_email:
                return 'Erro: Email já existe!', 400

                    

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))
    
        return render_template('contact.html')

    #delete
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)

        if user:
            db.session.delete(user)
            db.session.commit()
        return redirect('/')

    #Update
    @staticmethod
    def update_user(user_id):
        user = User.query.get(user_id)

        if user:
            user.name = request.form['name']
            user.email = request.form['email']
            db.session.commit()
        return redirect('/')