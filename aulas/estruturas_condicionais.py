media = 10

if media >= 5: 
    print("Aprovado")
else:
    print("Reprovado")


media1 = 9
frequencia = 50

if media1 >= 9:
    print("Aprovado")
elif media1 >= 6 and frequencia >= 75:
    print("Aprovado")
elif media1 >= 6 and frequencia < 75:
    print("Recuperação")
elif media1 < 6 and frequencia >= 75:
    print("Recuperação")
else:
    print("Reprovado")