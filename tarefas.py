tarefas ={}
id = 0
while True:
    print("Gerenciador de Tarefas")
    print("1. Inserir tarefa")
    print("2. Visualizar tarefas")
    print("3. Excluir tarefa")
    print("4. Sair")
    opcao = int(input("Sua opção:"))
    if opcao == 1:
        desc = input("Descreva a tarefa: ")
        tarefas[id] = desc
        id+=1
        print("Tarefa inserida com sucesso!")
    elif opcao == 2:
        if len(tarefas)>0:
            for k,v in tarefas.items():
                print(k,v)
        else:
            print("Lista Vazia")
    elif opcao == 3:
        id_exclusao = int(input("Entre com o id da tarefa a ser excluída:"))
        if id_exclusao in tarefas:
            del tarefas[id_exclusao]
            print("tarefa removida com sucesso!")
        else:
            print("id não encontrado")
    elif opcao == 4: 
        print("Saindo....")
        break
    else:
        print("Ops! Opção inválida!!")