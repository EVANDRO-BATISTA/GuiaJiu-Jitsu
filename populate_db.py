import os
import json
from flask import Flask
from models.guia import db, Position, Variation, Step
from config import Config

# Crie uma instância de aplicação Flask temporária para o contexto do banco de dados
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Seus dados JSON
default_data = {
    "beginner": [
        {
            "name": "Guarda Fechada",
            "description": "Posição fundamental onde você envolve o oponente com as pernas, controlando a distância e prevenindo passes.",
            "image": "beginner_guard.png",
            "variations": [
                {
                    "name": "Guarda Fechada Tradicional",
                    "description": "Técnica básica de defesa",
                    "steps": [
                        { "img": "placeholder.png", "description": "Deite-se de costas com pernas ao redor do quadril do oponente" },
                        { "img": "placeholder.png", "description": "Cruze os tornozelos mantendo os joelhos pressionados" },
                        { "img": "placeholder.png", "description": "Use mãos para controlar os pulsos ou colar do oponente" }
                    ]
                },
                {
                    "name": "Guarda com Triângulo",
                    "description": "Preparação para finalização",
                    "steps": [
                        { "img": "placeholder.png", "description": "Abra uma perna e passe sobre o ombro do oponente" },
                        { "img": "placeholder.png", "description": "Cruze o tornozelo sobre o joelho formando triângulo" },
                        { "img": "placeholder.png", "description": "Puxe a cabeça do oponente para estabilizar a posição" }
                    ]
                }
            ]
        },
        {
            "name": "Montada",
            "description": "Posição dominante sentada no torso do oponente, oferecendo controle total e oportunidades de finalização.",
            "image": "beginner_mount.png",
            "variations": [
                {
                    "name": "Montada Alta",
                    "description": "Controle máximo com estabilidade",
                    "steps": [
                        { "img": "placeholder.png", "description": "Coloque joelhos junto ao torso do oponente" },
                        { "img": "placeholder.png", "description": "Pés mantidos abaixo dos joelhos para estabilidade" },
                        { "img": "placeholder.png", "description": "Mãos controlando os pulsos ou cabeça do adversário" }
                    ]
                }
            ]
        },
        {
            "name": "Controle Lateral",
            "description": "Posição lateral de controle onde você imobiliza o oponente entre seu torso e o chão.",
            "image": "beginner_sidecontrol.png",
            "variations": [
                {
                    "name": "Controle com Pompeamento",
                    "description": "Imobilização avançada com controle",
                    "steps": [
                        { "img": "placeholder.png", "description": "Posicione o peito pressionando o torso do oponente" },
                        { "img": "placeholder.png", "description": "Joelho junto ao quadril para bloquear movimentos" },
                        { "img": "placeholder.png", "description": "Mão controlando o colarinho ou ombro para pressão" }
                    ]
                }
            ]
        }
    ],
    "intermediate": [
        {
            "name": "Guarda Aberta",
            "description": "Posição com pernas ativas controlando o oponente à distância, permitindo varreduras complexas.",
            "image": "intermediate_openguard.png",
            "variations": [
                {
                    "name": "Guarda Pombo",
                    "description": "Transição para chave de pé",
                    "steps": [
                        { "img": "placeholder.png", "description": "Posicione panturrilha em peito do oponente" },
                        { "img": "placeholder.png", "description": "Pé externo junto ao quadril para controle" },
                        { "img": "placeholder.png", "description": "Braços seguram calça para limitar mobilidade" }
                    ]
                }
            ]
        },
        {
            "name": "Pegada nas Costas",
            "description": "Posição dominante atrás do oponente com ganchos nas pernas, ideal para finalizações.",
            "image": "intermediate_backcontrol.png",
            "variations": [
                {
                    "name": "Cruzamento Lagartixa",
                    "description": "Técnica para manter controle",
                    "steps": [
                        { "img": "placeholder.png", "description": "Cruze os pés atrás dos joelhos do oponente" },
                        { "img": "placeholder.png", "description": "Braço sob o pescoço para controle de cabeça" },
                        { "img": "placeholder.png", "description": "Mão livre na lombar para apunhalamento" }
                    ]
                }
            ]
        },
        {
            "name": "Meia-Guarda",
            "description": "Posição defensiva onde você prende uma perna do oponente, criando oportunidades de escape.",
            "image": "intermediate_halfguard.png",
            "variations": [
                {
                    "name": "Meia-Guarda Profunda",
                    "description": "Varreduras eficientes",
                    "steps": [
                        { "img": "placeholder.png", "description": "Deite-se lateralmente prendendo perna adversária" },
                        { "img": "placeholder.png", "description": "Use joelho para criar ângulo favorável" },
                        { "img": "placeholder.png", "description": "Braços criam alavanca para rolar" }
                    ]
                }
            ]
        }
    ],
    "advanced": [
        {
            "name": "Berimbolo",
            "description": "Técnica avançada de inversão que permite assumir a posição nas costas a partir da guarda.",
            "image": "advanced_berimbolo.png",
            "variations": [
                {
                    "name": "Berimbolo Tradicional",
                    "description": "Transição rápida para costas",
                    "steps": [
                        { "img": "placeholder.png", "description": "Envolva perna adversária com De La Riva hook" },
                        { "img": "placeholder.png", "description": "Inverse corpo por baixo do adversário" },
                        { "img": "placeholder.png", "description": "Use momentum para girar nas costas" }
                    ]
                }
            ]
        },
        {
            "name": "Guarda de Borboleta",
            "description": "Posição sentada usando os pés nos quadris para explosões e varreduras.",
            "image": "advanced_butterflyguard.png",
            "variations": [
                {
                    "name": "Varredura Parafinho",
                    "description": "Varrendo com técnica precisa",
                    "steps": [
                        { "img": "placeholder.png", "description": "Posicione ambos os pés nos quadris adversários" },
                        { "img": "placeholder.png", "description": "Braços controlam pulsos ou ombros" },
                        { "img": "placeholder.png", "description": "Empurre com os pés enquanto levanta quadril" }
                    ]
                }
            ]
        },
        {
            "name": "Ashi Garami",
            "description": "Controle avançado de pernas para aplicação de chaves de tornozelo e joelho.",
            "image": "advanced_ashigarami.png",
            "variations": [
                {
                    "name": "Entrada Estilo Japonês",
                    "description": "Controle para footlock",
                    "steps": [
                        { "img": "placeholder.png", "description": "Envolva perna adversária entre suas pernas" },
                        { "img": "placeholder.png", "description": "Cruze tornozelos para imobilização" },
                        { "img": "placeholder.png", "description": "Girar quadril para aplicar pressão" }
                    ]
                }
            ]
        }
    ]
}


def populate_database():
    with app.app_context():
        print("Criando tabelas e populando o banco de dados...")
        
        # Opcional: Remova o banco de dados antigo antes de criar um novo
        db_path = os.path.join(app.root_path, 'database.db')
        if os.path.exists(db_path):
            os.remove(db_path)
        
        db.create_all()

        for level, positions in default_data.items():
            for pos_data in positions:
                # Crie o objeto Position
                new_position = Position(
                    name=pos_data["name"],
                    description=pos_data["description"],
                    image=pos_data["image"],
                    level=level
                )
                db.session.add(new_position)
                db.session.commit() # Commit para garantir que o ID da posição seja gerado

                for var_data in pos_data["variations"]:
                    # Crie o objeto Variation
                    new_variation = Variation(
                        name=var_data["name"],
                        description=var_data["description"],
                        position_id=new_position.id
                    )
                    db.session.add(new_variation)
                    db.session.commit() # Commit para garantir que o ID da variação seja gerado

                    for step_data in var_data["steps"]:
                        # Crie o objeto Step
                        new_step = Step(
                            img=step_data["img"],
                            description=step_data["description"],
                            variation_id=new_variation.id
                        )
                        db.session.add(new_step)

        db.session.commit()
        print("Banco de dados populado com sucesso!")

if __name__ == '__main__':
    populate_database()