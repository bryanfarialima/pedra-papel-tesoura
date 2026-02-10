# Pedra, Papel e Tesoura — Projeto de Exemplo

Este repositório contém uma versão refatorada do jogo "Pedra, Papel e Tesoura" escrita em Python, preparada como exemplo de projeto para seu portfólio.

**O que foi feito**:
- **Refatoração do script**: transformei o código monolítico em funções reutilizáveis (`get_player_choice`, `get_computer_choice`, `determine_winner`, `play_round`, `main`).
- **Tipos e Docstrings**: adicionei anotações de tipo e docstrings para facilitar leitura e testes.
- **Testes unitários**: adicionei testes com `unittest` em `tests/test_game.py`.
- **Pacote Python**: adicionei `__init__.py` para permitir importação em testes.

Estrutura de arquivos relevante:

- `jogo_pedra_papel_tesoura.py`: código refatorado e executável.
- `tests/test_game.py`: testes unitários.

Como rodar localmente

- Executar o jogo (interativo):

```bash
python3 Pedra_Papel_Tesoura/jogo_pedra_papel_tesoura.py
```

- Executar testes:

```bash
python3 -m unittest discover -s Pedra_Papel_Tesoura/tests -p "test_*.py"
```

Guia rápido do que aprender com este padrão

1. Separe lógica e I/O: coloque a lógica (determinar vencedor) em funções sem input/output para facilitar testes.
2. Adicione docstrings e tipos: ajudam editores e revisores a entender o contrato das funções.
3. Torne o pacote importável: um `__init__.py` simples permite executar testes e reutilizar código.
4. Escreva testes pequenos e determinísticos: foque na lógica central primeiro.
5. Prepare um README: descreva as mudanças e como executar — é essencial para repos de portfólio.

Próximos passos sugeridos

- Adicionar CI (GitHub Actions) para rodar testes automaticamente.
- Incluir um `LICENSE` e `setup.py` ou `pyproject.toml` se quiser publicar como pacote.

Se quiser, eu posso criar um workflow de CI e um `pyproject.toml` mínimo para você publicar no PyPI ou facilitar instalação.
