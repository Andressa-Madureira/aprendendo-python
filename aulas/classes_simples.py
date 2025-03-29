class Pessoa:
    def __init__(self, name, age, res): #método construtor -> inicializa os atributos da nossa classe. Self argumentos das funções e faz referência aos atributos da classe.

        #inicializar os atributos da classe
        self.nome = name
        self.idade = age
        self.residencia = res

#inicializar alguns atributos cujos valores são fixados

        self.num_filhos = 0
        self.profissao = None

#criando um objeto - 

objeto_construtor = Pessoa("Andressa",29, "RJ")

objeto_construtor.nome

       