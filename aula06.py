'''
lista = [3454,536,47,544,657,5,6,67544,53,34,46,53,456,5,43789,97,6576,45,865,5,47]
lista.append("rgreg")
print(lista)

#FIXME - Inserção
lista.insert(2, "cvfbg")
print(lista)

#FIXME - Substituição

lista[2] = "dcfgh"
print(lista)

#FIXME - Verificar se está na lista

print(47 in lista)
print(47 not in lista)

if "gomes" in lista:
# esse bloco só será executado quando a condição é true
    print("gay")
else:
# esse bloco só será executado quando a condição é false
     print("straight")
'''      
print(40*"-","Boletim Escolar",40*"-")

notas = []

aluno1 = int(input("Digite um número: "))
notas.append(aluno1)
aluno2 = int(input("Digite um número: "))
notas.append(aluno2)
aluno3 = int(input("Digite um número: "))
notas.append(aluno3)

# len conta a quantidade de elementos dentro de uma lista
quantidade_notas = len(notas)

# sum irá somar todos os valores da lista
soma = sum(notas)

media = soma / quantidade_notas

print(f"As notas são: {notas}")
print(f"A quantidade de notas são: {quantidade_notas}")
print(f"A soma deu: {soma}")
print(f"A média deu: {media}")

'''
#TODO - Situação
Aprovado >= 7
Recuperação >= 5
Reprovado
'''
if media >= 7:
    print(f"Aprovado com média {media}")
elif media >= 5:
    print(f"Recuperação com média {media}")
else:
    print("Reprovado")