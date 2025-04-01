#Polimorfismo - muitas formas - isinstance
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fala(self):
        print(f"{self.nome} faz barulho")

a1 = Animal("grilo")
a1.fala()

class Cachorro(Animal):

    def __init__(self, nome, raca, cor_do_pelo):

        super().__init__(nome)

        self.raca = raca
        self.cor_do_pelo = cor_do_pelo

    def fala(self):
        super().fala()

        print(f"Mas, por ser um cachorro, {self.nome} latiu")

class Gato(Animal):

    def fala(self):
        print(f"{self.nome} mia")

g2 = Gato("fred")
c2 = Cachorro("léo", "poodle", "branco")

testes = isinstance(g2, Gato)

result = isinstance(g2, Cachorro)
print(testes)
print(result)
#Pendente -> Fazer uma atividade sobre polimorfismo