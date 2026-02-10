#!/bin/bash
# Script para executar verificações de qualidade localmente
# Uso: chmod +x quality-check.sh && ./quality-check.sh

set -e

echo "🔍 Iniciando verificação de qualidade..."
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 1. Black formatting check
echo -e "${YELLOW}1️⃣  Verificando formatação com Black...${NC}"
if command -v black &> /dev/null; then
    black --check --diff Pedra_Papel_Tesoura/ || echo "⚠️  Problemas de formatação encontrados"
else
    echo "⚠️  Black não instalado. Execute: pip install black"
fi
echo ""

# 2. Flake8 linting
echo -e "${YELLOW}2️⃣  Executando Flake8...${NC}"
if command -v flake8 &> /dev/null; then
    flake8 Pedra_Papel_Tesoura/ --count --statistics || echo "⚠️  Problemas de estilo encontrados"
else
    echo "⚠️  Flake8 não instalado. Execute: pip install flake8"
fi
echo ""

# 3. Run tests
echo -e "${YELLOW}3️⃣  Executando testes...${NC}"
if command -v pytest &> /dev/null; then
    pytest Pedra_Papel_Tesoura/tests/ -v
else
    echo "🔄 Usando unittest..."
    python3 -m unittest discover -s Pedra_Papel_Tesoura/tests -p "test_*.py" -v
fi
echo ""

# 4. Coverage report
echo -e "${YELLOW}4️⃣  Gerando relatório de cobertura...${NC}"
if command -v pytest &> /dev/null; then
    pytest Pedra_Papel_Tesoura/tests/ --cov=Pedra_Papel_Tesoura --cov-report=term-missing --cov-report=html
    echo -e "${GREEN}✅ Relatório HTML gerado em: htmlcov/index.html${NC}"
else
    echo "⚠️  Pytest não instalado. Execute: pip install pytest pytest-cov"
fi
echo ""

echo -e "${GREEN}✅ Verificação de qualidade concluída!${NC}"
