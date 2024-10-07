# Definição e chamada de funções
# Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses:
def saudacao():
    print("Olá, mundo!")


saudacao()  # Imprime "Olá, mundo!"

# As funções podem aceitar parâmetros
# Parâmetros e argumentos


def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("João")  # Imprime "Olá, João!"
saudacao("Maria")  # Imprime "Olá, Maria!"

# As funções podem retornar valores usando a palavra-chave return.
# Valores de retorno


def soma(a, b):
    return a + b


resultado = soma(3, 4)
print(resultado)  # Imprime 7

# São funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.
# Funções anônimas (lambda)
# quadrado = lambda x: x ** 2
# print(quadrado(5))  # Imprime 25


def quadrado(x): return x ** 2


print(quadrado(5))  # Imprime 25

# As variáveis definidas dentro de uma função têm um escopo local,
# o que significa que só são acessíveis dentro da função.
# Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global
# e podem ser acessadas de qualquer parte do programa.
# Escopo das variáveis (local vs. global)


def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20

# --------   print(variavel_local) --------
# Gera um erro, a variável não está definida neste escopo.

# Documentação de funções (docstrings)
# É uma boa prática documentar nossas funções utilizando docstrings.


def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura

# Funções com número variável de argumentos
# Python permite definir funções que aceitem um número variável de argumentos.
# Isso é feito utilizando o operador * antes do nome do parâmetro.


def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22
