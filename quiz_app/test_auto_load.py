#!/usr/bin/env python3
"""Teste para verificar leitura automática de questões"""
import os
from question_parser import QuestionParser

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parser = QuestionParser(base_dir)
questions_data = parser.load_all_questions()

total = sum(len(q) for q in questions_data.values())
print(f"Total de questoes carregadas automaticamente: {total}")
print(f"Topicos encontrados: {len(questions_data)}")
print()

# Exemplo detalhado
example_topic = 'arquitetura/01_ARQUITETURA_VS_PADRAO'
if example_topic in questions_data:
    q_list = questions_data[example_topic]
    multiple = [q for q in q_list if q['type'] == 'multiple_choice']
    vf = [q for q in q_list if q['type'] == 'true_false']
    
    print(f"Exemplo - {example_topic}:")
    print(f"  - Questoes de Alternativas (PROVA_ALTERNATIVAS.md): {len(multiple)}")
    print(f"  - Questoes V/F (PROVA_VF.md): {len(vf)}")
    print(f"  - Total: {len(q_list)}")
    print()
    
    if multiple:
        print(f"  Primeira questao de alternativas:")
        print(f"    Pergunta: {multiple[0]['question'][:50]}...")
        print(f"    Opcoes: {list(multiple[0]['options'].keys())}")
    if vf:
        print(f"  Primeira questao V/F:")
        print(f"    Pergunta: {vf[0]['question'][:50]}...")
        print(f"    Resposta correta: {vf[0]['correct_answer']}")

print()
print("O quiz le automaticamente:")
print("1. Todos os arquivos PROVA_ALTERNATIVAS.md")
print("2. Todos os arquivos PROVA_VF.md")
print("3. De todos os subdiretorios de arquitetura/, mysql/ e nextjs/")
print()
print("Basta adicionar novos arquivos ou editar existentes e reiniciar o app!")

