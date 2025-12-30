#!/usr/bin/env python3
"""Teste rápido do parser"""
import os
import sys
from pathlib import Path
from question_parser import QuestionParser

# Obter diretório raiz
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(f"Diretório base: {base_dir}")
print(f"Testando parser...\n")

parser = QuestionParser(base_dir)
questions_data = parser.load_all_questions()

total_questions = sum(len(q) for q in questions_data.values())
print(f"Total: {total_questions} questoes de {len(questions_data)} topicos\n")

# Mostrar alguns exemplos
print("Primeiros 5 tópicos:")
for i, (topic_path, questions) in enumerate(list(questions_data.items())[:5]):
    topic_name = parser.get_topic_name(topic_path)
    print(f"  {i+1}. {topic_name}: {len(questions)} questões")
    if questions:
        q = questions[0]
        print(f"     Tipo: {q['type']}")
        print(f"     Questão: {q['question'][:60]}...")
        print()

print("✅ Parser funcionando corretamente!")

