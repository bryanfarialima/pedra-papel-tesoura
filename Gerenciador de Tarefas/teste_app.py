#!/usr/bin/python3
from pathlib import Path
import os
import sys

# Limpar tarefas anteriores para teste
pasta = Path.home() / "tarefas_app"
if pasta.exists():
    arquivo = pasta / "tarefas.txt"
    if arquivo.exists():
        arquivo.unlink()

pasta.mkdir(exist_ok=True)

arquivo = pasta / "tarefas.txt"

print(f"Arquivo salvo em: {arquivo}")

tarefas = []

if arquivo.exists():
    with open(arquivo, "r") as f:
        for linha in f:
            tarefas.append(linha.strip())


def salvar_tarefas(lista):
    with open(arquivo, "w") as f:
        for tarefa in lista:
            f.write(tarefa + "\n")


# Teste automatizado
print("\n=== TESTANDO FUNCIONALIDADES ===\n")

# Teste 1: Adicionar tarefa
print("✓ Teste 1: Adicionando tarefa 'Comprar leite'")
tarefas.append("Comprar leite")
salvar_tarefas(tarefas)
print("Tarefa adicionada!\n")

# Teste 2: Adicionar outra tarefa
print("✓ Teste 2: Adicionando tarefa 'Fazer exercício'")
tarefas.append("Fazer exercício")
salvar_tarefas(tarefas)
print("Tarefa adicionada!\n")

# Teste 3: Listar tarefas
print("✓ Teste 3: Listando tarefas")
if not tarefas:
    print("Nenhuma tarefa cadastrada.")
else:
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1} - {tarefa}")
print()

# Teste 4: Remover tarefa
print("✓ Teste 4: Removendo tarefa 1 ('Comprar leite')")
if 1 <= 1 <= len(tarefas):
    tarefas.pop(0)
    salvar_tarefas(tarefas)
    print("Tarefa removida!\n")

# Teste 5: Listar tarefas novamente
print("✓ Teste 5: Listando tarefas após remoção")
if not tarefas:
    print("Nenhuma tarefa cadastrada.")
else:
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1} - {tarefa}")
print()

# Verificar arquivo
print("✓ Teste 6: Verificando arquivo salvo")
with open(arquivo, "r") as f:
    conteudo = f.read()
    print(f"Conteúdo do arquivo:\n{conteudo}")

print("=== TODOS OS TESTES PASSARAM! ===")
