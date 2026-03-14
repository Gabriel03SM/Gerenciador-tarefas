import os

tarefas = []

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    print("GERENCIADOR DE TAREFAS")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")
    print("=" * 30)

def adicionar():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"nome": tarefa, "feito": False})
    print("Tarefa adicionada!")

def listar():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n📋 Lista de tarefas:")
    for i, t in enumerate(tarefas):
        status = "✔️" if t["feito"] else "❌"
        print(f"{i+1}. {t['nome']} [{status}]")

def concluir():
    listar()
    try:
        num = int(input("\nDigite o número da tarefa concluída: "))
        tarefas[num-1]["feito"] = True
        print("Tarefa concluída!")
    except:
        print("Número inválido.")

def remover():
    listar()
    try:
        num = int(input("\nDigite o número da tarefa para remover: "))
        tarefas.pop(num-1)
        print("Tarefa removida.")
    except:
        print("Número inválido.")

while True:
    limpar()
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        concluir()
    elif opcao == "4":
        remover()
    elif opcao == "5":
        print("Saindo")
        break
    else:
        print("Opção inválida.")

    input("\nPressione ENTER para continuar")
