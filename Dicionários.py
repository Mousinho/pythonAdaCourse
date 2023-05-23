# Dicionários

# Criando

dicionario = {}
dicionario = dict()
dicionario = {"nome": "pedro", "Idade": 26,"Altura": 1.74}

print(dicionario)
print(dicionario["Idade"])

# Adicionando elementos

dicionario["Programador"] = True
print(dicionario)

dicionario["Altura"] = 2
print(dicionario)

# Iterando

for i in dicionario:
    print(i, dicionario[i])

# Testando a existência da chave

print("peso" in dicionario)
print("Idade" in dicionario)