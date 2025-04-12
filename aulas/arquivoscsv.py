import csv

#valores separados por vírgulas - csv
#Criar arquivo 
tabela = [["Aluno", "Nota 1", "Nota 2", "Presença"],
          ["Luke", 7, 9, 75],
          ["Han", 4, 7, 100],
          ["Leia", 9, 9, 100]]

with open("alunos_stars.csv","w", encoding="utf-8", newline='') as f:

    csv.writer(f, delimiter= ",", lineterminator="\n").writerows(tabela)


#Como ler esse arquivo?

with open("alunos_stars.csv", "r", encoding="utf-8" ) as f:
    primeira_linha = f.readline()

    tabela_lida = [linha for linha in csv.reader(f,delimiter= ",", lineterminator="\n")]
    print(tabela_lida)