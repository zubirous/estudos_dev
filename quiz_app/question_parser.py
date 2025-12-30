import re
import os
from typing import List, Dict, Optional
from pathlib import Path


class QuestionParser:
    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
    
    def parse_alternativas_file(self, file_path: Path) -> List[Dict]:
        """Parse arquivo de questões de múltipla escolha"""
        questions = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern para questões de múltipla escolha - mais flexível
        pattern = r'## Questão \d+ \(Múltipla Escolha\)\n(.*?)\n\n(.*?)\n\n\*\*Resposta:\*\* (.+?)(?=\n\n---|\n\n##|$)'
        
        matches = re.finditer(pattern, content, re.DOTALL | re.MULTILINE)
        
        for match in matches:
            question_text = match.group(1).strip()
            options_text = match.group(2).strip()
            answer_text = match.group(3).strip()
            
            # Extrair opções
            options = {}
            option_pattern = r'^([a-d])\) (.+)$'
            for line in options_text.split('\n'):
                line = line.strip()
                if line and not line.startswith('**'):
                    opt_match = re.match(option_pattern, line)
                    if opt_match:
                        letter = opt_match.group(1)
                        text = opt_match.group(2).strip()
                        options[letter] = text
            
            # Extrair resposta(s) correta(s) - pode ter múltiplas se contiver "ou"
            answer_matches = re.findall(r'([a-d])\)', answer_text)
            
            # Se houver múltiplas respostas (ex: "b) SSG ou c) ISR"), aceitar todas
            if len(answer_matches) > 1 and ' ou ' in answer_text.lower():
                # Múltiplas respostas corretas
                correct_answers = answer_matches
                # Usar a primeira como principal para compatibilidade
                correct_answer = correct_answers[0]
                # Armazenar todas as respostas corretas na explicação
                explanation = answer_text
            elif answer_matches:
                # Resposta única
                correct_answer = answer_matches[0]
                # Limpar explicação removendo a resposta repetida
                explanation = answer_text
                if explanation.startswith(f"{correct_answer})"):
                    explanation = explanation[len(f"{correct_answer})"):].strip()
                    if explanation.startswith('-'):
                        explanation = explanation[1:].strip()
            else:
                correct_answer = None
                explanation = answer_text
            
            if correct_answer and options:
                questions.append({
                    'type': 'multiple_choice',
                    'question': question_text,
                    'options': options,
                    'correct_answer': correct_answer,
                    'correct_answers': answer_matches if len(answer_matches) > 1 and ' ou ' in answer_text.lower() else None,
                    'explanation': explanation
                })
        
        return questions
    
    def parse_vf_file(self, file_path: Path) -> List[Dict]:
        """Parse arquivo de questões verdadeiro/falso"""
        questions = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern para questões V/F - mais flexível
        pattern = r'## Questão \d+ \(Verdadeiro/Falso\)\n(.*?)\n\n\*\*Resposta:\*\* (.+?)(?=\n\n---|\n\n##|$)'
        
        matches = re.finditer(pattern, content, re.DOTALL | re.MULTILINE)
        
        for match in matches:
            question_text = match.group(1).strip()
            answer_text = match.group(2).strip()
            
            # Determinar se é Verdadeiro ou Falso - verificar início da resposta
            answer_lower = answer_text.lower()
            is_true = answer_lower.startswith('verdadeiro') or 'verdadeiro.' in answer_lower[:20]
            is_false = answer_lower.startswith('falso') or 'falso.' in answer_lower[:20]
            
            correct_answer = None
            if is_true and not is_false:
                correct_answer = 'V'
            elif is_false and not is_true:
                correct_answer = 'F'
            
            if correct_answer:
                questions.append({
                    'type': 'true_false',
                    'question': question_text,
                    'correct_answer': correct_answer,
                    'explanation': answer_text
                })
        
        return questions
    
    def load_all_questions(self) -> Dict[str, List[Dict]]:
        """Carrega todas as questões de todos os tópicos"""
        all_questions = {}
        
        # Diretórios a processar
        directories = ['arquitetura', 'mysql', 'nextjs']
        
        for dir_name in directories:
            dir_path = self.base_dir / dir_name
            if not dir_path.exists():
                continue
            
            # Buscar subdiretórios
            for subdir in dir_path.iterdir():
                if subdir.is_dir():
                    topic_name = f"{dir_name}/{subdir.name}"
                    
                    # Carregar questões de alternativas
                    alt_file = subdir / "PROVA_ALTERNATIVAS.md"
                    vf_file = subdir / "PROVA_VF.md"
                    
                    questions = []
                    
                    if alt_file.exists():
                        questions.extend(self.parse_alternativas_file(alt_file))
                    
                    if vf_file.exists():
                        questions.extend(self.parse_vf_file(vf_file))
                    
                    if questions:
                        all_questions[topic_name] = questions
        
        return all_questions
    
    def get_topic_name(self, topic_path: str) -> str:
        """Extrai nome amigável do tópico"""
        parts = topic_path.split('/')
        if len(parts) >= 2:
            # Remover números do início se existirem
            name = parts[1]
            name = re.sub(r'^\d+_', '', name)
            name = name.replace('_', ' ').title()
            return f"{parts[0].title()}: {name}"
        return topic_path

