#podemos criar nossas próprias funções em Python - um pedacinho de código que faz uma determinada função/tarefa específica

def fala_oi():
    print("Oi, dev!")

fala_oi()

def fala_oi_pra_alguem(nome_de_alguem):

    print(f"Oi, {nome_de_alguem}! Que bom te ver!")
    
fala_oi_pra_alguem("Andressa")

#Uma função pode ter 2 argumentos

'''
doc string:
  esta função recebe um nome e uma parte do dia, e imprime na tela um
  cumprimento de acordo com esses dois argumentos

  - nome (str): qualquer nome própiro;
  - parte_do_dia (str): deve ser unicamente uma das três opções: ["manhã", "tarde", "noite"]
  '''
def cumprimenta_parte_do_dia(nome, parte_do_dia):
    if parte_do_dia == "manhã":
        cumprimento = "Bom dia"
    elif parte_do_dia == "tarde":
        cumprimento = "Boa tarde"
    elif parte_do_dia == "noite":
        cumprimento = "Boa noite"
    else:
        raise ValueError(f"A parte do dia informada({parte_do_dia}) não é válida")

       
    return f"{cumprimento},{nome}!"


mensagem = cumprimenta_parte_do_dia("Andressa", "noite")
print(mensagem)

#biblioteca - sklearn : muito bem documentada


def calcula_soma(n1,n2):
    soma = n1 + n2
    return soma

def calcula_multi(n1, n2):
    multi = n1 * n2
    return multi

def calcula_subtracao(n1, n2):
    subtracao = n1 - n2
    return subtracao


def calcula_divisao(n1, n2):
    divisao = n1 / n2
    return divisao
    '''
    esta função calcula o quociente entre o primeiro argumento e o segundo 
    -n1(float), numerador
    -n2(float), denominador, deve ser !=0
    '''

#Criaremos agora a função de calculadora 

def calcula_operacao(n1,n2, op):
    '''
    -> n1(float)
    -> n2(float)
    -> op (str): indicando a operação a ser feita["+","-","*","/"]

    returns:

    n1[op] n2, onde [op] é a operação correspondente à string op

    '''

    if op == "+":
        return calcula_soma(n1, n2)
    elif op == "-":
        return calcula_subtracao(n1, n2)
    elif op == "*":
        return calcula_multi(n1, n2)
    elif op == "/":
        return calcula_divisao(n1, n2)
    else:
        raise ValueError(f"A operação informada ({op}) não é válida")
   
    
resultado1 = calcula_operacao(2,8, "+")
resultado2 = calcula_operacao(3,8, "*")
resultado3 = calcula_operacao(4,2, "-")
resultado4 = calcula_operacao(64,8, "/")


print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)




#verificar guia de boas práticas: PEP 8 - Style Guide for Python Code 

#PENDENTE - GIT PUSH

