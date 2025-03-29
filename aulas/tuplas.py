#Tuplas são estruturas bastante parecidas com listas:Podem guardar tipos diferentes de dados;São indexadas (podemos acessar elementos por índices);São iteráveis (podemos percorrer com o for). 

# Tuplas são inicializadas como uma sequência de valores entre parênteses ()
tupla = (1, 4.2, True, "ada", [1, 2, 3])

print(tupla)
len(tupla)

# é possível definir tuplas sem a utilização de parênteses, apenas listando os elementos, separados por vírgula
tupla2 = 1, 2, 3, "a", "b"
print(tupla2)

# tuple unpacking

x, y = 2, 3

# x = 2
# y = 3

print(x)
print(y)

#Operações com tuplas

tupla

tupla[-2]

for elemento in tupla:
    print(elemento)

for i in range(len(tupla)):
    print(i, tupla[i])

tupla
lista = list(tupla)
lista[0] = "um" 
lista

tupla

def valor_valor_quadrado_valor_cubo(x):

  return x, x**2, x**3

valor_valor_quadrado_valor_cubo(2)

