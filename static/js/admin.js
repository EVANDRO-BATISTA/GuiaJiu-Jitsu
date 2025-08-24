// // Helper functions for localStorage
// function loadPositionsData() {
//     const storedData = localStorage.getItem('positionsData');
//     if (storedData) {
//         return JSON.parse(storedData);
//     }
//     // This case should ideally not happen if script.js loads default data first
//     // but as a fallback, return an empty structure
//     return { beginner: [], intermediate: [], advanced: [] };
// }

// function savePositionsData(data) {
//     localStorage.setItem('positionsData', JSON.stringify(data));
// }

// document.addEventListener('DOMContentLoaded', () => {
//     let currentAdminLevel = 'beginner';
//     const levelButtons = document.querySelectorAll('.level-btn');
//     const addPositionBtn = document.querySelector('.add-position-btn');
//     const adminContentContainer = document.getElementById('admin-content-container');

//     // Initial render
//     renderPositionList(currentAdminLevel);

//     levelButtons.forEach(button => {
//         button.addEventListener('click', () => {
//             levelButtons.forEach(btn => btn.classList.remove('active'));
//             button.classList.add('active');
//             currentAdminLevel = button.dataset.level;
//             renderPositionList(currentAdminLevel);
//         });
//     });

//     addPositionBtn.addEventListener('click', () => {
//         renderPositionForm(currentAdminLevel);
//     });

//     function renderPositionList(level) {
//         const positionsData = loadPositionsData();
//         const positions = positionsData[level] || [];

//         let html = `
//             <h2 class="level-header">Gerenciar Posições para ${level.charAt(0).toUpperCase() + level.slice(1)}</h2>
//             <div class="admin-list">
//         `;

//         if (positions.length > 0) {
//             positions.forEach(position => {
//                 html += `
//                     <div class="admin-position-item">
//                         <span>${position.name}</span>
//                         <div class="admin-position-actions">
//                             <button class="action-btn edit-btn" data-name="${position.name}">Editar</button>
//                             <button class="action-btn delete-btn" data-name="${position.name}">Excluir</button>
//                         </div>
//                     </div>
//                 `;
//             });
//         } else {
//             html += `<p style="text-align: center; margin-top: 50px;">Nenhuma posição adicionada para este nível ainda. Clique em "Adicionar Nova Posição"!</p>`;
//         }
        
//         html += `</div>`;
//         adminContentContainer.innerHTML = html;

//         document.querySelectorAll('.edit-btn').forEach(button => {
//             button.addEventListener('click', (e) => {
//                 const positionName = e.target.dataset.name;
//                 const positionToEdit = positions.find(p => p.name === positionName);
//                 if (positionToEdit) {
//                     renderPositionForm(level, positionToEdit);
//                 }
//             });
//         });

//         document.querySelectorAll('.delete-btn').forEach(button => {
//             button.addEventListener('click', (e) => {
//                 const positionName = e.target.dataset.name;
//                 if (confirm(`Tem certeza que deseja excluir a posição "${positionName}"?`)) {
//                     deletePosition(level, positionName);
//                 }
//             });
//         });
//     }

//     function renderPositionForm(level, position = null) {
//         let isEditing = position !== null;
//         let formTitle = isEditing ? `Editar Posição: ${position.name}` : `Adicionar Nova Posição (${level.charAt(0).toUpperCase() + level.slice(1)})`;

//         let variationsHtml = '';
//         const currentVariations = position ? position.variations : [];

//         currentVariations.forEach((variation, varIndex) => {
//             let stepsHtml = '';
//             variation.steps.forEach((step, stepIndex) => {
//                 stepsHtml += `
//                     <div class="step-form">
//                         <button type="button" class="remove-step-btn" data-var-index="${varIndex}" data-step-index="${stepIndex}">X</button>
//                         <h5>Passo ${stepIndex + 1}</h5>
//                         <div class="admin-form-group">
//                             <label for="step-image-${varIndex}-${stepIndex}">Imagem do Passo (URL/Nome do Arquivo):</label>
//                             <input type="text" id="step-image-${varIndex}-${stepIndex}" name="stepImage" value="${step.img || ''}" placeholder="placeholder.png">
//                         </div>
//                         <div class="admin-form-group">
//                             <label for="step-description-${varIndex}-${stepIndex}">Descrição do Passo:</label>
//                             <textarea id="step-description-${varIndex}-${stepIndex}" name="stepDescription" placeholder="Descrição do passo">${step.description || ''}</textarea>
//                         </div>
//                     </div>
//                 `;
//             });

//             variationsHtml += `
//                 <div class="variation-form" data-index="${varIndex}">
//                     <button type="button" class="remove-variation-btn" data-index="${varIndex}">X</button>
//                     <h4>Variação ${varIndex + 1}</h4>
//                     <div class="admin-form-group">
//                         <label for="variation-name-${varIndex}">Nome da Variação:</label>
//                         <input type="text" id="variation-name-${varIndex}" name="variationName" value="${variation.name || ''}" required>
//                     </div>
//                     <div class="admin-form-group">
//                         <label for="variation-description-${varIndex}">Descrição da Variação:</label>
//                         <textarea id="variation-description-${varIndex}" name="variationDescription" placeholder="Descrição da variação">${variation.description || ''}</textarea>
//                     </div>
//                     <div class="steps-container-form">
//                         ${stepsHtml}
//                     </div>
//                     <button type="button" class="add-step-btn" data-var-index="${varIndex}">Adicionar Passo</button>
//                 </div>
//             `;
//         });

//         adminContentContainer.innerHTML = `
//             <div class="admin-form-container">
//                 <h2>${formTitle}</h2>
//                 <form id="position-form">
//                     <div class="admin-form-group">
//                         <label for="position-name">Nome da Posição:</label>
//                         <input type="text" id="position-name" name="positionName" value="${position ? position.name : ''}" required>
//                     </div>
//                     <div class="admin-form-group">
//                         <label for="position-description">Descrição da Posição:</label>
//                         <textarea id="position-description" name="positionDescription" placeholder="Descrição da posição" required>${position ? position.description : ''}</textarea>
//                     </div>
//                     <div class="admin-form-group">
//                         <label for="position-image">Imagem Principal (URL/Nome do Arquivo):</label>
//                         <input type="text" id="position-image" name="positionImage" value="${position ? position.image : ''}" placeholder="beginner_guard.png" required>
//                     </div>

//                     <h3>Variações</h3>
//                     <div id="variations-container-form">
//                         ${variationsHtml}
//                     </div>
//                     <button type="button" class="add-variation-btn">Adicionar Variação</button>

//                     <div class="form-actions">
//                         <button type="submit" class="save-btn">Salvar Posição</button>
//                         <button type="button" class="cancel-btn">Cancelar</button>
//                     </div>
//                 </form>
//             </div>
//         `;

//         addFormListeners(level, position);
//     }

//     function addFormListeners(level, originalPosition) {
//         const form = document.getElementById('position-form');
//         const variationsContainer = document.getElementById('variations-container-form');

//         // Cancel button
//         document.querySelector('.cancel-btn').addEventListener('click', () => {
//             renderPositionList(level);
//         });

//         // Add Variation button
//         document.querySelector('.add-variation-btn').addEventListener('click', () => {
//             addVariationToForm(variationsContainer);
//         });

//         // Event delegation for dynamically added remove variation/step buttons
//         variationsContainer.addEventListener('click', (e) => {
//             if (e.target.classList.contains('remove-variation-btn')) {
//                 const varDiv = e.target.closest('.variation-form');
//                 if (varDiv) {
//                     varDiv.remove();
//                     updateFormIndices(variationsContainer, '.variation-form', 'variation');
//                 }
//             } else if (e.target.classList.contains('add-step-btn')) {
//                 const varDiv = e.target.closest('.variation-form');
//                 if (varDiv) {
//                     const stepsContainer = varDiv.querySelector('.steps-container-form');
//                     addStepToForm(stepsContainer);
//                 }
//             } else if (e.target.classList.contains('remove-step-btn')) {
//                 const stepDiv = e.target.closest('.step-form');
//                 if (stepDiv) {
//                     stepDiv.remove();
//                     // No need to update step indices, they are relative to their variation
//                     // But if we want to re-number, we could call an updateFormIndices on the stepsContainer
//                 }
//             }
//         });

//         form.addEventListener('submit', (e) => {
//             e.preventDefault();
//             const newPositionData = collectFormData(form);
//             savePosition(level, newPositionData, originalPosition ? originalPosition.name : null);
//         });
//     }

//     function addVariationToForm(container) {
//         const varIndex = container.children.length; // Simple index for new variation
//         const newVariationHtml = `
//             <div class="variation-form" data-index="${varIndex}">
//                 <button type="button" class="remove-variation-btn" data-index="${varIndex}">X</button>
//                 <h4>Nova Variação ${varIndex + 1}</h4>
//                 <div class="admin-form-group">
//                     <label for="variation-name-${varIndex}">Nome da Variação:</label>
//                     <input type="text" id="variation-name-${varIndex}" name="variationName" required>
//                 </div>
//                 <div class="admin-form-group">
//                     <label for="variation-description-${varIndex}">Descrição da Variação:</label>
//                     <textarea id="variation-description-${varIndex}" name="variationDescription" placeholder="Descrição da variação"></textarea>
//                 </div>
//                 <div class="steps-container-form">
//                     <!-- Steps will be added here -->
//                 </div>
//                 <button type="button" class="add-step-btn" data-var-index="${varIndex}">Adicionar Passo</button>
//             </div>
//         `;
//         container.insertAdjacentHTML('beforeend', newVariationHtml);
//     }

//     function addStepToForm(stepsContainer) {
//         const varIndex = stepsContainer.closest('.variation-form').dataset.index;
//         const stepIndex = stepsContainer.children.length; // Simple index for new step
//         const newStepHtml = `
//             <div class="step-form">
//                 <button type="button" class="remove-step-btn" data-var-index="${varIndex}" data-step-index="${stepIndex}">X</button>
//                 <h5>Novo Passo ${stepIndex + 1}</h5>
//                 <div class="admin-form-group">
//                     <label for="step-image-${varIndex}-${stepIndex}">Imagem do Passo (URL/Nome do Arquivo):</label>
//                     <input type="text" id="step-image-${varIndex}-${stepIndex}" name="stepImage" placeholder="placeholder.png">
//                 </div>
//                 <div class="admin-form-group">
//                     <label for="step-description-${varIndex}-${stepIndex}">Descrição do Passo:</label>
//                     <textarea id="step-description-${varIndex}-${stepIndex}" name="stepDescription" placeholder="Descrição do passo"></textarea>
//                 </div>
//             </div>
//         `;
//         stepsContainer.insertAdjacentHTML('beforeend', newStepHtml);
//     }

//     function updateFormIndices(container, selector, type) {
//         Array.from(container.querySelectorAll(selector)).forEach((item, index) => {
//             item.dataset.index = index;
//             if (type === 'variation') {
//                 item.querySelector('h4').textContent = `Variação ${index + 1}`;
//                 item.querySelector('.add-step-btn').dataset.varIndex = index;
//                 item.querySelectorAll('.remove-step-btn').forEach(btn => btn.dataset.varIndex = index);
//                 item.querySelectorAll('[id^="variation-name-"], [id^="variation-description-"]').forEach(input => {
//                     input.id = `${type}-name-${index}`;
//                 });
//                 item.querySelectorAll('[id^="step-image-"], [id^="step-description-"]').forEach(input => {
//                     const oldIdParts = input.id.split('-');
//                     input.id = `step-${oldIdParts[2]}-${index}-${oldIdParts[4]}`; // Re-index var part
//                 });
//             }
//             // For steps, if needed to re-number text, iterate again within each variation.
//             // Currently, step numbers are just based on immediate children count, which is fine.
//         });
//     }

//     function collectFormData(form) {
//         const positionName = form.querySelector('#position-name').value.trim();
//         const positionDescription = form.querySelector('#position-description').value.trim();
//         const positionImage = form.querySelector('#position-image').value.trim();

//         const variations = [];
//         form.querySelectorAll('.variation-form').forEach(varDiv => {
//             const varName = varDiv.querySelector('[name="variationName"]').value.trim();
//             const varDescription = varDiv.querySelector('[name="variationDescription"]').value.trim();

//             const steps = [];
//             varDiv.querySelectorAll('.step-form').forEach(stepDiv => {
//                 const stepImage = stepDiv.querySelector('[name="stepImage"]').value.trim();
//                 const stepDescription = stepDiv.querySelector('[name="stepDescription"]').value.trim();
//                 steps.push({ img: stepImage || 'placeholder.png', description: stepDescription });
//             });
//             variations.push({ name: varName, description: varDescription, steps: steps });
//         });

//         return {
//             name: positionName,
//             description: positionDescription,
//             image: positionImage,
//             variations: variations
//         };
//     }

//     function savePosition(level, newPositionData, originalPositionName = null) {
//         const positionsData = loadPositionsData();
//         let positionsForLevel = positionsData[level];

//         if (originalPositionName) {
//             // Editing existing position
//             const index = positionsForLevel.findIndex(p => p.name === originalPositionName);
//             if (index !== -1) {
//                 positionsForLevel[index] = newPositionData;
//             }
//         } else {
//             // Adding new position
//             // Check for duplicate names for new positions
//             if (positionsForLevel.some(p => p.name === newPositionData.name)) {
//                 alert('Uma posição com este nome já existe para este nível. Por favor, use um nome diferente ou edite a posição existente.');
//                 return;
//             }
//             positionsForLevel.push(newPositionData);
//         }

//         savePositionsData(positionsData);
//         alert('Posição salva com sucesso!');
//         renderPositionList(level); // Go back to the list view
//     }

//     function deletePosition(level, positionName) {
//         const positionsData = loadPositionsData();
//         let positionsForLevel = positionsData[level];
        
//         positionsData[level] = positionsForLevel.filter(p => p.name !== positionName);
//         savePositionsData(positionsData);
//         alert('Posição excluída com sucesso!');
//         renderPositionList(level); // Refresh the list
//     }
// });