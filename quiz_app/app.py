from flask import Flask, render_template, request, jsonify, session
import random
import json
import re
import markdown
from pathlib import Path
from question_parser import QuestionParser

app = Flask(__name__)
app.secret_key = 'quiz-secret-key-change-in-production'

# Carregar questões
import os
# Obter diretório raiz do projeto (um nível acima de quiz_app)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parser = QuestionParser(base_dir)
questions_data = parser.load_all_questions()

# Debug: mostrar quantas questões foram carregadas
print(f"Carregadas {sum(len(q) for q in questions_data.values())} questões de {len(questions_data)} tópicos")

@app.route('/')
def index():
    """Página inicial - seleção de temas"""
    # Agrupar por tema
    themes = {
        'arquitetura': {
            'name': 'Arquitetura',
            'icon': '🏗️',
            'modules': {}
        },
        'mysql': {
            'name': 'MySQL',
            'icon': '🗄️',
            'modules': {}
        },
        'nextjs': {
            'name': 'Next.js',
            'icon': '⚡',
            'modules': {}
        }
    }
    
    for topic_path, questions in questions_data.items():
        parts = topic_path.split('/')
        if len(parts) >= 2:
            theme = parts[0].lower()
            module_path = parts[1]
            
            if theme in themes:
                module_name = parser.get_topic_name(topic_path)
                # Criar nome curto removendo números e prefixos
                short_name = module_path
                # Remover número no início (ex: 01_CONCEITOS_BASICOS -> CONCEITOS_BASICOS)
                short_name = re.sub(r'^\d+_', '', short_name)
                # Substituir underscores por espaços e capitalizar
                short_name = short_name.replace('_', ' ').title()
                
                # Extrair número para ordenação
                order_match = re.match(r'^(\d+)_', module_path)
                order_num = int(order_match.group(1)) if order_match else 999
                
                themes[theme]['modules'][topic_path] = {
                    'name': module_name,
                    'short_name': short_name,
                    'count': len(questions),
                    'order': order_num,
                    'order_num': order_num  # Número para exibição
                }
    
    # Ordenar módulos por ordem numérica
    for theme_key in themes:
        modules = themes[theme_key]['modules']
        themes[theme_key]['modules'] = dict(sorted(modules.items(), key=lambda x: x[1]['order']))
    
    return render_template('index.html', themes=themes)

@app.route('/quiz/<path:topic_path>')
def quiz(topic_path):
    """Página do quiz"""
    # Normalizar o caminho (remover espaços, etc)
    topic_path = topic_path.strip()
    
    if topic_path not in questions_data:
        # Tentar encontrar similar
        similar = [k for k in questions_data.keys() if topic_path.lower() in k.lower() or k.lower() in topic_path.lower()]
        if similar:
            return f"Tópico não encontrado: {topic_path}. Tente: {similar[0]}", 404
        return render_template('error.html', 
                             error="Tópico não encontrado",
                             message=f"O tópico '{topic_path}' não foi encontrado. Volte à página inicial e selecione um tópico válido."), 404
    
    questions = questions_data[topic_path].copy()
    random.shuffle(questions)
    
    # Salvar questões na sessão
    session['questions'] = json.dumps(questions)
    session['topic'] = topic_path
    session['current_index'] = 0
    session['answers'] = json.dumps([])
    session['score'] = 0
    
    topic_name = parser.get_topic_name(topic_path)
    return render_template('quiz.html', topic_name=topic_name, total=len(questions))

@app.route('/api/question/<int:index>')
def get_question(index):
    """API para obter questão específica"""
    questions = json.loads(session.get('questions', '[]'))
    
    if index < 0 or index >= len(questions):
        return jsonify({'error': 'Questão não encontrada'}), 404
    
    question = questions[index].copy()
    # Remover resposta correta antes de enviar
    if question['type'] == 'multiple_choice':
        correct = question.pop('correct_answer')
        question['_correct'] = correct  # Guardar separadamente
    elif question['type'] == 'true_false':
        correct = question.pop('correct_answer')
        question['_correct'] = correct
    
    return jsonify({
        'question': question,
        'total': len(questions),
        'index': index
    })

@app.route('/api/answer', methods=['POST'])
def submit_answer():
    """API para submeter resposta"""
    data = request.json
    question_index = data.get('index')
    answer = data.get('answer')
    
    questions = json.loads(session.get('questions', '[]'))
    answers = json.loads(session.get('answers', '[]'))
    
    # Verificar se já respondeu esta questão
    already_answered = any(a.get('question_index') == question_index for a in answers)
    if already_answered:
        # Atualizar resposta existente
        for a in answers:
            if a.get('question_index') == question_index:
                old_correct = a.get('is_correct', False)
                question = questions[question_index]
                correct_answer = question['correct_answer']
                # Verificar se há múltiplas respostas corretas
                if 'correct_answers' in question and question['correct_answers']:
                    is_correct = answer in question['correct_answers']
                else:
                    is_correct = answer == correct_answer
                
                a['answer'] = answer
                a['is_correct'] = is_correct
                
                # Atualizar score
                score = session.get('score', 0)
                if old_correct and not is_correct:
                    score -= 1
                elif not old_correct and is_correct:
                    score += 1
                session['score'] = score
                break
    else:
        # Nova resposta
        if question_index < 0 or question_index >= len(questions):
            return jsonify({'error': 'Questão não encontrada'}), 404
        
        question = questions[question_index]
        correct_answer = question['correct_answer']
        # Verificar se há múltiplas respostas corretas
        if 'correct_answers' in question and question['correct_answers']:
            is_correct = answer in question['correct_answers']
        else:
            is_correct = answer == correct_answer
        
        score = session.get('score', 0)
        if is_correct:
            score += 1
        
        # Salvar resposta
        answers.append({
            'question_index': question_index,
            'answer': answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct,
            'question': question['question'],
            'explanation': question.get('explanation', '')
        })
        
        session['score'] = score
    
    session['answers'] = json.dumps(answers)
    
    question = questions[question_index]
    
    # Obter is_correct atualizado
    if already_answered:
        for a in answers:
            if a.get('question_index') == question_index:
                is_correct = a.get('is_correct', False)
                break
    else:
        # Verificar se há múltiplas respostas corretas
        if 'correct_answers' in question and question['correct_answers']:
            is_correct = answer in question['correct_answers']
        else:
            is_correct = answer == question['correct_answer']
    
    # Formatar resposta correta para exibição
    if 'correct_answers' in question and question['correct_answers']:
        correct_answer_display = ' ou '.join([f"{ans})" for ans in question['correct_answers']])
    else:
        correct_answer_display = f"{question['correct_answer']})"
    
    return jsonify({
        'is_correct': is_correct,
        'correct_answer': correct_answer_display,
        'explanation': question.get('explanation', ''),
        'score': session.get('score', 0),
        'total': len(questions)
    })

@app.route('/results')
def results():
    """Página de resultados"""
    answers = json.loads(session.get('answers', '[]'))
    score = session.get('score', 0)
    topic_path = session.get('topic', '')
    questions = json.loads(session.get('questions', '[]'))
    
    topic_name = parser.get_topic_name(topic_path)
    total = len(questions)
    percentage = (score / total * 100) if total > 0 else 0
    
    # Adicionar opções das questões nas respostas para facilitar exibição
    for answer in answers:
        q_index = answer.get('question_index', 0)
        if q_index < len(questions):
            question = questions[q_index]
            answer['question_data'] = question
    
    return render_template('results.html', 
                         answers=answers, 
                         score=score, 
                         total=total,
                         percentage=percentage,
                         topic_name=topic_name,
                         questions=questions)

@app.route('/study/<path:topic_path>')
def study(topic_path):
    """Página para visualizar estudos (README.md)"""
    topic_path = topic_path.strip()
    
    # Construir caminho do arquivo README.md
    parts = topic_path.split('/')
    if len(parts) < 2:
        return render_template('error.html', 
                             error="Tópico inválido",
                             message=f"O caminho '{topic_path}' é inválido."), 404
    
    readme_path = Path(base_dir) / parts[0] / parts[1] / 'README.md'
    
    if not readme_path.exists():
        return render_template('error.html', 
                             error="Arquivo não encontrado",
                             message=f"O arquivo de estudos para '{topic_path}' não foi encontrado."), 404
    
    # Ler e converter markdown para HTML
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        html_content = markdown.markdown(
            markdown_content,
            extensions=['fenced_code', 'tables', 'nl2br']
        )
    except Exception as e:
        return render_template('error.html', 
                             error="Erro ao ler arquivo",
                             message=f"Erro ao processar o arquivo: {str(e)}"), 500
    
    topic_name = parser.get_topic_name(topic_path)
    
    return render_template('study.html', 
                         topic_name=topic_name,
                         topic_path=topic_path,
                         content=html_content)

if __name__ == '__main__':
    # Permitir acesso externo quando usar ngrok ou outros túneis
    # Para produção, use host='0.0.0.0' apenas se necessário
    app.run(debug=True, port=5000, host='127.0.0.1')

