#Métodos de Listas

lista = [1,3,12,8,2]

# append

print(lista)
lista.append(10)
print(lista)

# Insert

lista.insert(2, 17)
print(lista)

# extend

lista2 = [0,67,75]
lista.extend(lista2)
print(lista)

# pop
lista.pop()
print(lista)

lista.pop(0)
print(lista)

#Remove

lista.remove(2) #Remove o primeiro que ele encontra
print(lista)

# count

print("Quantas vezes aparece 67 na lista ",lista.count(67))

# index

print("Indice do elemento 10 é",lista.index(10))

# sort

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# len

print(len(lista))

# sum

print(sum(lista))

# max e min

print(max(lista))
print(min(lista))