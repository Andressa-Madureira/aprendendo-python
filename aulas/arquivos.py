arquivo = open("ola_mundo.txt", "w", encoding="utf-8")

#Para escrever no arquivo utilizamos o método write()
arquivo.write("olá, pessoal\n Esse é o meu primeiro arquivo em Python")

#Para fechar e salvar os arquivos:
arquivo.close()

#with garante que o arquivo será aberto e fechado

with open("ola_mundo4.txt", "r", encoding="utf-8") as terceiroArquivo:

    terceiroArquivo.write("olá, devsss!\n Terceiro arquivo")


#continuar escrevendo no nosso arquivo
with open("ola_mundo4.txt", "a", encoding="utf-8") as terceiroArquivo:

    terceiroArquivo.write("olá, devsss!, como vocês estão?")

#lê todo o conteudo 
with open("ola_mundo.txt", "r", encoding="utf-8") as f:
   conteudo = f.read()

#conteud.split("\n") pular a linha



