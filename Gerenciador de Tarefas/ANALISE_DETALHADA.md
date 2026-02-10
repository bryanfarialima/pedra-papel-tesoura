# 🔍 ANÁLISE DETALHADA DO CÓDIGO

## Explicação linha por linha do app_tarefas_completo.py

---

## 📌 SEÇÃO 1: IMPORTAÇÕES

```python
from pathlib import Path
from datetime import datetime, timedelta
import json
import os
```

**O que cada uma faz:**

```python
from pathlib import Path
# → Permite trabalhar com caminhos de forma segura e multiplataforma
# Exemplo: Path.home() retorna /Users/seu_usuario
# Melhor que usar strings com "/" ou "\"
```

```python
from datetime import datetime, timedelta
# → datetime: para trabalhar com datas e horas
#   datetime.now() = agora
# → timedelta: para adicionar/subtrair tempo
#   datetime.now() + timedelta(days=7) = daqui 7 dias
```

```python
import json
# → Para salvar e carregar dados em formato JSON
# json.dump() = escrever em arquivo
# json.load() = ler de arquivo
```

```python
import os
# → Para operações do sistema (limpar tela, etc)
# os.system("clear") = limpa tela no Mac/Linux
```

---

## 📌 SEÇÃO 2: CLASSE PRINCIPAL

```python
class GerenciadorTarefas:
    """
    Classe que gerencia todas as operações com tarefas.
    Organiza o código em métodos bem definidos (boas práticas).
    """
```

**Por que usar classe?**
- Agrupa dados (tarefas) com funções (métodos)
- Mais organizado que código solto
- Reutilizável
- Fácil de entender

---

## 📌 SEÇÃO 3: INICIALIZAÇÃO

```python
def __init__(self):
    # Criar pasta e arquivo de dados
    self.pasta = Path.home() / "tarefas_app"
    self.pasta.mkdir(exist_ok=True)
```

**Explicação:**
```
Path.home()        → /Users/bryanfarialima
        /          → operador para concatenar caminhos
        "tarefas_app" → pasta a criar
exist_ok=True      → não dá erro se já existe
```

```python
    self.arquivo = self.pasta / "tarefas.json"
```

**Cria o caminho:** `/Users/bryanfarialima/tarefas_app/tarefas.json`

```python
    self.prioridades = {"1": "Baixa", "2": "Média", "3": "Alta"}
```

**Dicionário (chave: valor):**
- Chave `"1"` → Valor `"Baixa"`
- Permite mapear entrada do usuário para prioridade real

```python
    self.cores = {
        "Baixa": "\033[92m",      # Verde
        "Média": "\033[93m",      # Amarelo
        "Alta": "\033[91m",       # Vermelho
        "reset": "\033[0m"        # Normal
    }
```

**Códigos ANSI:**
- `\033[92m` = começa cor verde
- `\033[0m` = reseta para normal
- Uso: `f"{cores['Alta']}TEXTO{cores['reset']}"`

```python
    self.tarefas = self.carregar_tarefas()
```

**Executa método para carregar tarefas existentes**

---

## 📌 SEÇÃO 4: CARREGAR TAREFAS

```python
def carregar_tarefas(self):
    """Carrega tarefas do arquivo JSON"""
    if self.arquivo.exists():
```

**Verifica se arquivo existe antes de ler**

```python
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
```

**Analisa:**
- `with open(...) as f:` = abre e fecha automaticamente
- `"r"` = modo leitura
- `encoding="utf-8"` = suporta caracteres especiais (português)
- `json.load(f)` = converte JSON para lista/dicionário Python
- `except` = se JSON está mal formatado, retorna lista vazia

---

## 📌 SEÇÃO 5: SALVAR TAREFAS

```python
def salvar_tarefas(self):
    """Salva tarefas no arquivo JSON"""
    with open(self.arquivo, "w", encoding="utf-8") as f:
        json.dump(self.tarefas, f, ensure_ascii=False, indent=2)
```

**Explicação:**
- `"w"` = modo escrita (cria/sobrescreve arquivo)
- `json.dump()` = converte Python para JSON e salva
- `ensure_ascii=False` = permite acentos (português)
- `indent=2` = formata com 2 espaços (fica legível)

---

## 📌 SEÇÃO 6: ADICIONAR TAREFA

```python
def adicionar_tarefa(self):
    """Adiciona uma nova tarefa com todos os detalhes"""
    
    titulo = input("Título da tarefa: ").strip()
```

**`.strip()`** = remove espaços antes e depois

```python
    if not titulo:
        print("❌ Título não pode ser vazio!")
        return
```

**`if not`** = "se não existe"  
**`return`** = sai da função aqui

```python
    tarefa = {
        "id": len(self.tarefas) + 1,
        "titulo": titulo,
        "concluida": False,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
```

**Dictionary (dicionário):**
- Chave "id" → Valor `len(self.tarefas) + 1`
  - `len()` = conta quantas tarefas existem
  - `+1` = próximo ID
- `datetime.now()` = data/hora atual
- `.strftime()` = formata para string legível

```python
    self.tarefas.append(tarefa)
    self.salvar_tarefas()
```

- `append()` = adiciona ao final da lista
- `salvar_tarefas()` = chama método para persistir

---

## 📌 SEÇÃO 7: LISTAR TAREFAS

```python
def listar_tarefas(self, filtro=None):
    """Lista tarefas com opções de filtro."""
    
    if not self.tarefas:
        print("\n❌ Nenhuma tarefa cadastrada.")
        return
```

- `if not self.tarefas` = se lista vazia
- `return` = sai da função

```python
    tarefas_filtradas = self.tarefas.copy()
```

- `.copy()` = cria cópia (não modifica original)

```python
    if filtro == "pendentes":
        tarefas_filtradas = [t for t in tarefas_filtradas if not t["concluida"]]
```

**List Comprehension:**
```
[novo_item for item in lista if condicao]
```

Quebrado:
```python
# Versão longa
tarefas_filtradas = []
for t in tarefas_filtradas:
    if not t["concluida"]:
        tarefas_filtradas.append(t)

# Versão curta (list comprehension)
tarefas_filtradas = [t for t in tarefas_filtradas if not t["concluida"]]
```

```python
    tarefas_filtradas.sort(
        key=lambda x: (-ordem_prioridade.get(x["prioridade"], 0), x["id"])
    )
```

**Lambda e sort:**
- `lambda x:` = função sem nome, recebe `x`
- `ordem_prioridade.get(...)` = busca com valor padrão 0
- `-ordem_prioridade` = negativo para ordem inversa (Alta primeiro)
- Ordena por tupla: primeiro por prioridade, depois por ID

---

## 📌 SEÇÃO 8: MARCAR CONCLUÍDA

```python
def marcar_concluida(self):
    """Marca uma tarefa como concluída"""
    
    tarefa_id = int(input("\nID da tarefa: "))
    tarefa = next((t for t in self.tarefas if t["id"] == tarefa_id), None)
```

**`next()` explicado:**
```python
# Localiza primeiro item que atende condição
next(
    (t for t in self.tarefas if t["id"] == tarefa_id),  # gerador
    None  # valor padrão se não encontrar
)
```

Quebrado:
```python
tarefa = None
for t in self.tarefas:
    if t["id"] == tarefa_id:
        tarefa = t
        break
```

```python
    if tarefa:
        tarefa["concluida"] = True
        self.salvar_tarefas()
```

- Modifica o dicionário diretamente
- Salva arquivo

---

## 📌 SEÇÃO 9: BUSCAR TAREFAS

```python
def buscar_tarefas(self):
    """Busca tarefas por palavra-chave"""
    
    termo = input("\nBuscar por: ").lower().strip()
```

- `.lower()` = converte para minúsculas (case-insensitive)

```python
    encontradas = [
        t for t in self.tarefas
        if termo in t["titulo"].lower() or termo in t["categoria"].lower()
    ]
```

- `in` = verifica se substring existe
- `termo in titulo.lower()` = "python" in "Estudar PYTHON Classes"

---

## 📌 SEÇÃO 10: FILTRAR POR CATEGORIA

```python
def filtrar_por_categoria(self):
    """Filtra tarefas por categoria"""
    
    categorias = sorted(set(t["categoria"] for t in self.tarefas))
```

**Quebrado:**
```python
# Passo 1: Extrair todas as categorias
categorias_lista = [t["categoria"] for t in self.tarefas]
# Resultado: ['Trabalho', 'Pessoal', 'Trabalho', 'Compras', 'Pessoal']

# Passo 2: Remover duplicatas com set()
categorias_unicas = set(categorias_lista)
# Resultado: {'Trabalho', 'Pessoal', 'Compras'}

# Passo 3: Ordenar
categorias = sorted(categorias_unicas)
# Resultado: ['Compras', 'Pessoal', 'Trabalho']
```

---

## 📌 SEÇÃO 11: ESTATÍSTICAS

```python
def estatisticas(self):
    """Exibe estatísticas das tarefas"""
    
    total = len(self.tarefas)
    concluidas = len([t for t in self.tarefas if t["concluida"]])
    pendentes = total - concluidas
```

- `len()` = conta itens
- List comprehension para contar com filtro

```python
    print(f"Concluídas: {concluidas} ({(concluidas/total*100):.1f}%)")
```

**F-string avançada:**
```python
(concluidas/total*100)  # calcula percentual
:.1f                    # formata com 1 decimal
```

---

## 📌 SEÇÃO 12: MENU PRINCIPAL

```python
def menu_principal(self):
    """Exibe menu e aguarda entrada do usuário"""
    while True:
        self._limpar_tela()
        print("...")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            self.adicionar_tarefa()
        elif opcao == "2":
            self.listar_tarefas()
        # ... mais opções
        elif opcao == "10":
            break
```

**Loop infinito:**
- `while True` = loop que nunca termina
- `break` = sai do loop
- `elif` = else if (outras condições)

---

## 📌 SEÇÃO 13: EXECUÇÃO

```python
if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    gerenciador.menu_principal()
```

**Por quê `if __name__ == "__main__"`?**

Permite que arquivo seja:
1. **Executado diretamente:** Roda o código
2. **Importado:** Não roda o código, só carrega a classe

```python
# Se executar diretamente
$ python3 app.py
# → Roda menu_principal()

# Se importar em outro arquivo
$ python3
>>> from app import GerenciadorTarefas
>>> g = GerenciadorTarefas()  # Criar manualmente
```

---

## 🎯 RESUMO DOS CONCEITOS

| Conceito | Uso | Exemplo |
|----------|-----|---------|
| **Classes** | Organizar código | `class GerenciadorTarefas` |
| **Métodos** | Funções da classe | `def adicionar_tarefa(self)` |
| **Dicionários** | Estrutura com chaves | `{"id": 1, "titulo": "..."}` |
| **Listas** | Coleção ordenada | `[tarefa1, tarefa2]` |
| **List comprehension** | Filtrar/mapear | `[t for t in lista if condicao]` |
| **JSON** | Persistência | `json.dump()`, `json.load()` |
| **Datetime** | Datas/horas | `datetime.now()`, `strftime()` |
| **Try/except** | Tratamento erro | `except ValueError` |
| **Lambda** | Função anônima | `lambda x: x * 2` |
| **F-strings** | Formatar texto | `f"{variavel} texto"` |
| **Path** | Caminhos seguros | `Path.home() / "pasta"` |

---

## 🎓 PRÓXIMOS PASSOS

1. **Estude cada método** - Copie e estude um por um
2. **Teste mudanças** - Modifique e veja o resultado
3. **Implemente novos** - Use os desafios do GUIA_ESTUDO.md
4. **Refatore código** - Melhore o que aprendeu

---

**Bom uso para aprender! 🚀**
