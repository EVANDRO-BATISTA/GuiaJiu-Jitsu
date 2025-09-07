document.addEventListener('DOMContentLoaded', function() {
    const variationsContainer = document.getElementById('variations-container');
    const addVariationBtn = document.getElementById('add-variation-btn');

    // Funções para criar os cards
    function createStepCard(variationIdx) {
        const stepCard = document.createElement('div');
        stepCard.classList.add('step-card');
        stepCard.innerHTML = `
            <div class="form-group">
                <label>URL da Imagem do Passo (Opcional):</label>
                <input type="text" class="form-control" name="step_img_${variationIdx}[]">
            </div>
            <div class="form-group">
                <label>Descrição do Passo:</label>
                <textarea class="form-control" name="step_desc_${variationIdx}[]" rows="2" required></textarea>
            </div>
            <button type="button" class="btn btn-danger btn-sm remove-step-btn">Remover Passo</button>
        `;
        return stepCard;
    }

    function createVariationCard(variationIdx) {
        const newVariationCard = document.createElement('div');
        newVariationCard.classList.add('variation-card');
        newVariationCard.innerHTML = `
            <div class="form-group">
                <label>Nome da Variação:</label>
                <input type="text" class="form-control" name="variation_name[]" required>
            </div>
            <div class="form-group">
                <label>Descrição da Variação:</label>
                <textarea class="form-control" name="variation_desc[]" rows="2" required></textarea>
            </div>
            <h4>Passos para a Nova Variação</h4>
            <div class="steps-container"></div>
            <button type="button" class="btn btn-info btn-sm add-step-btn">Adicionar Passo</button>
            <button type="button" class="btn btn-danger btn-sm remove-variation-btn">Remover Variação</button>
        `;
        
        // Adiciona um passo inicial
        const stepsContainer = newVariationCard.querySelector('.steps-container');
        stepsContainer.appendChild(createStepCard(variationIdx));
        
        return newVariationCard;
    }

    // Função para reindexar todos os campos de entrada após uma remoção
    function reindexFields() {
        const variationCards = document.querySelectorAll('.variation-card');
        variationCards.forEach((card, index) => {
            const newIndex = index + 1;
            
            // Atualiza os nomes dos campos de variação
            card.querySelector('input[name="variation_name[]"]').name = `variation_name_${newIndex}[]`;
            card.querySelector('textarea[name="variation_desc[]"]').name = `variation_desc_${newIndex}[]`;
            
            // Atualiza os nomes dos campos de passo
            const stepInputs = card.querySelectorAll('.steps-container input, .steps-container textarea');
            stepInputs.forEach(input => {
                const oldName = input.name;
                const newName = oldName.replace(/_\d+\[\]/, `_${newIndex}[]`);
                input.name = newName;
            });
        });
    }

    // Delegação de eventos
    variationsContainer.addEventListener('click', function(event) {
        const target = event.target;
        
        if (target.classList.contains('add-step-btn')) {
            const variationCard = target.closest('.variation-card');
            const stepsContainer = variationCard.querySelector('.steps-container');
            const variationIndex = Array.from(variationsContainer.children).indexOf(variationCard) + 1;
            stepsContainer.appendChild(createStepCard(variationIndex));
        } 
        else if (target.classList.contains('remove-step-btn')) {
            target.closest('.step-card').remove();
        } 
        else if (target.classList.contains('remove-variation-btn')) {
            target.closest('.variation-card').remove();
            reindexFields(); // Chama a função para reajustar os índices
        }
    });

    // Evento para o botão de Adicionar Variação
    addVariationBtn.addEventListener('click', function() {
        const newIndex = variationsContainer.children.length + 1;
        variationsContainer.appendChild(createVariationCard(newIndex));
    });
});