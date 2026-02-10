# 🎮 Pedra, Papel e Tesoura

> Uma implementação profissional do clássico jogo em Python com testes unitários, CI/CD e documentação completa. Ideal para portfólio, entrevistas e aprendizado de boas práticas.

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![CI](https://github.com/bryanfarialima/Pedra-Papel-Tesoura/actions/workflows/python-app.yml/badge.svg)](https://github.com/bryanfarialima/Pedra-Papel-Tesoura/actions)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange)](https://peps.python.org/pep-0008/)

</div>

---

## 📋 Sobre o Projeto

Um projeto de **demonstração de boas práticas em Python**, com foco em:

- ✅ **Clean Code**: separação de responsabilidades, funções puras e testáveis
- ✅ **Type Hints**: anotações de tipo completas para melhor IDE support
- ✅ **Unit Tests**: cobertura de testes com `unittest` (8 testes)
- ✅ **CI/CD**: integração contínua com GitHub Actions
- ✅ **Documentação**: docstrings em padrão Google e README completo
- ✅ **Versionamento**: estrutura profissional com `.gitignore`, `LICENSE`, `pyproject.toml`

---

## 🎯 Funcionalidades

- **Jogo interativo**: CLI com validação robusta de entrada
- **Lógica desacoplada**: funções puras facilitam testes
- **Modo testável**: parâmetros opcionais para execução sem input
- **Tratamento de erros**: catch de `KeyboardInterrupt` e `EOFError`
- **Extensível**: fácil adicionar novos modos ou variações

---

## 🚀 Quick Start

### Pré-requisitos
- Python 3.9+
- pip ou conda

### Instalação

```bash
git clone https://github.com/bryanfarialima/Pedra-Papel-Tesoura.git
cd Pedra-Papel-Tesoura

# Ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate  # Windows
```

### Jogar

```bash
python3 jogo_pedra_papel_tesoura.py
```

**Saída esperada:**
```
Escolha pedra, papel ou tesoura: pedra
Você escolheu pedra
Computador escolheu tesoura
Você venceu!
Jogar novamente? (s/n): n
Obrigado por jogar!
```

---

## 🧪 Testes

```bash
# Rodar todos os testes
python3 -m unittest discover -s tests -p "test_*.py" -v
```

**Cobertura:**
- ✅ Empate (3 casos)
- ✅ Vitória do jogador (3 casos)
- ✅ Vitória do computador (3 casos)

Total: **8 testes unitários**, todos passando ✓

---

## 📁 Estrutura do Projeto

```
Pedra_Papel_Tesoura/
├── jogo_pedra_papel_tesoura.py    # Código principal (65 linhas)
├── __init__.py                     # Torna pacote Python
├── tests/
│   └── test_game.py               # 8 testes unitários
└── README.md                       # Este arquivo
```

Arquivos na raiz:
- `.github/workflows/python-app.yml` — CI/CD com GitHub Actions
- `pyproject.toml` — Configuração de pacote e dependências
- `LICENSE` — Licença MIT
- `.gitignore` — Arquivos ignorados no Git

---

## 💡 Padrões Implementados

### 1. Separação de Responsabilidades

Cada função tem uma responsabilidade clara:

```python
# Funções puras (sem I/O) → testáveis
def determine_winner(jogador: str, computador: str) -> Literal["player", "computer", "tie"]:
    """Lógica pura sem dependências externas."""
    wins = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"}
    if jogador == computador:
        return "tie"
    return "player" if wins.get(jogador) == computador else "computer"

# Funções de I/O separadas
def get_player_choice() -> Choice:
    """Obtém entrada do usuário (pode ser mockada)."""
    while True:
        resposta = input("Escolha pedra, papel ou tesoura: ").strip().lower()
        if resposta in OPTIONS:
            return resposta
        print("Opção inválida!")
```

**Por que:** Código reutilizável, testável e fácil de manter.

### 2. Type Hints Completos

```python
from typing import Literal

Choice = Literal["pedra", "papel", "tesoura"]

def determine_winner(jogador: str, computador: str) -> Literal["player", "computer", "tie"]:
    ...
```

**Benefício:** IDE oferece autocomplete e detecção de erros antes de rodar.

### 3. Docstrings em Padrão Google

```python
def determine_winner(jogador: str, computador: str) -> Literal["player", "computer", "tie"]:
    """Determina o vencedor de uma rodada.

    Retorna 'player' se o jogador vence, 'computer' se o computador vence
    e 'tie' em caso de empate.
    """
```

### 4. Testes Unitários

```python
class TestDetermineWinner(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(game.determine_winner("pedra", "pedra"), "tie")
    
    def test_player_wins(self):
        self.assertEqual(game.determine_winner("pedra", "tesoura"), "player")
```

### 5. CI/CD Automatizado

Workflow em `.github/workflows/python-app.yml` executa:
- ✅ Testes em Python 3.9, 3.10, 3.11
- ✅ Valida em cada push
- ✅ Falha se testes não passarem

---

## 📚 Conceitos Cobertos

| Conceito | Local |
|----------|-------|
| Functions | `def determine_winner(...)` |
| Type Hints | `Literal["pedra", "papel", "tesoura"]` |
| Docstrings | Padrão Google em todas | 
| Dicts | `wins = {"pedra": "tesoura", ...}` |
| Conditionals | `if/elif/else` |
| Loops | `while True` |
| Exception Handling | `try/except KeyboardInterrupt` |
| Unit Tests | `unittest.TestCase` |
| Packaging | `pyproject.toml` |
| CI/CD | GitHub Actions |

---

## 🔧 Desenvolvimento Local

### Setup

```bash
git clone https://github.com/bryanfarialima/Pedra-Papel-Tesoura.git
cd Pedra-Papel-Tesoura

python3 -m venv venv
source venv/bin/activate

# Modo editable (útil para desenvolvimento)
pip install -e .
```

### Testes

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

---

## 🤝 Contribuindo

1. Fork o repositório
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

**Diretrizes:** PEP 8, adicione testes, atualize README.

---

## 📈 Próximas Melhorias

- [ ] Modo multiplayer local (jogador vs jogador)
- [ ] Variação: Pedra-Papel-Tesoura-Lagarto-Spock
- [ ] Estatísticas da sessão
- [ ] Publicar no PyPI
- [ ] Web UI com Flask/FastAPI
- [ ] Linting com pylint
- [ ] Type checking com mypy

---

## 📄 Licença

MIT — Veja [LICENSE](../LICENSE)

---

## 👤 Autor

**Bryan Faria Lima** - [@bryanfarialima](https://github.com/bryanfarialima)

---

<div align="center">
  Feito com ❤️ para demonstrar boas práticas em Python
</div>
