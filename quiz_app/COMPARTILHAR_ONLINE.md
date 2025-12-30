# 🌐 Como Compartilhar o Quiz Online

## Opção 1: ngrok (Mais Rápido - Recomendado)

### Passo a Passo:

1. **Baixe o ngrok:**
   - Acesse: https://ngrok.com/download
   - Baixe para Windows
   - Extraia o arquivo `ngrok.exe`

2. **Crie uma conta gratuita:**
   - Acesse: https://dashboard.ngrok.com/signup
   - É gratuito e rápido

3. **Configure o token (apenas primeira vez):**
   ```powershell
   # No PowerShell, navegue até onde está o ngrok.exe
   .\ngrok.exe config add-authtoken SEU_TOKEN_AQUI
   ```
   -- Exemplo: ngrok config add-authtoken 35XMgIblKAEhL20Bo8yRhwM2Nct_2sDSb2GCn7ZTnyBTqa6CQ
   *(O token você encontra em: https://dashboard.ngrok.com/get-started/your-authtoken)*

4. **Inicie o Flask (em um terminal):**
   ```powershell
   cd quiz_app
   python app.py
   ```

5. **Inicie o ngrok (em outro terminal):**
   ```powershell
   # Navegue até onde está o ngrok.exe
   .\ngrok.exe http 5000
   ```

6. **Compartilhe o link:**
   - O ngrok vai mostrar algo como: `https://abc123.ngrok-free.app`
   - **Esse é o link que você compartilha!**
   - Funciona mesmo se você fechar o terminal (mas precisa manter o Flask rodando)

### ⚠️ Importante:
- O link muda toda vez que você reinicia o ngrok (na versão gratuita)
- Mantenha o Flask rodando enquanto quiser compartilhar
- O ngrok gratuito tem limite de conexões simultâneas

---

## Opção 2: Cloudflare Tunnel (Alternativa Gratuita)

1. **Instale cloudflared:**
   - Baixe: https://github.com/cloudflare/cloudflared/releases
   - Extraia `cloudflared.exe`

2. **Execute:**
   ```powershell
   .\cloudflared.exe tunnel --url http://localhost:5000
   ```

3. **Compartilhe o link gerado**

---

## Opção 3: Deploy Permanente (Railway/Render)

### Railway (Recomendado - Grátis):
1. Acesse: https://railway.app
2. Conecte seu GitHub
3. Crie novo projeto
4. Adicione arquivo `Procfile`:
   ```
   web: python app.py
   ```
5. Configure variáveis se necessário
6. Deploy automático!

### Render (Alternativa):
1. Acesse: https://render.com
2. Conecte GitHub
3. Crie novo Web Service
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
5. Deploy!

---

## Script Automático (ngrok)

Use o script `start_public.ps1` para iniciar Flask + ngrok automaticamente!

