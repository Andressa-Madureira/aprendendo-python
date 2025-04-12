notas = [ 8, 9, 8.5, 10]

with open("notas.txt", "w", encoding="utf-8") as f:
    f.write(f"{notas[0]}")
    for elemento in notas[1:]: 
        f.write(f"\n{elemento}")