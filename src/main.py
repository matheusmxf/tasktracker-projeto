def main():
    tarefas = []

    while True:
        print("\n--- Menu TaskTracker ---")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n--- Cadastrar Nova Tarefa ---")
            
            while True:
                titulo = input("Título da tarefa: ").strip()
                if titulo == "":
                    print("Erro: O título não pode estar vazio. Digite novamente.")
                else:
                    break
            
            descricao = input("Descrição da tarefa (opcional): ").strip()
            
            while True:
                prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().capitalize()
                if prioridade in ["Alta", "Média", "Media", "Baixa"]:
                    break
                else:
                    print("Erro: Prioridade inválida. Escolha entre Alta, Média ou Baixa.")
            
            data_limite = input("Data limite (Ex: DD/MM/AAAA): ").strip()
            
            status = "Pendente"
            
            nova_tarefa = {
                "titulo": titulo,
                "descricao": descricao,
                "prioridade": prioridade,
                "data_limite": data_limite,
                "status": status
            }
            tarefas.append(nova_tarefa)
            print("\nMensagem de confirmação: Tarefa cadastrada com sucesso!")

        elif opcao == '2':
            print("\n--- Tarefas Cadastradas ---")
            
            if len(tarefas) == 0:
                print("Aviso de lista vazia: Nenhuma tarefa foi cadastrada ainda.")
            else:
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1}. {tarefa['titulo']} | Prioridade: {tarefa['prioridade']} | Data: {tarefa['data_limite']} | Status: {tarefa['status']}")
                    if tarefa['descricao']:
                        print(f"   Detalhes: {tarefa['descricao']}")

        elif opcao == '3':
            print("\nSaindo do TaskTracker. Até logo!")
            break
            
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()