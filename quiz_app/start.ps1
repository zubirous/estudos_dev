# Script PowerShell para Windows
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Quiz App - Iniciando..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se venv existe
if (-not (Test-Path "venv")) {
    Write-Host "Criando ambiente virtual..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host ""
}

Write-Host "Ativando ambiente virtual..." -ForegroundColor Green
& "venv\Scripts\Activate.ps1"

Write-Host "Instalando/atualizando dependencias..." -ForegroundColor Yellow
pip install -q -r requirements.txt

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Iniciando aplicacao..." -ForegroundColor Cyan
Write-Host "Acesse: http://localhost:5000" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

python app.py

