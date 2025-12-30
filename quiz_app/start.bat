@echo off
echo ========================================
echo Quiz App - Iniciando...
echo ========================================
echo.

REM Verificar se venv existe
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
    echo.
)

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Instalando/atualizando dependencias...
pip install -q -r requirements.txt

echo.
echo ========================================
echo Iniciando aplicacao...
echo Acesse: http://localhost:5000
echo ========================================
echo.

python app.py

pause

