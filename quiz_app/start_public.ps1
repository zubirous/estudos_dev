# Script para iniciar Flask e ngrok automaticamente
# Requer: ngrok.exe no PATH ou na mesma pasta

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Quiz App - Modo Publico (ngrok)" -ForegroundColor Cyan
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
Write-Host "INSTRUCOES:" -ForegroundColor Yellow
Write-Host "1. Este script vai iniciar o Flask" -ForegroundColor White
Write-Host "2. Em OUTRO terminal, execute: ngrok http 5000" -ForegroundColor White
Write-Host "3. Copie o link HTTPS do ngrok e compartilhe!" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se ngrok está disponível
$ngrokPath = Get-Command ngrok -ErrorAction SilentlyContinue
if ($ngrokPath) {
    Write-Host "ngrok encontrado! Iniciando Flask e ngrok..." -ForegroundColor Green
    Write-Host ""
    
    # Iniciar Flask em background
    $flaskJob = Start-Job -ScriptBlock {
        Set-Location $using:PWD
        & "venv\Scripts\python.exe" app.py
    }
    
    Start-Sleep -Seconds 3
    
    # Iniciar ngrok
    Write-Host "Iniciando ngrok..." -ForegroundColor Green
    Write-Host "Seu link publico aparecera abaixo:" -ForegroundColor Yellow
    Write-Host ""
    
    ngrok http 5000
    
    # Parar Flask quando ngrok parar
    Stop-Job $flaskJob
    Remove-Job $flaskJob
} else {
    Write-Host "ngrok nao encontrado no PATH." -ForegroundColor Red
    Write-Host ""
    Write-Host "Opcoes:" -ForegroundColor Yellow
    Write-Host "1. Instale ngrok: https://ngrok.com/download" -ForegroundColor White
    Write-Host "2. Adicione ao PATH ou coloque ngrok.exe nesta pasta" -ForegroundColor White
    Write-Host "3. Ou inicie manualmente em outro terminal: ngrok http 5000" -ForegroundColor White
    Write-Host ""
    Write-Host "Iniciando apenas Flask..." -ForegroundColor Yellow
    Write-Host "Em outro terminal, execute: ngrok http 5000" -ForegroundColor Cyan
    Write-Host ""
    
    python app.py
}

