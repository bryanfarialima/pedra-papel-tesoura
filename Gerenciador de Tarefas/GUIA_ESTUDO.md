# 📚 GUIA DE ESTUDO - APP DE TAREFAS COMPLETO

## Olá! Este é um guia para você aprender os conceitos usados no código.

---

## 🎯 O QUE MUDOU DO CÓDIGO INICIAL PARA O COMPLETO?

### 1. **ESTRUTURA COM CLASSES (Programação Orientada a Objetos)**

**ANTES (Código simples):**
```python
tarefas = []
def salvar_tarefas(lista):
    # código solto
```

**DEPOIS (Código organizado):**
```python
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    
    def salvar_tarefas(self):
        # código organizado
```

**Por quê?** Classes nos permitem:
- Agrupar dados (self.tarefas) com funções (métodos)
- Manter tudo organizado em um único lugar
- Reutilizar o código facilmente
- Esconder detalhes internos (encapsulamento)

---

## 2. **JSON EM VEZ DE TXT SIMPLES**

**ANTES:**
```
Comprar leite
Fazer exercício
```

**DEPOIS:**
```json
[
  {
    "id": 1,
    "titulo": "Comprar leite",
    "categoria": "Compras",
    "prioridade": "Baixa",
    "concluida": false,
    "data_vencimento": "10/02/2026"
  }
]
```

**Por quê JSON?**
- Suporta múltiplos campos por tarefa
- Fácil de ler e escrever
- Estruturado e organizado
- Fácil de ordenar e filtrar

**Como usar:**
```python
import json

# Salvar
with open("arquivo.json", "w") as f:
    json.dump(tarefas, f)

# Carregar
with open("arquivo.json", "r") as f:
    tarefas = json.load(f)
```

---

## 3. **METODOS SEPARADOS POR RESPONSABILIDADE**

Cada método faz UMA coisa bem:

```python
def adicionar_tarefa(self):
    """Apenas adiciona"""

def salvar_tarefas(self):
    """Apenas salva no arquivo"""

def listar_tarefas(self, filtro=None):
    """Apenas lista"""
```

**Por quê?** Isso chama-se **Princípio da Responsabilidade Única (SRP)**
- Código mais limpo
- Fácil de testar
- Fácil de manter
- Fácil de reutilizar

---

## 4. **PRIORIDADES E CATEGORIAS**

```python
self.prioridades = {"1": "Baixa", "2": "Média", "3": "Alta"}
```

Adicionado:
- Campo `prioridade` em cada tarefa
- Campo `categoria` para agrupar
- Ordenação por prioridade com `sorted()`

```python
# Ordenar por prioridade
tarefas.sort(key=lambda x: -ordem_prioridade[x["prioridade"]])
```

---

## 5. **DATAS E VENCIMENTOS**

```python
from datetime import datetime, timedelta

# Criar data
data = datetime.now()  # Data/hora atual

# Adicionar dias
proxima_semana = datetime.now() + timedelta(days=7)

# Formatar para string
data.strftime("%d/%m/%Y")  # "09/02/2026"

# Converter string para data
datetime.strptime("09/02/2026", "%d/%m/%Y")
```

---

## 6. **FILTROS E BUSCAS**

### List Comprehension (forma pythônica)

```python
# Filtrar tarefas concluídas
concluidas = [t for t in self.tarefas if t["concluida"]]

# Filtrar por categoria
trabalho = [t for t in self.tarefas if t["categoria"] == "Trabalho"]

# Filtrar e transformar
titulos = [t["titulo"] for t in self.tarefas]
```

**Como funciona:**
```
[NOVO_ITEM for ITEM in LISTA if CONDICAO]
```

---

## 7. **TRATAMENTO DE ERROS**

```python
try:
    tarefa_id = int(input("Digite o ID: "))
except ValueError:
    print("❌ ID inválido!")
```

**Por quê?** Se o usuário digitar "abc" em vez de número, não cai programa:
- `try`: tenta executar
- `except`: captura o erro
- Continua executando normalmente

---

## 8. **CORES NO TERMINAL**

```python
self.cores = {
    "Alta": "\033[91m",      # Vermelho
    "Média": "\033[93m",     # Amarelo
    "Baixa": "\033[92m",     # Verde
    "reset": "\033[0m"       # Normal
}

# Usar cores
print(f"{self.cores['Alta']}Tarefa importante{self.cores['reset']}")
```

**Códigos ANSI comuns:**
- `\033[91m` = Vermelho
- `\033[92m` = Verde
- `\033[93m` = Amarelo
- `\033[0m` = Reset (volta ao normal)

---

## 9. **MÉTODOS AUXILIARES**

```python
def _exibir_tarefa(self, tarefa):
    """Método privado (começa com _)
    Reutilizado em vários lugares"""
    # código aqui
```

**Por quê o underscore?**
- Sinaliza que é uso interno da classe
- Não deve ser chamado de fora
- Evita duplicação de código

---

## 10. **LAMBDA E SORTED()**

```python
# Lambda: função anônima (sem nome)
tarefa_quadrada = lambda x: x ** 2

# Usar lambda em sorted
tarefas.sort(key=lambda x: x["prioridade"])
```

**Como funciona:**
```python
sorted(lista, key=funcao_de_chave)
```

A função retorna qual valor usar para ordenar.

---

## 11. **STRING FORMATTING (f-strings)**

```python
# Antes (ruim)
print("Tarefa: " + titulo + " - Status: " + status)

# Depois (bom - f-string)
print(f"Tarefa: {titulo} - Status: {status}")

# Com expressões
print(f"Total: {len(tarefas)} tarefas ({(len(tarefas)/total*100):.1f}%)")
```

---

## 12. **DICIONÁRIOS E NEXT()**

```python
# Encontrar uma tarefa pelo ID
tarefa = next((t for t in self.tarefas if t["id"] == tarefa_id), None)

# Como funciona:
# next(gerador, valor_padrao)
# Retorna o PRIMEIRO item que atende a condição
# Ou None se não encontrar
```

---

## 🔥 DESAFIOS PARA VOCÊ PRATICAR

### Fácil:
1. Adicione um campo "tags" as tarefas (lista de palavras-chave)
2. Crie filtro por tags
3. Adicione campo de "criador" da tarefa

### Médio:
4. Adicione exclusão de tarefas por padrão de texto (regex)
5. Crie relatório semanal de tarefas
6. Adicione "recorrência" (tarefa que se repete)

### Difícil:
7. Crie sincronização com arquivo .csv
8. Adicione autenticação de usuários
9. Implemente undo/redo de operações
10. Crie exportação para PDF

---

## 📖 RECURSOS PARA APRENDER MAIS

### Sobre Classes:
```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

dog = Cachorro("Rex")
print(dog.fazer_som())  # Au au!
```

### Sobre JSON:
- `json.dump()` = escrever em arquivo
- `json.load()` = ler de arquivo
- `json.dumps()` = converter para string
- `json.loads()` = converter de string

### Sobre Datetime:
- `datetime.now()` = agora
- `datetime.today()` = hoje
- `timedelta()` = diferença de tempo
- `.strftime()` = formatar data
- `.strptime()` = ler data

---

## 🎓 CHECKLIST DE APRENDIZADO

Você entendeu:

- [ ] Classes e métodos
- [ ] JSON (carregar/salvar)
- [ ] List comprehensions
- [ ] Tratamento de erros (try/except)
- [ ] Lambda e sorted()
- [ ] Datetime
- [ ] Cores no terminal
- [ ] f-strings
- [ ] Princípio da Responsabilidade Única (SRP)
- [ ] Como organizar código grande

---

## 💡 PRÓXIMAS ETAPAS

1. **Execute o app:** `python3 app_tarefas_completo.py`
2. **Estude o código:** Leia linha por linha
3. **Faça modificações:** Customize conforme desejar
4. **Implemente novos recursos:** Use os desafios acima
5. **Refatore:** Melhore o código existente

---

**Bom estudo! 🚀**
