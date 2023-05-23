#Estrutura Condicionais

idade = int(input ("Qual a sua idade?"))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

print("########")
'''''
nota01 = float(input("Quanto você tirou na sua 1 prova?"))
nota02 = float(input("Quanto você tirou na sua 2 prova?"))
media = (nota01+nota02)/2

if media >= 7:
    print("Você foi aprovado!")
elif media <= 5:
    print("Recuperação")
else:
    print("Você não foi aprovado!")
'''
media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print("Aprovado!")
else:
    print("Reprovado")