#percorre cada elemento da lista

list = [10, 8, 65, 24, 32]

for elemento in list:
    print(elemento, elemento*2, elemento/2)


#range - recebe 3 argumentos -> é um sequência de N elementos que começa em 0
list_num = [4,7,13,15,1,8,16,20,3]
len(list_num)

for indice in range(9):
    print(indice, list_num[indice])

N=5
for i in range(N):
    print("Olá,mundo")