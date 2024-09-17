'''
lista1 = [0,1,2,3,4,5,6,7,8,9,10]
lista2 = ["a","e","i","o","u"]

print(lista1[1])
print(lista1[2:])
#FIXME - indices negativos são tratados de forma especial, o -1 é considerado o último elemento
print(lista1[-1])

#FIXME - Método de ordenar a lista de forma crescente
lista3 = [2,421,5432,444,23344,34,3,423,66,864,645,45,7,4,565,6,6546,6,]
print(sorted(lista3))
print(lista3)
lista3.sort()

#FIXME - Método de forma decrescente
print(lista3)
lista3.sort(reverse=True)
print(sorted(lista3, reverse=True))

#FIXME - Métodos de remover: remove, pop, del
#FIXME - remove em relação ao nome
nomes = ["a","e","i","o","u","b","c","d"]
nomes.remove("e")
print(nomes)
#FIXME - remove de acordo com o indice
nomes.pop(1)
print(nomes)
#FIXME - remove mais de um elemento da lista
del(nomes[1:4])
print(nomes)
'''
nomes2 = []
novo_nome = input("fala ai: ")
nomes2.append(novo_nome)
print(nomes2)