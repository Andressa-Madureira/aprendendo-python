#coleção:

lista_numeros = [2, 5, 4.2, -6] 
type(lista_numeros)
print(lista_numeros) 
print(lista_numeros[2])

#fatiar - me dá os primeiros 3 elementos começando com o index(posição) 1 
print(lista_numeros[1:3])

#pegar de determinada posição até o final
print(lista_numeros[1:])


#

l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2

l3
l3*2

#funções de lista
#criar uma lista vazia:

list = []

#incluir um número no final
list.append(5)

print(list)

list.append("Andressa")
list.append("8")

print(list)


#adicionar um elemento em uma posição específica => lê-se: na posição 2, inclua a string Joana

list.insert(2,"Joana")

print(list)

#para atulizar/redefinir um dos elementos da lista:

list[3] = 1

print(list)

#para somar um elemento da lista e incluir/atualizar
list[0] = list[0] + 5
print(list)

#remover item da lista que tem o número informado(apenas a primeira aparição)

list.remove(10)
print(list)

#remover um elemento de determinado índice

list.pop(0)

print(list)

list.append(85)
list.append(23)
list.append(14)
list.append(2)
list.append(90)

print(list)

#para ordenar os elementos

list_ord = []
list_ord.append(85)
list_ord.append(7)
list_ord.append(5)
list_ord.append(35)
list_ord.append(25)

print(list_ord)

sorted(list_ord)

#ordenar string - é ordenada de acordo com a tabela asci

list_alpha = []

list_alpha.append("ana")
list_alpha.append("beto")
list_alpha.append("Andressa")
list_alpha.append("joana")
list_alpha.append("Paula")

print(list_alpha)

sorted(list_alpha)

#ordenar de ordem inversa

sorted(list_ord)[::-1]


#retornar a primeira aparição do elemento

list_ord.index(5)

#encontrar o maior elemento da lista

max(list_ord)

#encontrar o menor elemento da lista
min(list_ord)

#para saber quantos elementos tem na lista

len(list_ord)

#somar os elementos da lista

sum(list_ord)

#calcular o valor medio dos elementos

sum(list_ord) / len(list_ord)