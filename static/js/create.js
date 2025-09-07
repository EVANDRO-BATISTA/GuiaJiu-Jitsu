        let variationCount = 1;
        function addVariation() {
            variationCount++;
            const variationsContainer = document.getElementById('variations_container');
            
            const newVariationHtml = `
                <hr>
                <h3>Variação ${variationCount}</h3>
                <label for="variation_name_${variationCount}">Nome da Variação:</label>
                <input type="text" id="variation_name_${variationCount}" name="variation_name[]" required><br><br>
                
                <label for="variation_desc_${variationCount}">Descrição da Variação:</label><br>
                <textarea id="variation_desc_${variationCount}" name="variation_desc[]" rows="4" cols="50" required></textarea><br><br>

                <div class="steps_container" id="steps_container_${variationCount}">
                    <h4>Passo 1</h4>
                    <label for="step_img_${variationCount}_1">URL da Imagem do Passo:</label>
                    <input type="text" id="step_img_${variationCount}_1" name="step_img_${variationCount}[]"><br><br>
                    
                    <label for="step_desc_${variationCount}_1">Descrição do Passo:</label><br>
                    <textarea id="step_desc_${variationCount}_1" name="step_desc_${variationCount}[]" rows="4" cols="50" required></textarea><br><br>
                </div>
                <button class="add-variation-btn" type="button" onclick="addStep(${variationCount})">Adicionar Outro Passo</button>
            `;
            
            variationsContainer.insertAdjacentHTML('beforeend', newVariationHtml);
        }

        let stepCounts = {1: 1};
        function addStep(variationId) {
            if (!stepCounts[variationId]) {
                stepCounts[variationId] = 1;
            }
            stepCounts[variationId]++;
            const stepsContainer = document.getElementById(`steps_container_${variationId}`);

            const newStepHtml = `
                <hr>
                <h4>Passo ${stepCounts[variationId]}</h4>
                <label for="step_img_${variationId}_${stepCounts[variationId]}">URL da Imagem do Passo:</label>
                <input type="text" id="step_img_${variationId}_${stepCounts[variationId]}" name="step_img_${variationId}[]"><br><br>
                
                <label for="step_desc_${variationId}_${stepCounts[variationId]}">Descrição do Passo:</label><br>
                <textarea id="step_desc_${variationId}_${stepCounts[variationId]}" name="step_desc_${variationId}[]" rows="4" cols="50" required></textarea><br><br>
            `;

            stepsContainer.insertAdjacentHTML('beforeend', newStepHtml);
        }


//Mensagem de Sucesso
document.addEventListener('DOMContentLoaded', function() {
    const popupContainer = document.getElementById('popup-container');
    
    // Verifique se há mensagens de flash para mostrar o pop-up
    const hasMessages = document.querySelector('.message-container .alert-success');
    if (hasMessages) {
        popupContainer.style.display = 'flex';
    }

    // Fecha o pop-up ao clicar no botão de fechar
    const closeBtn = document.querySelector('.popup-content .close-btn');
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            popupContainer.style.display = 'none';
        });
    }

    // Fecha o pop-up ao clicar fora do conteúdo dele
    popupContainer.addEventListener('click', function(event) {
        if (event.target === popupContainer) {
            popupContainer.style.display = 'none';
        }
    });
});