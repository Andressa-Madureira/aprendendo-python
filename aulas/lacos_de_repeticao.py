
numero = 1

while numero <= 10:
    print(numero," posição", sep="°")
    numero+=1


num = float(input("Digite um número maior que 10: "))
while num <= 10:
    num = float(input("O numero digitado foi menor ou igual a 10! Digite um numero maior que 10: "))

    print("Legal! O numero digitado foi: ", num)


estado_civil = input("Digite seu estado civil(opções: S, C, D, V ): ")

while estado_civil != "S" and estado_civil != "C" and estado_civil != "D" and estado_civil != "V":
   estado_civil = input("Resposta inválida! Digite seu estado civil(opções: S, C, D, V ): ")
   print("O estado civil ", estado_civil)