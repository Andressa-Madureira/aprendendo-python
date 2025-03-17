#string é uma coleção de caracteres

nome = 'Andressa'

for caractere in nome:
    print(caractere)

len(nome)

nome[2]

#alterar caracteres(ou palavras) podemos utilizar o "replace()"

nome.replace("A", "a")

#Transformar em lista:
nome = 'andressa'

nome_lista = list(nome)

nome_lista[-1]

nome_lista

#Transforma a lista de volta para string, podemos usar a função join(). Concatena cada elemento da lista 

"".join(nome_lista)

#soma de strings

"a" + "b"

#multiplicação de string por inteiro- ao multiplicar a string é repetida

"ab" * 3
"abc" * 7

print("="*100)
print("Olá, sejam bem vindos(as) ao meu Github".center(100))
print("="*100)

#funções de strings 
     #para centralizar:

"andressa".center(50)

#transformar todos os caracteres em maiuscula

"andressa".upper()

#transformar todos os caracteres em minuscula
"JOANA".lower()

#Deixa a primeira letra de cada palavra em maiuscula:
"olá, devs!"
"olá, devs!".title()

#Deixa a primeira letra da primeira palavra em maiuscula:
apresentacao = "olá, devs!"

apresentacao.capitalize()

#Quebrar espaços - transformando a string em lista

apresentacao.split()

#Tirar espaços que estão sobrando no fim e no inicio da string - função strip()
string = "                    Eu gosto de estudar Python                   "
string.strip()

#Outras funções : isdigit() - isalpha() - isalnum() - isspace()
fala = "ele disse para o colega: 'nos encontramos amanhã às 14:00??'"

lista_de_letras=[]
lista_de_numeros=[]
lista_de_simbolos =[]

for char in fala:
    if char.isalpha():
        lista_de_letras.append(char)
    elif char.isdigit():
        lista_de_numeros.append(char)
    else:
        lista_de_simbolos.append(char)

    print("Letras",lista_de_letras)
    print("Numeros",lista_de_numeros)
    print("Simbolos", lista_de_simbolos)


estado_civil = input("Digite seu estado civil(opções possíveis S, C, D, V): ").upper()

while estado_civil not in ["S", "C", "D", "V"]:
    estado_civil = input("Resposta inválida! Digite seu estado civil(opções possíveis S, C, D, V): ").upper()

    print(f"Estado civil:{estado_civil}")