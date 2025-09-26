# controllers/controller.py

from flask import render_template, request, jsonify, redirect, url_for, flash
from models.guia import db, Position, Variation, Step
from flask import flash, get_flashed_messages # Adicione este import

# Rotas das View iniciais
def guia_bjj():
    positions = Position.query.filter_by(level='beginner').all()
    return render_template('index.html', positions=positions)

def view_ini(position_id):
    # Busque a posição pelo ID. `query.get()` é um método eficiente para isso.
    position = Position.query.get(position_id)
    
    # Se a posição não for encontrada, retorne um erro 404
    if not position:
        return "Posição não encontrada!", 404
        
    # Recupere as variações e os passos da posição encontrada
    # O SQLAlchemy já carrega as variações por causa da relação (backref)
    
    return render_template('adm/visualizar_Posicoes/view_position_ini.html', position=position)

    # positions = Position.query.filter_by(level='beginner').all()    
    # return render_template('adm/visualizar_Posicoes/view_position_ini.html', positions=positions)

def indexinter():
    positions = Position.query.filter_by(level='intermediate').all()
    return render_template('index_inter.html', positions=positions)

def view_inter(position_id):
    # Busque a posição pelo ID. `query.get()` é um método eficiente para isso.
    position = Position.query.get(position_id)
    
    # Se a posição não for encontrada, retorne um erro 404
    if not position:
        return "Posição não encontrada!", 404
        
    # Recupere as variações e os passos da posição encontrada
    # O SQLAlchemy já carrega as variações por causa da relação (backref)
    
    return render_template('adm/visualizar_Posicoes/view_position_inter.html', position=position)

    # positions = Position.query.filter_by(level='beginner').all()    
    # return render_template('adm/visualizar_Posicoes/view_position_ini.html', positions=positions)

def indexavanc():
    positions = Position.query.filter_by(level='advanced').all()
    return render_template('index_avanc.html', positions=positions)

def view_avanc(position_id):
    # Busque a posição pelo ID. `query.get()` é um método eficiente para isso.
    position = Position.query.get(position_id)
    
    # Se a posição não for encontrada, retorne um erro 404
    if not position:
        return "Posição não encontrada!", 404
        
    # Recupere as variações e os passos da posição encontrada
    # O SQLAlchemy já carrega as variações por causa da relação (backref)
    
    return render_template('adm/visualizar_Posicoes/view_position_ini.html', position=position)

    # positions = Position.query.filter_by(level='beginner').all()    
    # return render_template('adm/visualizar_Posicoes/view_position_ini.html', positions=positions)

def admin_bjj():
    positions = Position.query.filter_by(level='beginner').all()
    return render_template('adm/admin.html', positions=positions)

def interadm():
    positions = Position.query.filter_by(level='intermediate').all()
    return render_template('adm/inter_adm.html',positions=positions)

def avancadm():
    positions = Position.query.filter_by(level='advanced').all()
    return render_template('adm/avanc_adm.html',positions=positions)