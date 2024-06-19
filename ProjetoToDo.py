tarefas = []

def adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{idx}. {tarefa['nome']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status})")

def marcar_tarefa_concluida(tarefas, indice):
    if indice < 1 or indice > len(tarefas):
        print("Índice de tarefa inválido.")
        return
    tarefas[indice - 1]["concluida"] = True
    print(f"Tarefa '{tarefas[indice - 1]['nome']}' marcada como concluída.")

def listar_tarefas_por_prioridade(tarefas, prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["prioridade"] == prioridade]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada com a prioridade '{prioridade}'.")
        return
    for idx, tarefa in enumerate(tarefas_filtradas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{idx}. {tarefa['nome']} - {tarefa['descricao']} (Categoria: {tarefa['categoria']}, Status: {status})")

def listar_tarefas_por_categoria(tarefas, categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["categoria"] == categoria]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
        return
    for idx, tarefa in enumerate(tarefas_filtradas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{idx}. {tarefa['nome']} - {tarefa['descricao']} (Prioridade: {tarefa['prioridade']}, Status: {status})")

def exibir_menu():
    print("\nGerenciador de Tarefas Diárias")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Listar Tarefas por Prioridade")
    print("5. Listar Tarefas por Categoria")
    print("6. Sair")

def main():
    tarefas = []
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                nome = input("Nome da Tarefa: ")
                descricao = input("Descrição: ")
                prioridade = input("Prioridade: ")
                categoria = input("Categoria: ")
                adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria)
            case '2':
                listar_tarefas(tarefas)
            case '3':
                indice = int(input("Índice da Tarefa a ser marcada como concluída: "))
                marcar_tarefa_concluida(tarefas, indice)
            case '4':
                prioridade = input("Prioridade: ")
                listar_tarefas_por_prioridade(tarefas, prioridade)
            case '5':
                categoria = input("Categoria: ")
                listar_tarefas_por_categoria(tarefas, categoria)
            case '6':
                print("Saindo do programa.")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
