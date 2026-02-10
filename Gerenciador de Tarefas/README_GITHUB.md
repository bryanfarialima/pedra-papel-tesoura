# 📱 Gerenciador de Tarefas - Portfólio Júnior

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Sistema profissional de gerenciamento de tarefas em Python com persistência em JSON.

## ✨ Funcionalidades

- ✅ **Adicionar** tarefas com título, descrição, categoria e prioridade
- ✅ **Listar** todas as tarefas ou apenas as pendentes
- ✅ **Concluir** tarefas marcando como finalizada
- ✅ **Editar** tarefas existentes
- ✅ **Remover** tarefas com confirmação
- ✅ **Buscar** tarefas por palavra-chave
- ✅ **Filtrar** por categoria
- ✅ **Estatísticas** gerais (total, concluídas, por prioridade, por categoria)
- ✅ **Persistência** automática em JSON
- ✅ **Logging** profissional de operações

## 🎓 Conceitos Demonstrados

### Programação Orientada a Objetos
- Classe bem estruturada
- Separação de responsabilidades
- Métodos públicos e privados

### Python Moderno
- **Dataclasses** para modelo de dados
- **Type Hints** completos em todos os métodos
- **Optional** para valores nulos
- **List Comprehensions** onde apropriado
- **Generator Expressions** para buscas

### Boas Práticas
- **Logging** profissional com `logging` module
- **Tratamento de Exceções** robusto
- **Persistência de Dados** com JSON
- **Clean Code** com nomes descritivos
- **Docstrings** em Google Style
- **Type Safety** com type hints

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.9+
- Sem dependências externas (usa apenas stdlib)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/gerenciador-tarefas.git
cd gerenciador-tarefas

# Execute o programa
python3 app_tarefas_github.py
```

## 📖 Como Usar

```
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Editar tarefa
5 - Remover tarefa
6 - Buscar tarefas
7 - Filtrar por categoria
8 - Ver estatísticas
9 - Sair
```

### Exemplo de Uso

```bash
$ python3 app_tarefas_github.py

==================================================
📱 GERENCIADOR DE TAREFAS
==================================================
1 - Adicionar
2 - Listar
3 - Concluir
4 - Editar
5 - Remover
6 - Buscar
7 - Filtrar por categoria
8 - Estatísticas
9 - Sair

Escolha: 1

==================================================
➕ ADICIONAR NOVA TAREFA
==================================================
Título: Estudar Type Hints
Descrição: Aprender a usar type hints em Python
Categoria: Estudos
Prioridade: 1-Baixa  2-Média  3-Alta
Escolha: 3
Prazo (DD/MM/YYYY ou vazio): 15/02/2026

✅ Tarefa 'Estudar Type Hints' adicionada com sucesso!
```

## 📁 Estrutura de Arquivos

```
gerenciador-tarefas/
├── app_tarefas_github.py      # Arquivo principal
├── README.md                  # Este arquivo
├── .gitignore                 # Arquivos ignorados pelo Git
├── LICENSE                    # Licença MIT
└── tarefas_app/               # Pasta gerada automaticamente
    └── tarefas.json          # Arquivo de dados (criado automaticamente)
```

## 💾 Persistência de Dados

As tarefas são armazenadas automaticamente em:
```
~/.tarefaas_app/tarefas.json
```

Exemplo de estrutura JSON:
```json
[
  {
    "id": 1,
    "titulo": "Estudar Type Hints",
    "descricao": "Aprender a usar type hints em Python",
    "categoria": "Estudos",
    "prioridade": "Alta",
    "concluida": false,
    "criado_em": "2026-02-09T14:30:45.123456",
    "vencimento": "2026-02-15"
  }
]
```

## 🔧 Desenvolvimento

### Estrutura de Classes

```python
class Tarefa:
    """Modelo de dados para uma tarefa."""
    id: int
    titulo: str
    descricao: str
    categoria: str
    prioridade: str
    concluida: bool
    criado_em: str
    vencimento: Optional[str]

class GerenciadorTarefas:
    """Gerencia todas as operações com tarefas."""
```

### Métodos Principais

| Método | Função |
|--------|--------|
| `adicionar()` | Cria nova tarefa |
| `listar()` | Exibe todas as tarefas |
| `concluir()` | Marca como concluída |
| `editar()` | Modifica tarefa existente |
| `remover()` | Deleta tarefa |
| `buscar()` | Busca por palavra-chave |
| `filtrar_categoria()` | Filtra por categoria |
| `estatisticas()` | Exibe relatório |

## 🏗️ Arquitetura

### Camadas
1. **Modelo (Dataclass)** - `Tarefa`
2. **Lógica de Negócio** - `GerenciadorTarefas`
3. **Persistência** - `_carregar()`, `_salvar()`
4. **Interface** - `menu()`

### Padrões Utilizados
- **CRUD** completo
- **Separação de Responsabilidades**
- **Factory Pattern** (leve) em `from_dict()`
- **Repository Pattern** (leve) em persistência

## 📊 Qualidade de Código

### Métricas
- ✅ 100% Type Hints coverage
- ✅ Docstrings em todos os métodos públicos
- ✅ Logging profissional
- ✅ Tratamento robusto de exceções
- ✅ Validação de entrada

### Validações
- Título obrigatório
- Data em formato correto (DD/MM/YYYY)
- ID deve ser número
- Confirmação antes de deletar

## 🧪 Testando a Aplicação

### Teste Manual
```bash
python3 app_tarefas_github.py

# Siga o menu interativo
```

### Operações para Testar
1. Adicionar 3 tarefas diferentes
2. Listar e verificar ordem (por prioridade)
3. Concluir uma tarefa
4. Editar título e categoria
5. Buscar por termo
6. Filtrar por categoria
7. Ver estatísticas
8. Remover uma tarefa
9. Sair e reabrir (dados devem persistir)

## 📝 Logging

A aplicação registra todas as operações em tempo real:

```
2026-02-09 14:30:45 - __main__ - INFO - Gerenciador iniciado com 0 tarefas
2026-02-09 14:31:02 - __main__ - INFO - Tarefa criada: • [1] Estudar Type Hints (Alta)
2026-02-09 14:31:15 - __main__ - INFO - ✅ 1 tarefas salvas com sucesso
```

Útil para debugging e auditoria.

## 🐛 Troubleshooting

### Dados não salvam
```bash
# Verificar permissão da pasta
ls -la ~/.tarefas_app/

# Se necessário, criar pasta manualmente
mkdir -p ~/.tarefas_app
```

### Erro ao carregar arquivo
```
❌ JSON inválido em ...
```
Delete `~/.tarefas_app/tarefas.json` e reinicie.

## 🚀 Próximas Melhorias

- [ ] Testes unitários com `pytest`
- [ ] Interface web com `Flask` ou `FastAPI`
- [ ] Banco de dados SQLite
- [ ] Notificações para tarefas vencidas
- [ ] Autenticação de usuários
- [ ] Exportação para CSV/PDF
- [ ] API REST

## 📚 Recursos de Aprendizado

- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Dataclasses Documentation](https://docs.python.org/3/library/dataclasses.html)
- [Logging Module](https://docs.python.org/3/library/logging.html)
- [JSON Module](https://docs.python.org/3/library/json.html)

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2026 Bryan Faria Lima

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas! Sinta-se livre para:

1. Fork o projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 👨‍💻 Autor

**Bryan Faria Lima**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [seu-perfil](https://linkedin.com/in/seu-perfil)
- Email: seu-email@example.com

## 🎯 Objetivo

Este projeto foi desenvolvido como demonstração de conhecimentos em Python para entrada em vaga de desenvolvedor Júnior.

### Conceitos Demonstrados
- ✅ POO (Orientação a Objetos)
- ✅ Python Moderno (Dataclasses, Type Hints)
- ✅ Logging Profissional
- ✅ Tratamento de Exceções
- ✅ Persistência de Dados
- ✅ Clean Code
- ✅ Documentação de Código

## ⭐ Feedback

Se você achou este projeto útil, considere dar uma ⭐!

---

**Desenvolvido com ❤️ e ☕**
