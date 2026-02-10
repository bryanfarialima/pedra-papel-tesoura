from pathlib import Path

pasta = Path.home() / "tarefas_app"
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


while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ").strip()
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(i + 1, "-", tarefa)

    elif opcao == "3":
        if not tarefas:
            print("Nada para remover.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(i + 1, "-", tarefa)

            try:
                numero = int(input("Qual número deseja remover? "))
            except ValueError:
                print("Digite apenas números.")
                continue

            if 1 <= numero <= len(tarefas):
                tarefas.pop(numero - 1)
                salvar_tarefas(tarefas)
                print("Tarefa removida!")
            else:
                print("Número inválido.")

    elif opcao == "4":
        print("Encerrando programa ...")
        break

    else:
        print("Opção inválida")
