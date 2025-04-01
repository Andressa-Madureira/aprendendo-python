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
    
    def __gt__(self, other):
        if self.h > other.h:
            return True
        elif self.h == other.h and self.m > other.m:
            return True
        elif self.h == other.h and self.m == other.m and self.s > other.s:
            return True

        return False

h1 = Horario(9, 27, 42)
h2 = Horario(9, 38, 36)
h3 = h1 + h2
print(h1)
print(h2)
print(h3)

print(f"Entrei às {h1}\n Trabalhei por {h2}\n Vou sair às {h3}")

print(h1 > h2)

# Atividade 1:

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __eq__(self, outro):
        return self.x == outro.x

class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __eq__(self, outro):
        return self.y == outro.y

a = A(x=1, y=2)
b = B(x=1, y=3)
print(a==b, b==a)

#Atividade 2:

class Tolerancia:
    def __init__(self, x, tol_minima=3, tol_maxima=6):
        self.x = x
        self.tol_minima = tol_minima
        self.tol_maxima = tol_maxima
    def __eq__(self, outro):
        return abs(self.x - outro.x) <= self.tol_minima
    def __ne__(self, outro):
        return abs(self.x - outro.x) >= self.tol_maxima
a = Tolerancia(x=10)
b = Tolerancia(x=15)
print(a==b, a!=b)