#For
'''for i in range(1,11,2):
    print(i)'''

soma = 0

for i in range(1,4):
    nota = float(input(f"Informe a sua nota {i} :")) #fstring
    soma = soma + nota

print(soma / 3)