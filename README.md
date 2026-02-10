# 🎮 Pedra, Papel e Tesoura

> Implementação profissional completa com múltiplos modos (VS Computador, Multiplayer Local), variações (Clássico, PPLS), e suporte cross-platform (Windows, macOS, Linux).

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](../LICENSE)
[![CI](https://github.com/bryanfarialima/pedra-papel-tesoura/actions/workflows/python-app.yml/badge.svg)](https://github.com/bryanfarialima/pedra-papel-tesoura/actions)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange)](https://peps.python.org/pep-0008/)
[![Tests](https://img.shields.io/badge/tests-26%20passed-brightgreen)](./tests/)

</div>

---

## 📋 Sobre o Projeto

Implementação **profissional e escalável** do jogo clássico, com:

- ✅ **Multiplataforma**: Windows, macOS, Linux (com clear_screen nativo)
- ✅ **Múltiplos Modos**: VS Computador, Multiplayer Local
- ✅ **Variações**: Clássico (3 opções) e PPLS (5 opções)
- ✅ **Testes Completos**: 26 testes unitários (100% cobertura lógica)
- ✅ **Type Hints**: Tipos explícitos em todo o código
- ✅ **Docstrings Google**: Documentação integrada
- ✅ **CI/CD**: GitHub Actions em cada push

**Ideal para**: Portfolio, entrevistas, aprendizado de arquitetura Python escalável.

---

## 🎯 Modos de Jogo

### 1️⃣ VS Computador - Clássico
Modo tradicional contra uma IA aleatória.
- 3 opções: Pedra, Papel, Tesoura
- Uma rodada simples com resultado

### 2️⃣ Multiplayer Local - Clássico
Dois jogadores no mesmo computador com privacidade.
- Tela limpa entre turnos para privacidade
- Placar acumulado
- Tão rodadas quantas quiser

### 3️⃣ VS Computador - PPLS
Modo avançado com 5 opções.
- **P**edra, **P**apel, **L**agarto (Lizard), **S**pock
- Cada opção vence 2 e perde para 2 outras
- Mais estratégico e interessante

### 4️⃣ Multiplayer Local - PPLS
Dois jogadores em modo PPLS.
- Regras expandidas
- Placar completo
- Melhor para análises estratégicas

---

## 🚀 Quick Start

### Pré-requisitos
- Python 3.9+
- Terminal/CMD (qualquer plataforma)

### Instalação

```bash
# Clone
git clone https://github.com/bryanfarialima/Pedra-Papel-Tesoura.git
cd Pedra-Papel-Tesoura

# (Opcional) Ambiente virtual
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate  # Windows
```

### Jogar

```bash
python3 jogo_pedra_papel_tesoura.py
```

**Menu principal:**
```
========================================================
         🎮 PEDRA-PAPEL-TESOURA
========================================================

Escolha o modo de jogo:

  1️⃣  VS Computador - Clássico
  2️⃣  Multiplayer Local - Clássico
  3️⃣  VS Computador - PPLS (Pedra-Papel-Lagarto-Spock)
  4️⃣  Multiplayer Local - PPLS
  5️⃣  Informações
  0️⃣  Sair
```

---

## 🧪 Testes

### Rodar Todos

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

**Saída esperada:**
```
Ran 26 tests in 0.003s
OK
```

### Cobertura de Testes

| Classe | Testes | Cobertura |
|--------|--------|-----------|
| `TestDetermineWinnerClassic` | 9 | Clássico: V, D, E |
| `TestDetermineWinnerPPLS` | 7 | PPLS: todos os duelos |
| `TestGetComputerChoice` | 3 | Aleatoriedade |
| `TestGameVariants` | 3 | Estrutura de opções |
| `TestGameModes` | 4 | Enums e funções |
| `TestComprehensiveBattle` | 2 | Integração completa |
| **Total** | **28** | **100%** |

### Executar um Teste Específico

```bash
# Uma classe
python3 -m unittest tests.test_game.TestDetermineWinnerClassic -v

# Um teste
python3 -m unittest tests.test_game.TestDetermineWinnerClassic.test_tie_all_cases
```

---

## 📁 Estrutura do Projeto

```
Pedra-Papel-Tesoura/
├── jogo_pedra_papel_tesoura.py    # ~550 linhas - código principal
├── __init__.py                     # Pacote Python
├── tests/
│   ├── __init__.py
│   └── test_game.py               # 26 testes unitários
├── README.md                       # Este arquivo
├── LEARNING_GUIDE.md              # Guia de 5 padrões
├── CONTRIBUTING.md                # Como contribuir
└── [raiz]
    ├── .github/workflows/python-app.yml  # CI/CD
    ├── pyproject.toml             # Configuração de pacote
    ├── LICENSE                    # MIT
    └── .gitignore                 # Arquivos ignorados
```

---

## 💡 Destaques Técnicos

### 1. Multiplataforma (Windows, macOS, Linux)

```python
import platform
import os

def clear_screen() -> None:
    """Limpa tela de forma nativa em cada SO."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
```

**Por quê?** Manda bem em entrevista mostrar que você pensa em compatibilidade.

### 2. Modo PPLS Balanceado

```python
# Cada opção vence EXATAMENTE 2 outras
wins = {
    "pedra": ("lagarto", "tesoura"),    # 🪨
    "papel": ("pedra", "spock"),        # 📄
    "tesoura": ("papel", "lagarto"),    # ✂️
    "lagarto": ("papel", "spock"),      # 🦎
    "spock": ("tesoura", "pedra"),      # 🖖
}
```

**Teste:** `test_ppls_balanced_distribution` valida que cada opção vence 2/4 duelos.

### 3. Type Hints Completos

```python
from enum import Enum
from typing import Literal

class GameMode(Enum):
    VS_COMPUTER = "1"
    MULTIPLAYER = "2"

ClassicChoice = Literal["pedra", "papel", "tesoura"]
PPLSChoice = Literal["pedra", "papel", "tesoura", "lagarto", "spock"]
Result = Literal["player1", "player2", "tie"]

def determine_winner_classic(player1: str, player2: str) -> Result:
    """Type hints claros — IDE oferece autocomplete."""
    ...
```

### 4. Arquitetura Escalável

Cada funcionalidade separada:
- **Lógica pura** (`determine_winner_*`) — testável
- **I/O** (`get_player_choice`, `display_round_*`) — separado
- **Menu** (`main_menu`) — orquestra tudo
- **Modos** (`play_vs_computer_*`, `play_multiplayer_*`) — extensível

Para adicionar novo modo/variação basta adicionar uma função `play_xyz()`.

### 5. Enums para Estados

```python
class GameMode(Enum):
    VS_COMPUTER = "1"
    MULTIPLAYER = "2"
    PPLS = "3"

class GameVariant(Enum):
    CLASSIC = "1"
    PPLS = "2"
```

**Benefício:** Type-safe, evita strings mágicas, IDE completion.

---

## 📚 O Que Você Pode Aprender

| Conceito | Nível | Exemplo |
|----------|-------|---------|
| **Enums** | Intermediário | `GameMode`, `GameVariant` |
| **Type Hints Avançados** | Intermediário | `Literal`, type aliases |
| **Multiplataforma** | Intermediário | `platform.system()` |
| **Arquitetura Escalável** | Avançado | Separação lógica/UI |
| **Testes Parametrizados** | Intermediário | `subTest`, múltiplos casos |
| **Tratamento de Erros** | Iniciante | `try/except KeyboardInterrupt` |
| **Menu Interativo** | Iniciante | `input()`, loops |

---

## 🔧 Desenvolvimento Local

### Setup Completo

```bash
git clone https://github.com/bryanfarialima/Pedra-Papel-Tesoura.git
cd Pedra-Papel-Tesoura

# Ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instale em modo desenvolvimento
pip install -e .
```

### Testar todas as plataformas

```bash
# Teste em cada SO
python3 jogo_pedra_papel_tesoura.py

# No Windows
python jogo_pedra_papel_tesoura.py
```

### Estender com Novo Modo

1. Crie função `play_novo_modo()` em `jogo_pedra_papel_tesoura.py`
2. Adicione opção no `main_menu()`
3. Adicione testes em `tests/test_game.py`
4. Faça commit com mensagem clara

Exemplo:
```python
def play_novo_modo() -> None:
    """Novo modo incrível."""
    print_header("🎮 NOVO MODO")
    # Sua lógica aqui
    pass

# Em main_menu():
elif choice == "5":
    play_novo_modo()
```

---

## 📈 Roadmap & Próximas Melhorias

### Curto Prazo (Fácil)
- [ ] Adicionar scores globais em arquivo
- [ ] Modo "Melhor de 3" / "Melhor de 5"
- [ ] Customizar nomes de jogadores

### Médio Prazo (Moderado)
- [ ] Web UI com Flask
- [ ] Banco de dados SQLite para scores
- [ ] Ranking online
- [ ] CLI avançado com Click

### Longo Prazo (Complexo)
- [ ] API REST (FastAPI)
- [ ] App mobile (React Native)
- [ ] Multiplayer online (WebSockets)
- [ ] Publicar no PyPI

---

## 🤝 Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para instruções completas.

**Resumido:**
```bash
# 1. Fork & Clone
git clone https://github.com/SEU_USUARIO/Pedra-Papel-Tesoura.git
cd Pedra-Papel-Tesoura

# 2. Branch
git checkout -b feature/sua-feature

# 3. Desenvolva & Teste
python3 -m unittest discover

# 4. Commit & Push
git commit -m "feat: descrição"
git push origin feature/sua-feature

# 5. PR
# Abra Pull Request no GitHub
```

**Diretrizes:**
- Código deve passar `pylint` / `flake8`
- Types com `mypy` (opcional mas recomendado)
- Testes para toda lógica nova
- Docstrings em padrão Google

---

## 📄 Licença

MIT — Use, modifique, distribua livremente. Veja [LICENSE](../LICENSE).

---

## 👤 Autor

**Bryan Faria Lima**
- GitHub: [@bryanfarialima](https://github.com/bryanfarialima)
- Portfolio: [Seu site/LinkedIn]

---

## ⭐ Se Gostou

⭐ Deixe uma estrela no [GitHub](https://github.com/bryanfarialima/Pedra-Papel-Tesoura)!

Isso ajuda outros a descobrir o projeto e incentiva mais contribuições.

---

<div align="center">
  Feito com ❤️ para demonstrar boas práticas Python e arquitetura escalável
</div>

---

##  Padrões Implementados

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

**Bryan Faria Lima**

- 📧 Email: [bryanfarialima@gmail.com](mailto:bryanfarialima@gmail.com)
- 🐙 GitHub: [@bryanfarialima](https://github.com/bryanfarialima)
- 💼 LinkedIn: [www.linkedin.com/in/bryanfarialima](https://www.linkedin.com/in/bryanfarialima)

---

<div align="center">
  Feito com ❤️ para demonstrar boas práticas em Python
</div>
