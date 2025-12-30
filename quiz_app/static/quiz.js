let currentIndex = 0;
let totalQuestions = 0;
let currentQuestion = null;
let selectedAnswer = null;

// Carregar primeira questão
document.addEventListener('DOMContentLoaded', () => {
    loadQuestion(0);
});

async function loadQuestion(index) {
    try {
        const response = await fetch(`/api/question/${index}`);
        const data = await response.json();
        
        if (data.error) {
            alert(data.error);
            return;
        }
        
        currentQuestion = data.question;
        currentIndex = data.index;
        totalQuestions = data.total;
        
        updateProgress();
        renderQuestion();
    } catch (error) {
        console.error('Erro ao carregar questão:', error);
        alert('Erro ao carregar questão');
    }
}

function updateProgress() {
    const progress = ((currentIndex + 1) / totalQuestions) * 100;
    document.getElementById('progress-fill').style.width = progress + '%';
    document.getElementById('progress-text').textContent = 
        `Questão ${currentIndex + 1} de ${totalQuestions}`;
}

function renderQuestion() {
    const questionText = document.getElementById('question-text');
    const optionsContainer = document.getElementById('options-container');
    const btnSubmit = document.getElementById('btn-submit');
    const btnNext = document.getElementById('btn-next');
    const btnFinish = document.getElementById('btn-finish');
    const feedback = document.getElementById('feedback');
    
    // Reset
    selectedAnswer = null;
    btnSubmit.disabled = true;
    btnNext.style.display = 'none';
    btnFinish.style.display = 'none';
    feedback.style.display = 'none';
    
    questionText.textContent = currentQuestion.question;
    
    // Renderizar opções
    optionsContainer.innerHTML = '';
    
    if (currentQuestion.type === 'multiple_choice') {
        const options = ['a', 'b', 'c', 'd'];
        options.forEach(letter => {
            if (currentQuestion.options[letter]) {
                const optionDiv = document.createElement('div');
                optionDiv.className = 'option';
                optionDiv.innerHTML = `
                    <input type="radio" name="answer" id="opt-${letter}" value="${letter}">
                    <label for="opt-${letter}" class="option-label">${letter}) ${currentQuestion.options[letter]}</label>
                `;
                
                optionDiv.addEventListener('click', () => {
                    document.getElementById(`opt-${letter}`).checked = true;
                    selectedAnswer = letter;
                    btnSubmit.disabled = false;
                    updateOptionSelection();
                });
                
                optionsContainer.appendChild(optionDiv);
            }
        });
    } else if (currentQuestion.type === 'true_false') {
        const options = [
            { value: 'V', label: 'Verdadeiro' },
            { value: 'F', label: 'Falso' }
        ];
        
        options.forEach(opt => {
            const optionDiv = document.createElement('div');
            optionDiv.className = 'option';
            optionDiv.innerHTML = `
                <input type="radio" name="answer" id="opt-${opt.value}" value="${opt.value}">
                <label for="opt-${opt.value}" class="option-label">${opt.label}</label>
            `;
            
            optionDiv.addEventListener('click', () => {
                document.getElementById(`opt-${opt.value}`).checked = true;
                selectedAnswer = opt.value;
                btnSubmit.disabled = false;
                updateOptionSelection();
            });
            
            optionsContainer.appendChild(optionDiv);
        });
    }
    
    // Event listener para radio buttons
    document.querySelectorAll('input[name="answer"]').forEach(radio => {
        radio.addEventListener('change', (e) => {
            selectedAnswer = e.target.value;
            btnSubmit.disabled = false;
            updateOptionSelection();
        });
    });
}

function updateOptionSelection() {
    document.querySelectorAll('.option').forEach(opt => {
        opt.classList.remove('selected');
    });
    
    if (selectedAnswer) {
        const selectedOpt = document.querySelector(`input[value="${selectedAnswer}"]`);
        if (selectedOpt) {
            selectedOpt.closest('.option').classList.add('selected');
        }
    }
}

document.getElementById('btn-submit').addEventListener('click', async () => {
    if (!selectedAnswer) return;
    
    try {
        const response = await fetch('/api/answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                index: currentIndex,
                answer: selectedAnswer
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            alert(data.error);
            return;
        }
        
        // Mostrar feedback
        const feedback = document.getElementById('feedback');
        feedback.style.display = 'block';
        
        if (data.is_correct) {
            feedback.className = 'feedback correct';
            feedback.textContent = '✅ Correto! ' + data.explanation;
        } else {
            feedback.className = 'feedback incorrect';
            let correctLabel;
            if (currentQuestion.type === 'multiple_choice') {
                // Verificar se há múltiplas respostas (formato "b) ou c)")
                if (data.correct_answer.includes(' ou ')) {
                    // Extrair todas as letras das respostas corretas
                    const matches = data.correct_answer.match(/([a-d])\)/g);
                    if (matches) {
                        const labels = matches.map(m => {
                            const letter = m[0];
                            return `${letter}) ${currentQuestion.options[letter]}`;
                        });
                        correctLabel = labels.join(' ou ');
                    } else {
                        correctLabel = data.correct_answer;
                    }
                } else {
                    // Resposta única
                    const letter = data.correct_answer[0];
                    correctLabel = `${letter}) ${currentQuestion.options[letter]}`;
                }
            } else {
                correctLabel = (data.correct_answer === 'V' ? 'Verdadeiro' : 'Falso');
            }
            feedback.textContent = `❌ Incorreto! A resposta correta é: ${correctLabel}. ${data.explanation}`;
        }
        
        // Desabilitar opções
        document.querySelectorAll('.option').forEach(opt => {
            opt.style.pointerEvents = 'none';
        });
        
        document.getElementById('btn-submit').disabled = true;
        
        // Mostrar próximo botão
        if (currentIndex < totalQuestions - 1) {
            document.getElementById('btn-next').style.display = 'inline-block';
        } else {
            document.getElementById('btn-finish').style.display = 'inline-block';
        }
    } catch (error) {
        console.error('Erro ao submeter resposta:', error);
        alert('Erro ao submeter resposta');
    }
});

document.getElementById('btn-next').addEventListener('click', () => {
    loadQuestion(currentIndex + 1);
});

document.getElementById('btn-finish').addEventListener('click', () => {
    window.location.href = '/results';
});

