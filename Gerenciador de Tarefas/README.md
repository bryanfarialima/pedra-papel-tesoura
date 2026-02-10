# 📱 Gerenciador de Tarefas - Versão Completa

## 📋 Arquivos do Projeto

```
Python Projetos/
├── app_tarefas.py              ← Versão inicial (seu código original)
├── app_tarefas_completo.py     ← Versão COMPLETA com todas funcionalidades
├── teste_app.py                ← Teste da versão inicial
├── teste_completo.py           ← Teste da versão completa
├── GUIA_ESTUDO.md              ← Conceitos e explicações
└── README.md                   ← Este arquivo
```

---

## 🚀 COMO USAR

### Executar a versão completa (interativa)
```bash
/usr/bin/python3 "/Users/bryanfarialima/Documents/Python Projetos/app_tarefas_completo.py"
```

### Executar os testes
```bash
/usr/bin/python3 "/Users/bryanfarialima/Documents/Python Projetos/teste_completo.py"
```

---

## ✨ FUNCIONALIDADES IMPLEMENTADAS

### 1. ➕ Adicionar Tarefa
- Título obrigatório
- Descrição (opcional)
- Categoria (trabalho, pessoal, estudos, saúde, compras, etc)
- Nível de prioridade (Alta, Média, Baixa)
- Data de vencimento (opcional)

```python
# Exemplo da estrutura de uma tarefa
{
    "id": 1,
    "titulo": "Estudar Python",
    "descricao": "Classes e herança",
    "categoria": "Estudos",
    "prioridade": "Alta",
    "concluida": False,
    "data_vencimento": "15/02/2026",
    "data_criacao": "09/02/2026 14:30"
}
```

### 2. 📋 Listar Tarefas
- Mostra todas as tarefas
- Exibe com formatação colorida
- Mostra status (✅ concluída / ⭕ pendente)
- Mostra todas as informações da tarefa

### 3. ✅ Marcar como Concluída
- Marca tarefa como completa
- Sem deletar a tarefa
- Pode ser "desfeita" editando

### 4. ✏️ Editar Tarefa
- Modifica qualquer campo
- Campos em branco mantêm valor anterior
- Salva automaticamente

### 5. ❌ Remover Tarefa
- Deleta tarefa permanentemente
- Pede confirmação antes de remover

### 6. 🔍 Buscar Tarefa
- Busca por palavra-chave
- Procura em título e categoria
- Mostra resultados formatados

### 7. 📁 Filtrar por Categoria
- Lista categorias disponíveis
- Filtra tarefas por categoria
- Agrupa tarefas relacionadas

### 8. 🧹 Limpar Tarefas Concluídas
- Remove todas as tarefas marcadas como feitas
- Pede confirmação
- Útil para manter lista limpa

### 9. 📊 Ver Estatísticas
- Total de tarefas
- Percentual de conclusão
- Contagem por prioridade
- Contagem por categoria

### 10. 🚪 Sair
- Encerra o programa
- Dados salvos automaticamente

---

## 🗂️ ESTRUTURA DO CÓDIGO

### Classe Principal: `GerenciadorTarefas`

```python
class GerenciadorTarefas:
    def __init__(self):
        # Configurações iniciais
    
    # Métodos de Arquivo
    def carregar_tarefas(self)
    def salvar_tarefas(self)
    
    # Métodos de Operação (CRUD)
    def adicionar_tarefa(self)
    def listar_tarefas(self, filtro=None)
    def marcar_concluida(self)
    def editar_tarefa(self)
    def remover_tarefa(self)
    def limpar_concluidas(self)
    def buscar_tarefas(self)
    def filtrar_por_categoria(self)
    def estatisticas(self)
    
    # Métodos Auxiliares
    def _exibir_tarefa(self, tarefa)
    def _limpar_tela(self)
    
    # Menu
    def menu_principal(self)
```

---

## 📊 LOCALIZAÇÃO DOS ARQUIVOS

- **Arquivo de dados:** `~/.tarefas_app/tarefas.json`
  - Exemplo: `/Users/bryanfarialima/tarefas_app/tarefas.json`
- **Estrutura:** Array JSON com objetos de tarefas

---

## 🎓 CONCEITOS APRENDIDOS

### Programação Orientada a Objetos (POO)
- Classes
- Métodos
- Atributos (self)
- Encapsulamento

### Estruturas de Dados
- Dicionários
- Listas
- Listas de dicionários
- List comprehensions

### Operações com Arquivos
- Ler JSON
- Escrever JSON
- Manipular caminhos com Path

### Funcionalidades de Data/Hora
- datetime.now()
- timedelta
- strftime() e strptime()

### Tratamento de Erros
- try/except
- Validação de entrada

### Funcionalidades Avançadas
- Lambda functions
- sorted() com key
- next() com generator
- Cores ANSI no terminal
- f-strings

---

## 🔧 CONFIGURAÇÃO DO AMBIENTE

O código usa apenas bibliotecas padrão do Python:
- `pathlib` - gerenciar caminhos
- `datetime` - dados/horas
- `json` - persistência de dados
- `os` - operações do sistema

**Nenhuma instalação externa necessária!**

---

## 📈 ROADMAP PARA MELHORIAS FUTURAS

### Curto Prazo
- [ ] Exportar tarefas para CSV
- [ ] Importar tarefas de CSV
- [ ] Backup automático

### Médio Prazo
- [ ] Interface gráfica (tkinter ou PyQt)
- [ ] Sincronização com nuvem
- [ ] Notificações de vencimento

### Longo Prazo
- [ ] Aplicativo web (Flask/Django)
- [ ] Aplicativo mobile
- [ ] API RESTful
- [ ] Banco de dados (SQLite/PostgreSQL)

---

## 💡 DICAS DE ESTUDO

1. **Leia o código devagar** - Entenda cada linha
2. **Teste as funcionalidades** - Use o app interativo
3. **Faça modificações** - Customize conforme desejar
4. **Implemente novas features** - Use os desafios do GUIA_ESTUDO.md
5. **Estude a seção de conceitos** - Entenda a teoria por trás

---

## 🆘 TROUBLESHOOTING

**Erro: "Python não encontrado"**
```bash
# Use o caminho completo
/usr/bin/python3 app_tarefas_completo.py
```

**Erro: "Arquivo não encontrado"**
- Verifique se está na pasta correta
- Use caminhos absolutos

**Dados não salvam**
- Verifique permissões da pasta `~/tarefas_app`
- Verifique se tem espaço em disco

---

## 📞 CONTATO / SUGESTÕES

Se tiver dúvidas sobre o código:
1. Leia o GUIA_ESTUDO.md
2. Procure pelos comentários no código
3. Use print() para debugar
4. Teste funções individualmente

---

## 📄 LICENÇA

Este projeto é educacional. Sinta-se livre para usar e modificar!

---

**Versão:** 1.0  
**Última atualização:** 09/02/2026  
**Status:** ✅ Funcional
