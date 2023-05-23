# Criando Funções

# Função Inicial

def saudacao():
    
    print("Seja bem vindo(a)!")
    print("Olá, é um prazer ter você fazendo parte desse curso!")

saudacao()

# Funçãoa com parâmetros

def saudacao(nome, curso):
    
    print(f"Seja bem vindo(a), {nome}!")
    print(f"Olá, é um prazer ter você fazendo parte do curso {curso}!")

saudacao("Pedro","Ruby")

# Função com parâmetros default

def saudacao(nome, curso="Python"):
    
    print(f"Seja bem vindo(a), {nome}!")
    print(f"Olá, é um prazer ter você fazendo parte do curso {curso}!")

saudacao("Pedro")

# Funções com retorno

def soma (n1,n2):
    return n1 + n2

resultado = soma(4,3)

print("O resultado da soma é: ",resultado)

def calculator (n1,n2,operation = "+"):
    if operation == "+":
        return n1+n2
    elif operation == "-":
        return n1-n2
    elif operation == "*":
        return n1*n2
    elif operation == "/":
        return n1/n2
resultado = calculator(34,2,"/")

print(resultado)
