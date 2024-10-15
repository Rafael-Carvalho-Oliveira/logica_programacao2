import os

lista_usuario = dict()

while True:
    
    
    print()
    print(30*"#","MENU",30*"#")
    print("1. Cadastrar usuário")
    print("2. Listar Usuário")
    print("3. Excluir Usuário")
    print("4. Sair")
    print(66*"#")
    print()

    opcao = int(input("Digite a opção desejada: "))   

    #Cadastrar o usuário

    if opcao == 1:
        nome = input("Digite o nome do usuário: ").capitalize()
        senha = input("Digite a senha do usuário: ").upper()
        email = input("Digite o email do usuário: ").lower()        
        lista_usuario[email] = {"nome": nome, "senha": senha, "email": email}
        print("Usuário cadastrado com sucesso")

    #Listar usuários
    elif opcao == 2:
        if lista_usuario:
            print("Usuários Cadastrados")
            for email, dados in lista_usuario.items():
                print(f"Nome: {dados['nome']}, Senha: {dados['senha']}, Email: {dados['email']}")
        else:
            print("Nenhum usuário cadastrado")


    #Excluir Usuário

    elif opcao == 3:
        nome_remove = input("Digite o nome do usuário que deseja excluir: ").capitalize()
        if nome_remove in lista_usuario:
            del lista_usuario[nome]
            print("Usuário excluído com sucesso")
        else:
            print("Usuário não encontrado")

    #Sair

    elif opcao == 4:
        print("Saindo do sistema...")
        break