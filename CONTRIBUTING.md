# 🤝 Contribuindo para o Projeto

Obrigado por querer contribuir! Este documento descreve como fazer isso de forma eficaz.

## 🎯 Antes de Começar

- Leia o [README.md](README.md) para entender o projeto
- Consulte [LEARNING_GUIDE.md](LEARNING_GUIDE.md) para entender nossos padrões
- Verifique se há [Issues](https://github.com/bryanfarialima/Pedra-Papel-Tesoura/issues) abertas

## 🐛 Reportar Bugs

1. Verifique se o bug já foi reportado
2. Abra uma [Issue](https://github.com/bryanfarialima/Pedra-Papel-Tesoura/issues/new)
3. Descreva:
   - Versão do Python
   - Passos para reproduzir
   - Comportamento esperado vs real
   - Screenshots (se aplicável)

**Exemplo:**
```
Título: Crash ao inserir caracteres especiais

Versão Python: 3.10
Passos:
1. Rodar jogo_pedra_papel_tesoura.py
2. Digitar "pédra" (com acento)
3. Programa falha com KeyError

Esperado: Rejeitar e pedir nova entrada
```

## ✨ Sugerir Melhorias (Features)

1. Abra uma [Issue](https://github.com/bryanfarialima/Pedra-Papel-Tesoura/issues) com rótulo `enhancement`
2. Descreva:
   - Problema que resolve
   - Solução proposta
   - Exemplos de uso

## 🔧 Como Contribuir com Código

### 1. Fork & Clone

```bash
# Fork no GitHub (clique botão Fork)
git clone https://github.com/SEU_USUARIO/Pedra-Papel-Tesoura.git
cd Pedra-Papel-Tesoura
```

### 2. Crie uma Branch

```bash
# Sempre crie branch a partir de main
git checkout -b feature/sua-feature
# ou
git checkout -b fix/seu-bug
```

**Convenção de nomenclatura:**
- `feature/nome-descritivo` — para novas funcionalidades
- `fix/nome-descritivo` — para correções de bugs
- `docs/nome` — para atualizações de documentação
- `refactor/nome` — para refatorações

### 3. Desenvolva

```bash
# Ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Faça suas mudanças
# Rode testes frequentemente
python3 -m unittest discover -s tests -p "test_*.py" -v
```

### 4. Commit com Mensagens Claras

```bash
# Mensagem clara de commit
git commit -m "feat: adicionar modo multiplayer local"
git commit -m "fix: validação de entrada com acentos"
git commit -m "docs: expandir seção de testes"
```

**Padrão (Conventional Commits):**
- `feat:` — nova funcionalidade
- `fix:` — correção de bug
- `docs:` — documentação
- `refactor:` — reorganização sem mudar comportamento
- `test:` — testes
- `chore:` — manutenção

### 5. Push & Pull Request

```bash
# Upload da sua branch
git push -u origin feature/sua-feature

# Depois abra PR no GitHub (interface web)
```

**No PR, descreva:**
- Qual problema resolve
- Como foi testado
- Screenshots (se UI)

## ✅ Checklist Antes de Submeter

- [ ] Código segue [PEP 8](https://peps.python.org/pep-0008/)
- [ ] Adicionou testes para o novo código
- [ ] Todos os testes passam: `python3 -m unittest discover`
- [ ] Trabalho original (sem copiar sem atribuição)
- [ ] Documentação atualizada (docstrings, README, etc.)
- [ ] Nenhum erro de tipo (com mypy opcionalmente)

## 🎓 Padrões de Código

### Type Hints

```python
# ✅ Sempre adicione tipos
def calculate(value: float) -> float:
    return value * 2

# ❌ Evite sem tipos
def calculate(value):
    return value * 2
```

### Docstrings

```python
def minha_funcao(param: str) -> int:
    """Descrição breve de uma linha.
    
    Descrição mais longa se necessário. Explique por que existe,
    não como funciona (o código explica como).
    
    Args:
        param: Descrição do parâmetro.
    
    Returns:
        int: O que retorna.
    
    Example:
        >>> minha_funcao("teste")
        5
    """
    return len(param)
```

### Testes

```python
import unittest

class TestMeuCodigoNovo(unittest.TestCase):
    def test_caso_sucesso(self):
        """Testa comportamento esperado."""
        result = funcao_nova("input")
        self.assertEqual(result, "esperado")
    
    def test_caso_erro(self):
        """Testa comportamento com erro."""
        with self.assertRaises(ValueError):
            funcao_nova(None)
```

## 🔍 Revisão de Código

- Seremos respeitosos e construtivos
- Pedidos podem ser feitos para:
  - Melhorar legibilidade
  - Adicionar testes
  - Alinhar com padrões
- Discussão é bem-vinda!

## 🚀 Exemplo Completo

```bash
# 1. Fork & clone
git clone https://github.com/SEU_USUARIO/Pedra-Papel-Tesoura.git
cd Pedra-Papel-Tesoura

# 2. Setup
python3 -m venv venv && source venv/bin/activate
pip install -e .

# 3. Crie branch
git checkout -b feature/estatisticas

# 4. Desenvolva com TDD
# Escreva teste → implementação → passe teste
cat > tests/test_stats.py << 'EOF'
import unittest
from jogo import GameStats

class TestGameStats(unittest.TestCase):
    def test_track_wins(self):
        stats = GameStats()
        stats.add_win("player")
        self.assertEqual(stats.wins["player"], 1)
EOF

python3 -m unittest tests.test_stats -v  # Falha (esperado)

# Implemente em jogo_pedra_papel_tesoura.py
# ...

python3 -m unittest tests.test_stats -v  # Passa!

# 5. Commit
git add .
git commit -m "feat: adicionar rastreamento de estatísticas"

# 6. Push & PR
git push origin feature/estatisticas
# Abra PR no GitHub web
```

## 📜 Licença & Atribuição

Por contribuir, você concorda que:
- Seu código será licenciado sob MIT (veja [LICENSE](../LICENSE))
- Seu nome pode aparecer em `CONTRIBUTORS.md` (se quiser)

## ❓ Dúvidas?

- Abra uma [Discussion](https://github.com/bryanfarialima/Pedra-Papel-Tesoura/discussions)
- Comente em uma [Issue](https://github.com/bryanfarialima/Pedra-Papel-Tesoura/issues)

---

<div align="center">
  Obrigado por contribuir! 🎉
</div>
