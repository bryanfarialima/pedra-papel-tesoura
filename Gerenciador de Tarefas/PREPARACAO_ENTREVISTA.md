# 🎤 PREPARAÇÃO PARA ENTREVISTA TÉCNICA - VAGA JUNIOR

## 📋 Índice
1. [Checklist de Código](#checklist)
2. [Perguntas Comuns](#perguntas)
3. [Como Apresentar](#apresentacao)
4. [Dicas de Entrevista](#dicas)
5. [Recursos para Estudar](#recursos)

---

## 🎯 CHECKLIST: SEU CÓDIGO ESTÁ PRONTO?

### Type Hints
- [x] Type hints em todos os métodos
- [x] Type hints em atributos de classe
- [x] Uso de `Optional[]` para valores nulos
- [x] Uso de `List[]`, `Dict[]` do módulo `typing`

### Documentação
- [x] Docstring em classe principal
- [x] Docstring em métodos públicos
- [x] Docstring descreve parâmetros
- [x] Docstring descreve retorno
- [ ] Exemplos de uso nos docstrings
- [ ] Usar Google ou NumPy style consistently

### Tratamento de Erros
- [x] Try/except em operações de arquivo
- [x] Try/except em conversão de tipos
- [x] Mensagens de erro descritivas
- [x] Logging de operações críticas
- [ ] Teste com entrada inválida

### Validação de Entrada
- [x] Validar se título está vazio
- [x] Validar se ID é número
- [x] Validar formato de data
- [x] Pedir confirmação antes de deletar
- [ ] Validar limites (strings não infinitas)

### Boas Práticas
- [x] Constantes em MAIÚSCULAS
- [x] Métodos privados com `_` inicial
- [x] Métodos com responsabilidade única
- [x] Usar `List comprehension` onde possível
- [x] Usar `next()` para buscar primeiro item
- [ ] Evitar `print()` direto (usar logging)
- [ ] Nome das variáveis descritivos

### Estrutura
- [x] Código organizado em classe
- [x] Menu centralizado
- [x] Métodos separados por funcionalidade
- [ ] Arquivo `requirements.txt`
- [ ] Arquivo `README.md` com instruções

---

## ❓ PERGUNTAS COMUNS EM ENTREVISTA

### 1. "Explique seu projeto"

✅ **Resposta Profissional:**

"Desenvolvi um Gerenciador de Tarefas em Python que demonstra:

**Arquitetura:** Sistema orientado a objetos com uma classe principal que
encapsula toda a lógica de negócio. Persistência em JSON para simplicidade.

**Type System:** Uso intenso de Type Hints com anotações tipo `List[Dict]`,
`Optional[str]`, e `-> None` em todos os métodos para garantir clareza
de contrato e permitir verificação estática.

**Error Handling:** Tratamento robusto com try/except em operações I/O,
validação de entrada do usuário e logging de operações críticas.

**Design:** Menu escalável usando dicionário (fácil adicionar funcionalidades),
métodos utilitários privados para reutilização de código, constantes em
MAIÚSCULAS.

**UX:** Feedback claro ao usuário (✅ ❌ ⚠️), confirmação antes de operações
destrutivas, mensagens de erro descritivas.

Resultado: Código limpo, profissional, testável e pronto para integração
com banco de dados quando necessário."

---

### 2. "Qual foi o maior desafio?"

✅ **Resposta Boa:**

"O maior desafio foi gerenciar IDs de forma robusta. Inicialmente usava
`len(tarefas) + 1`, mas isso criava IDs duplicadas após deletar tarefas.

Resolvi usando `max((t["id"] for t in self.tarefas), default=0) + 1`,
que garante que cada novo ID é único mesmo após remoções, usando um
generator expression para elegância pythônica."

---

### 3. "Como você testaria este código?"

✅ **Resposta Profissional:**

"Eu criaria testes unitários usando `unittest` ou `pytest`:

```python
import unittest

class TestGerenciador(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorTarefas()
    
    def test_gerar_id_unico(self):
        '''ID nunca repete mesmo após remoção'''
        id1 = self.gerenciador._gerar_id()
        self.gerenciador.tarefas.append({'id': id1})
        id2 = self.gerenciador._gerar_id()
        self.assertNotEqual(id1, id2)
    
    def test_adicionar_tarefa(self):
        '''Tarefa adicionada aparece na lista'''
        # ... teste aqui
        
    def test_validar_data_invalida(self):
        '''Data inválida retorna None'''
        resultado = self.gerenciador._validar_data("99/99/9999")
        self.assertIsNone(resultado)
```

Além disso, faria testes de integração (end-to-end) com dados reais."

---

### 4. "Como você melhoraria este código?"

✅ **Resposta Pensada:**

"Melhorias imediatas:
- Integrar com banco de dados SQLite para melhor escalabilidade
- Adicionar testes unitários e cobertura de código
- Separar lógica de apresentação (UI) da negócio (MVVM/MVC)
- Criar camada de repositório para abstrair persistência

Melhorias futuras:
- Criar API REST com FastAPI para uso remoto
- Frontend web com React ou Vue
- Autenticação e autorização de usuários
- Sistema de compartilhamento de tarefas entre usuários"

---

### 5. "Qual é a diferença entre `List[Dict]` e `List`?"

✅ **Resposta Correta:**

"`List[Dict]` é um Type Hint que indica EXATAMENTE que é uma lista de
dicionários.

Quando você escreve:
```python
self.tarefas: List[Dict]
```

Você está dizendo:
- `self.tarefas` é uma lista
- Cada elemento da lista é um dicionário
- IDE consegue dar autocomplete para métodos de dicionário

Sem o Type Hint, IDE não sabe o que fazer:
```python
self.tarefas = []  # O que é isso? Qualquer coisa?
```

Isso é importante para: autocomplete, verificação estática (mypy),
documentação automática e código mais legível."

---

### 6. "Você conhece padrões de design?"

✅ **Resposta:**

"No meu projeto usei alguns padrões:

1. **Factory Pattern (Leve)** - `_encontrar_tarefa()` encapsula lógica
de busca

2. **Strategy Pattern (Leve)** - Dicionário de ações permite plugar
comportamentos diferentes

3. **Repository Pattern (Conceitual)** - Métodos `_carregar()` e `_salvar()`
abstraem persistência

Para projetos maiores eu usaria frameworks que implementam isso nativamente
(Django ORM para Repository, FastAPI para Factory de endpoints, etc)."

---

### 7. "O que você faria diferente em produção?"

✅ **Resposta Profissional:**

"Em produção eu mudaria:

1. **Persistência:** JSON → SQLite/PostgreSQL com ORM (SQLAlchemy)
2. **Configuração:** Variáveis de ambiente com `python-dotenv`
3. **Testing:** Testes unitários com `pytest`, coverage mínimo 80%
4. **Linting:** `black` para formato, `pylint` para estilo, `mypy` para tipos
5. **Logging:** `logging.config` centralizado, não prints
6. **Estrutura:** Separar em `models/`, `services/`, `views/`
7. **API:** Expor via REST com `FastAPI` ou `Flask`
8. **DevOps:** Docker, CI/CD com GitHub Actions, deploy em cloud"

---

## 🎤 COMO APRESENTAR SEU PROJETO

### Estrutura de Apresentação (5-10 minutos)

1. **Contexto** (30 segundos)
   - "Criei um Gerenciador de Tarefas em Python para aprender..."

2. **Funcionalidades** (1 minuto)
   - "Permite adicionar, listar, editar, remover, buscar e filtrar tarefas..."

3. **Tecnologias** (1 minuto)
   - "Usei Type Hints, tratamento de erros, logging, persistência em JSON..."

4. **Desafios** (1-2 minutos)
   - "O maior desafio foi..."

5. **Aprendizados** (1-2 minutos)
   - "Aprendi sobre..."

6. **Próximas Etapas** (30 segundos)
   - "Pretendo integrar com banco de dados e criar API REST..."

---

## 💡 DICAS DE ENTREVISTA

### ANTES
- [ ] Clone seu projeto e teste tudo
- [ ] Prepare uma explicação de 2-3 minutos
- [ ] Estude os conceitos que usou (Type Hints, logging, etc)
- [ ] Prepare exemplos de code reviews (mostre humildade)
- [ ] Tenha link do GitHub pronto para compartilhar
- [ ] Considere ter documentação criada

### DURANTE
- [ ] Fale com confiança (você estudou!)
- [ ] Admita quando não sabe: "Não sei, mas posso aprender"
- [ ] Faça perguntas sobre o projeto: "Que tipo de escala vocês esperam?"
- [ ] Busque feedback: "Qual seria sua sugestão?"
- [ ] Seja honesto sobre suas limitações: "Ainda estou aprendendo..."
- [ ] Mostre que pensa em qualidade: "Testo com..."

### DEPOIS
- [ ] Obrigado pelo tempo
- [ ] Pedir feedback
- [ ] Seguir up em 2-3 dias

---

## 📚 RECURSOS PARA ESTUDAR

### Type Hints
- [ ] PEP 484 - Type Hints
- [ ] Documentação `typing` module
- [ ] `mypy` para validação estática

### Logging
- [ ] `logging` module documentation
- [ ] Structured logging com dictConfig

### Testes
- [ ] `unittest` básico
- [ ] `pytest` avançado
- [ ] Cobertura com `coverage.py`

### Design Patterns
- [ ] "Design Patterns in Python" (real Python blog)
- [ ] Factory, Strategy, Repository patterns

### Python Profissional
- [ ] PEP 8 (Style Guide)
- [ ] PEP 20 (The Zen of Python - `import this`)
- [ ] Clean Code (Robert Martin)

---

## 🎯 PERGUNTAS QUE VOCÊ DEVE FAZER NA ENTREVISTA

### Sobre o Projeto
- "Qual é a estrutura do código da empresa?"
- "Vocês usam Type Hints?"
- "Como é o processo de code review?"

### Sobre o Trabalho
- "Como é o onboarding de juniors?"
- "Qual é a estrutura de mentoria?"
- "Quanto tempo dedica para aprendizado?"

### Sobre a Empresa
- "Qual é a stack tecnológica atual?"
- "Para onde vocês estão evoluindo?"
- "Como é a cultura da empresa?"

---

## ✅ CHECKLIST FINAL

Antes de uma entrevista técnica, seu código deve ter:

- [ ] Type hints em TUDO
- [ ] Docstrings em métodos públicos
- [ ] Tratamento de exceções
- [ ] Feedback ao usuário
- [ ] Código legível e organizado
- [ ] Constantes em MAIÚSCULAS
- [ ] Métodos com responsabilidade única
- [ ] Documentação no README
- [ ] Sem código comentado
- [ ] Sem valores mágicos soltos

---

## 🚀 MENTALIDADE PARA VAGA JUNIOR

**Lembre-se:**
- Você NÃO precisa saber tudo
- Você NÃO precisa ter experiência
- Você PRECISA mostrar que pode aprender
- Você PRECISA mostrar que escreve código limpo
- Você PRECISA mostrar que toma iniciativa

**Quando perguntarem algo que não sabe:**

❌ "Nunca fiz isso"

✅ "Não tenho experiência com isso, mas já li/estudei sobre. Posso aprender rápido"

---

## 💪 VOCÊ ESTÁ PRONTO!

Seu projeto é profissional e bem feito. Agora é questão de:

1. **Entender profundamente** cada parte do seu código
2. **Praticar** explicando para amigos
3. **Estar honesto** sobre o que você sabe e não sabe
4. **Mostrar entusiasmo** por aprender
5. **Demonstrar qualidade** no que você faz

Boa sorte! 🍀

---

**Última coisa:** Não copie código da internet sem entender. Melhor ter
um projeto pequeno e bem feito do que grande e superficial.

**Abraços e sucesso na sua carreira!** 🎉
