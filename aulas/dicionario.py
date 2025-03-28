#definido a partir de dois elementos: uma chave e um valor

# dicionario = {"chave": valor} - chave é o incide 

lista =[2,6,9]
lista[1]

dicionario = {"a":3, "b": 9, "c": 15}

dicionario["b"]

#cadastro de nome, idade e cidade


cadastro = [["João", 20, "São Paulo"],
["Maria", 30, "Rio de Janeiro"],
["Marta", 15, "Salvador"]]

cadastro_dict = {"nomes": ["José","Maria","Marta"],

                "idades": [20, 30, 15],

                "cidades": ["SP", "RJ", "Salvador"]}

cadastro_dict["nomes"]

cadastro_dict["nomes"].append("Joaquim")
cadastro_dict["idades"].append(26)
cadastro_dict["cidades"].append("Santo André")

cadastro_dict["nomes"]


import pandas as pd

df = pd.DataFrame(cadastro_dict)

df