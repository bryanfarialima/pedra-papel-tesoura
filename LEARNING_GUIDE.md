# 📚 Guia de Aprendizado — Pedra, Papel e Tesoura

Este guia explica as **boas práticas implementadas** neste projeto e como aplicá-las em seus próprios projetos Python.

---

## 🎯 Objetivos de Aprendizado

Após estudar este projeto, você entenderá:
1. Como separar lógica de aplicação (business logic) de I/O
2. Por que type hints melhoram a qualidade do código
3. Como escrever testes unitários sem mocks complexos
4. Como estruturar um projeto Python profissional
5. Como configurar CI/CD com GitHub Actions

---

## 📖 Padrão 1: Separação de Responsabilidades

### O Problema
Código iniciante geralmente mistura tudo:

```python
# ❌ Avoid - código ruim (monolítico)
while True:
    player = input("Escolha: ").lower()
    computer = random.choice(opcoes)
    
    if player == computer:
        print("Empate!")
    elif (player == "pedra" and computer == "tesoura"):
        print("Você venceu!")
    # ... etc
```

**Problemas:**
- Impossível testar sem simular input do usuário
- Lógica acoplada a I/O
- Difícil reutilizar em outras interfaces (Web, API)

### A Solução
Separe **lógica pura** de **I/O**:

```python
# ✅ Bom - funções puras
def determine_winner(jogador: str, computador: str) -> Literal["player", "computer", "tie"]:
    """Apenas lógica, SEM input/output."""
    if jogador == computador:
        return "tie"
    wins = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"}
    return "player" if wins.get(jogador) == computador else "computer"

# ✅ Bom - I/O separado
def get_player_choice() -> Choice:
    """APENAS obter e validar input."""
    while True:
        resposta = input("Escolha: ").strip().lower()
        if resposta in OPTIONS:
            return resposta

# ✅ Bom - orquestração
def play_round(interactive=True, player_choice=None):
    """Combina lógica + I/O."""
    player = player_choice or get_player_choice()
    computer = get_computer_choice()
    return determine_winner(player, computer)
```

### Por Que Funciona
- **Testabilidade**: `determine_winner("pedra", "tesoura")` é testável sem input
- **Reutilizabilidade**: Posso usar `determine_winner` em Web API
- **Clareza**: Cada função tem uma responsabilidade bem definida

### Aplicar em Seus Projetos
```python
# Identifique "pontos de decisão" sem I/O
def calculate_discount(price: float, customer_type: str) -> float:
    """Lógica pura — sem input()."""
    if customer_type == "vip":
        return price * 0.9
    return price

# Separe entrada
def get_price() -> float:
    """Obtém input e valida."""
    while True:
        try:
            return float(input("Preço: "))
        except ValueError:
            print("Digite um número!")

# Use em testes
assert calculate_discount(100, "vip") == 90
```

---

## 📖 Padrão 2: Type Hints (Anotações de Tipo)

### O Problema
Sem tipos, é difícil saber o que uma função espera/retorna:

```python
# ❌ Confuso
def determine_winner(jogador, computador):
    # Qual é o tipo esperado?
    # Pode ser None? Pode ser int?
    ...
```

### A Solução
Adicione anotações de tipo:

```python
from typing import Literal

Choice = Literal["pedra", "papel", "tesoura"]  # Type alias

def determine_winner(jogador: str, computador: str) -> Literal["player", "computer", "tie"]:
    """Tipos indicam contrato da função."""
    ...
```

### Benefícios
1. **IDE oferece autocomplete** melhor
2. **Erros detectados antes de rodar** (com mypy, pylint, Pylance)
3. **Documentação automática** — tipos explicam o código
4. **Refatoração segura** — mudar tipos enquanto desenvolve

### Type Hints Comuns

```python
# Básicos
def greet(name: str) -> str:
    return f"Olá, {name}!"

# Opcionais
def get_user(user_id: int | None = None) -> dict:
    ...

# Coleções
def process_items(items: list[str]) -> dict[str, int]:
    ...

# Union
from typing import Union
def process(value: Union[int, str]) -> float:
    ...

# Type alias (igual ao projeto!)
Choice = Literal["pedra", "papel", "tesoura"]
def validate_choice(c: Choice) -> bool:
    ...
```

### Aplicar em Seus Projetos
```python
# ❌ Antes (sem tipos)
def calculate_age(birth_year):
    return 2026 - birth_year

# ✅ Depois (com tipos)
def calculate_age(birth_year: int) -> int:
    """Calcula idade em 2026."""
    return 2026 - birth_year

# Agora IDE sabe: entrada é int, saída é int
```

---

## 📖 Padrão 3: Docstrings em Padrão Google

### O Problema
Comentários ruins ou inconsistentes:

```python
# ❌ Vago
def determine_winner(jogador, computador):
    # retorna quem venceu
    ...
```

### A Solução
Use docstrings estruturadas:

```python
def determine_winner(jogador: str, computador: str) -> Literal["player", "computer", "tie"]:
    """Determina o vencedor de uma rodada.
    
    Implementa as regras clássicas:
    - Pedra vence Tesoura
    - Tesoura vence Papel
    - Papel vence Pedra
    
    Args:
        jogador: Escolha do jogador ('pedra', 'papel' ou 'tesoura').
        computador: Escolha do computador.
    
    Returns:
        Literal["player", "computer", "tie"]: Resultado.
    
    Example:
        >>> determine_winner("pedra", "tesoura")
        'player'
    """
    ...
```

### Por Quê?
- IDE e `help()` exibem formato bom
- Documentação integrada ao código
- Padrão consistente em toda a equipe
- Geradores de docs (`sphinx`) usam isso

### Aplicar em Seus Projetos
```python
def calculate_tax(amount: float, tax_rate: float = 0.15) -> float:
    """Calcula imposto sobre um valor.
    
    Args:
        amount: Valor base (ex: R$ 100).
        tax_rate: Taxa de imposto (0-1, default 15%).
    
    Returns:
        float: Montante de imposto a pagar.
    
    Example:
        >>> calculate_tax(100, 0.15)
        15.0
    """
    return amount * tax_rate
```

---

## 📖 Padrão 4: Testes Unitários

### O Problema
Testar sem estrutura é caótico:

```python
# ❌ Sem testes — como sabe se funciona?
result = determine_winner("pedra", "tesoura")
if result == "player":
    print("OK")
else:
    print("ERRO")  # Cada vez que roda?
```

### A Solução
Use `unittest` (ou `pytest`):

```python
import unittest
from jogo import determine_winner

class TestDetermineWinner(unittest.TestCase):
    def test_tie(self):
        """Testa empate."""
        result = determine_winner("pedra", "pedra")
        self.assertEqual(result, "tie")
    
    def test_player_wins(self):
        """Testa vitória do jogador."""
        result = determine_winner("pedra", "tesoura")
        self.assertEqual(result, "player")

if __name__ == "__main__":
    unittest.main()  # Roda todos os testes
```

Rodar:
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

### Estrutura de Teste
```
# Arrange (preparar)
player = "pedra"
computer = "tesoura"

# Act (executar)
result = determine_winner(player, computer)

# Assert (validar)
assert result == "player"
```

### Benefícios
- ✅ Valida código automaticamente
- ✅ Detecta regressões (problema que volta)
- ✅ Documenta comportamento esperado
- ✅ Refatoração segura (muded sem medo)

### Aplicar em Seus Projetos
```python
# seu_calculador.py
def sum_positive(numbers: list[int]) -> int:
    """Soma apenas números positivos."""
    return sum(n for n in numbers if n > 0)

# test_seu_calculador.py
import unittest
from seu_calculador import sum_positive

class TestSumPositive(unittest.TestCase):
    def test_all_positive(self):
        result = sum_positive([1, 2, 3])
        self.assertEqual(result, 6)
    
    def test_mixed(self):
        result = sum_positive([1, -2, 3])
        self.assertEqual(result, 4)
    
    def test_empty(self):
        result = sum_positive([])
        self.assertEqual(result, 0)

unittest.main()
```

---

## 📖 Padrão 5: Estrutura de Projeto Profissional

### Arquivos Essenciais

```
seu_projeto/
├── seu_modulo/              # ← sua lógica (pode ser diretório ou .py)
│   ├── __init__.py          # Torna essa pasta um pacote Python
│   ├── main.py              # Lógica principal
│   └── utils.py             # Funções auxiliares
├── tests/
│   ├── __init__.py
│   └── test_main.py         # Testes para main.py
├── README.md                # Documentação principal
├── LICENSE                  # Licença (MIT, Apache, etc.)
├── .gitignore               # Arquivos ignorados no Git
├── pyproject.toml           # Configuração de pacote e dependências
└── .github/
    └── workflows/
        └── python-app.yml   # CI/CD (GitHub Actions)
```

### `pyproject.toml` — Por Quê?
Define como instalar/empacotar seu projeto:

```toml
[project]
name = "meu-projeto"
version = "0.1.0"
description = "Projeto exemplo"
requires-python = ">=3.9"
dependencies = []  # pip install -e .

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

Depois você instala:
```bash
pip install -e .
```

### `.gitignore` — Por Quê?
Evita commitar arquivos desnecessários:

```
__pycache__/
*.pyc
.venv/
venv/
build/
dist/
*.egg-info/
.DS_Store
```

### `LICENSE` — Por Quê?
Define permissões de uso:
- **MIT**: Qualquer um usa, muda, vende — você não é responsável
- **Apache 2.0**: Parecido, mais formal
- **GPL**: Quem usa precisa publicar também

### CI/CD (`.github/workflows/`)
Roda testes automaticamente em repositório:

```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
      - name: Run tests
        run: python3 -m unittest discover
```

**Benefício:** Garante que código sempre está "verde" (testes passam).

---

## 🔗 Checklist — Aplicar em Seu Projeto

- [ ] Separe lógica pura de I/O
- [ ] Adicione type hints em tudo
- [ ] Escreva docstrings Google para funções públicas
- [ ] Crie `tests/test_*.py` para toda lógica
- [ ] Organize: `seu_modulo/`, `tests/`, `README.md`, `LICENSE`, `.gitignore`
- [ ] Adicione `pyproject.toml` com seu projeto
- [ ] Configure CI/CD (GitHub Actions ou outra)
- [ ] Rode `python3 -m unittest discover` antes de commitar

---

## 🚀 Próximos Passos

1. **Linting & Formatting**
   ```bash
   pip install black flake8 pylint
   black seu_modulo/          # Formata código
   flake8 seu_modulo/         # Verifica problemas estilo
   ```

2. **Type Checking**
   ```bash
   pip install mypy
   mypy seu_modulo/            # Valida tipos
   ```

3. **Code Coverage**
   ```bash
   pip install coverage
   coverage run -m unittest discover
   coverage report
   ```

4. **Documentação Automática**
   ```bash
   pip install sphinx
   sphinx-quickstart docs/
   make html
   ```

---

## 📚 Referências

- [PEP 8 — Style Guide for Python](https://peps.python.org/pep-0008/)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [Type Hints — Python Typing](https://docs.python.org/3/library/typing.html)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

## 💡 Perguntas Frequentes

**P: Por que não usar `pytest` em vez de `unittest`?**
R: `unittest` é padrão (vem com Python). `pytest` é mais moderno e popular em novos projetos. Ambas são válidas.

**P: Quando adicionar type hints?**
R: Sempre! Mesmo que comece o projeto, adicione tipos. Previne bugs e melhora documentação.

**P: Preciso de 100% de testes?**
R: Ideal 80-90%. Foque em lógica crítica e edge cases.

**P: Como organizar testes em projetos grandes?**
R: Espelhe a estrutura do projeto:
```
src/
  auth/
    __init__.py
    login.py
  database/
    __init__.py
    models.py
tests/
  auth/
    test_login.py
  database/
    test_models.py
```

---

<div align="center">
  ✨ Boas práticas geram código melhor, mais seguro e fácil de manter ✨
</div>
