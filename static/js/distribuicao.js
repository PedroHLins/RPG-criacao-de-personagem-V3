document.addEventListener('DOMContentLoaded', () => {

    const attributeButtons = document.querySelectorAll('.attribute-btn');
    const valueButtons = document.querySelectorAll('.value-btn');
    const finalSubmitButton = document.getElementById('submit-final');

    let selectedAttribute = null;
    let selectedValue = null;
    let assignedCount = 0;

    attributeButtons.forEach(button => {
        button.addEventListener('click', () => {
            attributeButtons.forEach(btn => btn.classList.remove('selected'));
            button.classList.add('selected');
            selectedAttribute = button;
            tryToAssign();
        });
    });

    valueButtons.forEach(button => {
        button.addEventListener('click', () => {
            valueButtons.forEach(btn => btn.classList.remove('selected'));
            button.classList.add('selected');
            selectedValue = button;
            tryToAssign();
        });
    });

    function tryToAssign() {
        if (selectedAttribute && selectedValue) {
            const attributeName = selectedAttribute.dataset.attribute;
            const value = selectedValue.textContent;
            const hiddenInput = document.getElementById(`attr-${attributeName}`);
            hiddenInput.value = value;
            selectedAttribute.disabled = true;
            selectedValue.disabled = true;
            selectedAttribute.classList.remove('selected');
            selectedValue.classList.remove('selected');
            selectedAttribute = null;
            selectedValue = null;
            assignedCount++;

            if (assignedCount === 6) {
                finalSubmitButton.disabled = false;
                finalSubmitButton.textContent = "Ver Ficha do Personagem!";
            }
        }
    }
});