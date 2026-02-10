#!/bin/bash
# Setup automático para postar no GitHub
# Uso: bash setup_github.sh <seu-usuario-github>

if [ -z "$1" ]; then
    echo "Uso: bash setup_github.sh seu-usuario-github"
    echo "Exemplo: bash setup_github.sh bryanfarialima"
    exit 1
fi

GITHUB_USER=$1
REPO_NAME="gerenciador-tarefas"
REPO_URL="https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

echo "🚀 Setup do Repositório GitHub"
echo "================================"
echo "Usuário: $GITHUB_USER"
echo "Repositório: $REPO_NAME"
echo "URL: $REPO_URL"
echo ""

# Passo 1: Criar diretório
echo "📁 Criando diretório do projeto..."
mkdir -p "$REPO_NAME"
cd "$REPO_NAME"

# Passo 2: Copiar arquivos
echo "📋 Copiando arquivos..."
cp "../app_tarefas_github.py" "main.py"
cp "../README_GITHUB.md" "README.md"
cp "../.gitignore_template" ".gitignore"

# Passo 3: Inicializar git
echo "🔧 Inicializando Git..."
git init
git config user.name "Bryan Faria Lima"
git config user.email "seu-email@gmail.com"

# Passo 4: Primeiro commit
echo "📝 Criando primeiro commit..."
git add .
git commit -m "feat: initial commit - gerenciador de tarefas com dataclass"

# Passo 5: Adicionar remoto
echo "🌐 Adicionando remoto..."
git remote add origin "$REPO_URL"

# Passo 6: Enviar para GitHub
echo "📤 Enviando para GitHub (branch main)..."
git branch -M main
git push -u origin main

echo ""
echo "✅ PRONTO! Seu repositório está no GitHub:"
echo "🔗 $REPO_URL"
echo ""
echo "Próximos passos:"
echo "1. Acesse o link acima para verificar"
echo "2. Compartilhe no LinkedIn"
echo "3. Adicione em seu portfólio"
echo ""
echo "Parabéns! 🎉"
