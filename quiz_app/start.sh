#!/bin/bash
echo "========================================"
echo "Quiz App - Iniciando..."
echo "========================================"
echo ""

# Verificar se venv existe
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
    echo ""
fi

echo "Ativando ambiente virtual..."
source venv/bin/activate

echo "Instalando/atualizando dependências..."
pip install -q -r requirements.txt

echo ""
echo "========================================"
echo "Iniciando aplicação..."
echo "Acesse: http://localhost:5000"
echo "========================================"
echo ""

python app.py

