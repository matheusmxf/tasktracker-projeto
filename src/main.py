def main():
    tarefas = []

    while True:
        print("\n--- Menu TaskTracker ---")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n[Módulo de Cadastro em construção]")
        elif opcao == '2':
            print("\n[Módulo de visualização em construção]")
        elif opcao == '3':
            print("\nSaindo do TaskTracker. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()