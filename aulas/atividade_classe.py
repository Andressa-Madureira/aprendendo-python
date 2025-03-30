class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def postar(self):
        print(f"{self.nome} fez uma postagem!")
    
class Influencer(Usuario):
    def __init__(self, nome, email, seguidores):
        super().__init__(nome, email)

        self.seguidores = seguidores
    def postar(self):
        print(f"{self.nome} postou um #publi para seus 5000 seguidores!")
    
class Administrador(Usuario):

    def banir_usuario(self, usuario_banido):
        print(f"O usuário {usuario_banido} foi banido por {self.nome}")

#Criando os objetos

usuario_comum = Usuario("Andressa", "andressa@email.com")
influencer_famosa = Influencer("Bruna", "bruna@email.com", 5000)
moderadora = Administrador("Joana", "joana@email.com")

#Chamando os métodos
usuario_comum.postar()

influencer_famosa.postar()

moderadora.banir_usuario("Carlos")