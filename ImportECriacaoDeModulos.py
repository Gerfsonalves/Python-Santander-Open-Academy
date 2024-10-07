# Importar módulos
# Podemos importar um módulo completo ou funções específicas de um módulo.
import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0
"""
Neste exemplo, importa-se o módulo math utilizando a declaração import. 
Em seguida, utiliza-se a função sqrt() do módulo math 
para calcular a raiz quadrada de 25."""

# Neste caso, importa-se apenas a função sqrt() do módulo math,
# o que nos permite utilizá-la diretamente sem ter que precedê-la com o nome do módulo.
""" from math import sqrt


resultado = sqrt(25)
print(resultado)  # Imprime 5.0"""


# Funções e classes de módulos padrão
"""
import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatório)  # Imprime um número inteiro aleatório entre 1 e 10


data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual
"""

# Criar e utilizar módulos personalizados

# meu_modulo.py
"""
def saudar(nome):
    print(f"Olá, {nome}!")


def calcular_soma(a, b):
    return a + b
Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.

import meu_modulo


meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8
"""

# Organização do código em módulos
# podemos ter um módulo operacoes.py que contenha funções relacionadas com operações matemáticas,
# e outro módulo utilidades.py que contenha funções de uso geral.
"""
# operacoes.py
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


# utilidades.py
def imprimir_mensagem(mensagem):
    print(mensagem)


def obter_nome_usuario():
    return input("Digite seu nome: ")
Depois, podemos importar e utilizar essas funções em nosso programa principal.

import operacoes
import utilidades


resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")


nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

"""

# PACOTES
# Criar e utilizar
# criamos um diretório chamado meu_pacote com a seguinte estrutura
"""
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py

"""
# Depois, podemos importar e utilizar os módulos do pacote em nosso programa.
"""
from meu_pacote import modulo1, modulo2


modulo1.funcao1()
modulo2.funcao2()
"""
