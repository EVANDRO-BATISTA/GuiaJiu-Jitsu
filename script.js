// Function to load data from localStorage or use default
function loadPositionsData() {
    const storedData = localStorage.getItem('positionsData');
    if (storedData) {
        return JSON.parse(storedData);
    } else {
        // Default data if nothing in localStorage
        const defaultData = {
            beginner: [
                {
                    name: "Guarda Fechada",
                    description: "Posição fundamental onde você envolve o oponente com as pernas, controlando a distância e prevenindo passes.",
                    image: "beginner_guard.png",
                    variations: [
                        {
                            name: "Guarda Fechada Tradicional",
                            description: "Técnica básica de defesa",
                            steps: [
                                { img: "placeholder.png", description: "Deite-se de costas com pernas ao redor do quadril do oponente" },
                                { img: "placeholder.png", description: "Cruze os tornozelos mantendo os joelhos pressionados" },
                                { img: "placeholder.png", description: "Use mãos para controlar os pulsos ou colar do oponente" }
                            ]
                        },
                        {
                            name: "Guarda com Triângulo",
                            description: "Preparação para finalização",
                            steps: [
                                { img: "placeholder.png", description: "Abra uma perna e passe sobre o ombro do oponente" },
                                { img: "placeholder.png", description: "Cruze o tornozelo sobre o joelho formando triângulo" },
                                { img: "placeholder.png", description: "Puxe a cabeça do oponente para estabilizar a posição" }
                            ]
                        }
                    ]
                },
                {
                    name: "Montada",
                    description: "Posição dominante sentada no torso do oponente, oferecendo controle total e oportunidades de finalização.",
                    image: "beginner_mount.png",
                    variations: [
                        {
                            name: "Montada Alta",
                            description: "Controle máximo com estabilidade",
                            steps: [
                                { img: "placeholder.png", description: "Coloque joelhos junto ao torso do oponente" },
                                { img: "placeholder.png", description: "Pés mantidos abaixo dos joelhos para estabilidade" },
                                { img: "placeholder.png", description: "Mãos controlando os pulsos ou cabeça do adversário" }
                            ]
                        }
                    ]
                },
                {
                    name: "Controle Lateral",
                    description: "Posição lateral de controle onde você imobiliza o oponente entre seu torso e o chão.",
                    image: "beginner_sidecontrol.png",
                    variations: [
                        {
                            name: "Controle com Pompeamento",
                            description: "Imobilização avançada com controle",
                            steps: [
                                { img: "placeholder.png", description: "Posicione o peito pressionando o torso do oponente" },
                                { img: "placeholder.png", description: "Joelho junto ao quadril para bloquear movimentos" },
                                { img: "placeholder.png", description: "Mão controlando o colarinho ou ombro para pressão" }
                            ]
                        }
                    ]
                }
            ],
            intermediate: [
                {
                    name: "Guarda Aberta",
                    description: "Posição com pernas ativas controlando o oponente à distância, permitindo varreduras complexas.",
                    image: "intermediate_openguard.png",
                    variations: [
                        {
                            name: "Guarda Pombo",
                            description: "Transição para chave de pé",
                            steps: [
                                { img: "placeholder.png", description: "Posicione panturrilha em peito do oponente" },
                                { img: "placeholder.png", description: "Pé externo junto ao quadril para controle" },
                                { img: "placeholder.png", description: "Braços seguram calça para limitar mobilidade" }
                            ]
                        }
                    ]
                },
                {
                    name: "Pegada nas Costas",
                    description: "Posição dominante atrás do oponente com ganchos nas pernas, ideal para finalizações.",
                    image: "intermediate_backcontrol.png",
                    variations: [
                        {
                            name: "Cruzamento Lagartixa",
                            description: "Técnica para manter controle",
                            steps: [
                                { img: "placeholder.png", description: "Cruze os pés atrás dos joelhos do oponente" },
                                { img: "placeholder.png", description: "Braço sob o pescoço para controle de cabeça" },
                                { img: "placeholder.png", description: "Mão livre na lombar para apunhalamento" }
                            ]
                        }
                    ]
                },
                {
                    name: "Meia-Guarda",
                    description: "Posição defensiva onde você prende uma perna do oponente, criando oportunidades de escape.",
                    image: "intermediate_halfguard.png",
                    variations: [
                        {
                            name: "Meia-Guarda Profunda",
                            description: "Varreduras eficientes",
                            steps: [
                                { img: "placeholder.png", description: "Deite-se lateralmente prendendo perna adversária" },
                                { img: "placeholder.png", description: "Use joelho para criar ângulo favorável" },
                                { img: "placeholder.png", description: "Braços criam alavanca para rolar" }
                            ]
                        }
                    ]
                }
            ],
            advanced: [
                {
                    name: "Berimbolo",
                    description: "Técnica avançada de inversão que permite assumir a posição nas costas a partir da guarda.",
                    image: "advanced_berimbolo.png",
                    variations: [
                        {
                            name: "Berimbolo Tradicional",
                            description: "Transição rápida para costas",
                            steps: [
                                { img: "placeholder.png", description: "Envolva perna adversária com De La Riva hook" },
                                { img: "placeholder.png", description: "Inverse corpo por baixo do adversário" },
                                { img: "placeholder.png", description: "Use momentum para girar nas costas" }
                            ]
                        }
                    ]
                },
                {
                    name: "Guarda de Borboleta",
                    description: "Posição sentada usando os pés nos quadris para explosões e varreduras.",
                    image: "advanced_butterflyguard.png",
                    variations: [
                        {
                            name: "Varredura Parafinho",
                            description: "Varrendo com técnica precisa",
                            steps: [
                                { img: "placeholder.png", description: "Posicione ambos os pés nos quadris adversários" },
                                { img: "placeholder.png", description: "Braços controlam pulsos ou ombros" },
                                { img: "placeholder.png", description: "Empurre com os pés enquanto levanta quadril" }
                            ]
                        }
                    ]
                },
                {
                    name: "Ashi Garami",
                    description: "Controle avançado de pernas para aplicação de chaves de tornozelo e joelho.",
                    image: "advanced_ashigarami.png",
                    variations: [
                        {
                            name: "Entrada Estilo Japonês",
                            description: "Controle para footlock",
                            steps: [
                                { img: "placeholder.png", description: "Envolva perna adversária entre suas pernas" },
                                { img: "placeholder.png", description: "Cruze tornozelos para imobilização" },
                                { img: "placeholder.png", description: "Girar quadril para aplicar pressão" }
                            ]
                        }
                    ]
                }
            ]
        };
        localStorage.setItem('positionsData', JSON.stringify(defaultData));
        return defaultData;
    }
}

let positionsData = loadPositionsData(); // Initialize at the top

document.addEventListener('DOMContentLoaded', () => {
    let currentLevel = 'beginner';

    const levelButtons = document.querySelectorAll('.level-btn');
    const contentContainer = document.getElementById('content-container');
    const positionDetailContainer = document.getElementById('position-detail-container');
    const backButton = document.querySelector('.back-button');
    let currentPosition = null;
    
    showLevel(currentLevel);
    
    levelButtons.forEach(button => {
        button.addEventListener('click', () => {
            levelButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            showLevel(button.dataset.level);
        });
    });
    
    backButton.addEventListener('click', () => {
        showLevel(currentLevel); // Always go back to the current level overview
    });
    
    function showLevel(level) {
        currentLevel = level;
        positionDetailContainer.style.display = 'none';
        backButton.style.display = 'none';
        contentContainer.style.display = 'block';
        
        // Reload positionsData to ensure latest changes from admin page are reflected
        positionsData = loadPositionsData();

        const positions = positionsData[level];
        
        let html = `
            <h2 class="level-header">Posições para ${level.charAt(0).toUpperCase() + level.slice(1)}</h2>
            <div class="positions-grid">
        `;
        
        if (positions && positions.length > 0) {
            positions.forEach(position => {
                html += `
                    <div class="position-card" data-name="${position.name}">
                        <div class="card-image" style="background-image: url('${position.image}')"></div>
                        <div class="card-content">
                            <h3>${position.name}</h3>
                            <p>${position.description}</p>
                        </div>
                    </div>
                `;
            });
        } else {
            html += `<p style="text-align: center; margin-top: 50px;">Nenhuma posição disponível para este nível ainda. Visite a página de Admin para adicionar!</p>`;
        }
        
        html += `</div>`;
        contentContainer.innerHTML = html;
        
        // Add click event for position cards
        document.querySelectorAll('.position-card').forEach(card => {
            card.addEventListener('click', () => {
                const positionName = card.dataset.name;
                const position = positions.find(p => p.name === positionName);
                if (position) {
                    showPositionDetails(position);
                }
            });
        });
    }
    
    function showPositionDetails(position) {
        backButton.style.display = 'block';
        contentContainer.style.display = 'none';
        positionDetailContainer.style.display = 'block';
        
        let variationsHtml = '';
        if (position.variations && position.variations.length > 0) {
            position.variations.forEach(variation => {
                let stepsHtml = '';
                if (variation.steps && variation.steps.length > 0) {
                    variation.steps.forEach((step, index) => {
                        stepsHtml += `
                            <div class="step-card">
                                <div class="step-number">${index+1}</div>
                                <div class="step-image" style="background-image: url('${step.img}')"></div>
                                <div class="step-description">${step.description}</div>
                            </div>
                        `;
                    });
                } else {
                    stepsHtml = `<p>Nenhum passo detalhado para esta variação.</p>`;
                }
                
                variationsHtml += `
                    <div class="variation-card">
                        <h3>${variation.name}</h3>
                        <p>${variation.description}</p>
                        <div class="steps-container">
                            ${stepsHtml}
                        </div>
                    </div>
                `;
            });
        } else {
            variationsHtml = `<p>Nenhuma variação disponível para esta posição.</p>`;
        }
        
        positionDetailContainer.innerHTML = `
            <div class="position-header">
                <div class="detail-main-image" style="background-image: url('${position.image}')"></div>
                <div class="position-info">
                    <h2>${position.name}</h2>
                    <p>${position.description}</p>
                </div>
            </div>
            <div class="variations-container">
                ${variationsHtml}
            </div>
        `;
    }
});