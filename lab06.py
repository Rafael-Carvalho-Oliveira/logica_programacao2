'''
lista = []

nome0 = input("Digite um nome: ")
lista.append(nome0)
nome1 = input("Digite um nome: ")
lista.append(nome1)
nome2 = input("Digite um nome: ")
lista.append(nome2)
nome3 = input("Digite um nome: ")
lista.append(nome3)

lista.sort()

if "a" and not "s" in lista:
    print(f"{nome0} e {nome1} está na lista")
else:
    print("não está na lista")
'''

numero_sorte = [25,4,76,34]
nome0 = input("Digite um número: ")
numero_sorte.append(nome0)
nome1 = input("Digite um número: ")
numero_sorte.append(nome1)
nome2 = input("Digite um número: ")
numero_sorte.append(nome2)
nome3 = input("Digite um número: ")
numero_sorte.append(nome3)

if nome0+nome1+nome2+nome3 in numero_sorte:
    print("tu ganhou")
else:
    print("tu perdeu")