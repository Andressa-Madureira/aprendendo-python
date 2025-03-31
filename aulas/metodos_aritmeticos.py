n1 = 5
n2 = 6

resultAdd = n1.__add__(n2)

print(resultAdd)

resultSub = n1.__sub__(n2)

print(resultSub)

resultMulti = n1.__mul__(n2)

print(resultMulti)

class Horario:
    def __init__(self, hora, min, seg):

        self.h = hora
        self.m = min
        self.s = seg

    def __repr__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def __str__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
    
    def __add__(self, other):
        se = self.s + other.s
        mi = self.m + other.m
        ho = self.h + other.h

        if se >= 60:
            # mi = mi + 1
            mi += 1
            
            # se = se - 60
            se -= 60

        if mi >= 60:
            ho += 1
            mi -= 60

        if ho >= 24:
            ho -=24

        return Horario(ho, mi, se)

h1 = Horario(9, 27, 42)
h2 = Horario(8, 0, 0)
h3 = h1 + h2
print(h1)
print(h2)
print(h3)

print(f"Entrei às {h1}\n Trabalhei por {h2}\n Vou sair às {h3}")


   
