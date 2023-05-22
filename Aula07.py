#Listas

#Antes
nota1 = 7
nota2 = 4.4
nota3 = 8.3

#Com lista

notas = [7,4.4,8.3]

#Criando listas
lista = []     # Vazia
lista = list() # Vazia
lista = [26,"Pedro",True,3.1234] # Tipos
Lista_de_Listas = [10,[1,2,3]]   # Lista dentro de lista

#Indexação e Slices {Fatiamento}

lista = [10,"Pedro",3.1245,True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#Slices

lista = [10,50,30,25,23,543,654,23]

print(lista[3:6])
print(lista[2:6:2])

#Interação com FOR

for elemento in lista:
    print(elemento)

#Utilizando tamanho da lista

print("Comprimento da lista ",len(lista))

for i in range(len(lista)):
    
    print(lista[i])
