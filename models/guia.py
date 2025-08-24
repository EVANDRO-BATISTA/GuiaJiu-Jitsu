# models/positions.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabela para as Posições (Guarda Fechada, Montada, etc.)
class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True) # A imagem da posição
    
    # O nível (beginner, intermediate, advanced)
    level = db.Column(db.String(50), nullable=False)
    
    # Relacionamento com as variações
    variations = db.relationship('Variation', backref='position', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Position {self.name}>'

# Tabela para as Variações (Guarda Fechada Tradicional, etc.)
class Variation(db.Model):
    __tablename__ = 'variations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Chave estrangeira para a tabela Position
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'), nullable=False)

    # Relacionamento com os passos
    steps = db.relationship('Step', backref='variation', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Variation {self.name}>'

# Tabela para os Passos de cada variação
class Step(db.Model):
    __tablename__ = 'steps'
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=False)
    
    # Chave estrangeira para a tabela Variation
    variation_id = db.Column(db.Integer, db.ForeignKey('variations.id'), nullable=False)

    def __repr__(self):
        return f'<Step {self.id}>'

# # models/book.py

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Book(db.Model):
#     __tablename__ = 'books'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     author = db.Column(db.String(100), nullable=False)

#     def __repr__(self):
#         return f'<Book {self.title}>'