class Horario:
    def __init__(self, hora, min, seg):
        self.h = hora
        self.m = min
        self.s = seg

    def __repr__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def __str__ (self):
        return f"O horário é: {self.h:02d}:{self.m:02d}:{self.s:02d}"

h1 = Horario(15, 7, 2)
print(h1)