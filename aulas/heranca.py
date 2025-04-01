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


c2 = Cachorro("Leo", "poodle", "branco")
c2.fala()
    