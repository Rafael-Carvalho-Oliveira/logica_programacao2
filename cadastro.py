lista_usuario = []

while True:
    
    print()
    print(30*"#","MENU",30*"#")
    print("1. Cadastrar usuário")
    print("2. Listar Usuário")
    print("3. Excluir Usuário")
    print("4. Buscar pelo nome")
    print("5. Sair")
    print(66*"#")
    print()

    opcao = int(input("Digite a opção desejada: "))

    #Cadastrar usuário
    if opcao == 1:
        nome = input("Digite o nome que deseja cadastrar: ").upper()

        if nome != "":
            lista_usuario.append(nome)
            print(f"Usuário {nome} cadastrado com sucesso!")
        else:
            print("Digite algum valor!")

    #listar usuario
    elif opcao == 2:
        for i, n in enumerate(lista_usuario):
            print(f"{i + 1}° {n}")
    #excluir usuario
    elif opcao ==  3:

        nome = input("Digite o nome que deseja excluir: ").upper()

        for i in lista_usuario:
            if nome == i:
                lista_usuario.remove(i)
                print("Usuário removido com sucesso")

    #buscar pelo nome
    elif opcao == 4:
        nome_buscar = input("digite o nome que deseja buscar na lista: ").upper()

        if nome_buscar != "":
            for i in lista_usuario:
                    if i == nome_buscar:
                        print(i)

    #sair do sistema
    elif opcao == 5:
        print("Saindo do sistema!")
        break

    else:
        print("Digite uma opção válida!")

