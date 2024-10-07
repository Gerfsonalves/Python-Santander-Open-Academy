# Listas
frutas = ["maçã", "banana", "laranja"]

# Para acessar os elementos de uma lista.
print(frutas[0])
print(frutas[1])
print(frutas[2])

# Você também pode acessar os elementos a partir do final da lista utilizando índices negativos.
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

# Métodos de listas
# append(elemento): adiciona um elemento ao final da lista.
# insert(indice, elemento): insere um elemento em uma posição específica da lista.
# remove(elemento): remove a primeira ocorrência de um elemento na lista.
# pop(indice): remove e retorna o elemento em uma posição específica da lista.
# sort(): ordena os elementos da lista em ordem ascendente.
# reverse(): inverte a ordem dos elementos na lista.
frutas = ["maçã", "banana", "laranja"]


frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]


fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"


frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]

# Listas de compreensão
# Neste exemplo, é criada uma nova lista chamada quadrados, que contém os quadrados dos números pares da lista números. A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]

# Tuplas
# Para criar uma tupla, encerre os elementos entre parênteses:
# Criação e acesso
ponto = (3, 4)
# Para acessar os elementos de uma tupla, utilize o índice do elemento entre colchetes, similar às listas:
print(ponto[0])

print(ponto[1])


# count(elemento): devolve o número de vezes que um elemento aparece na tupla.
# index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca.
# len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.
# Métodos de tuplas
minha_tupla = (1, 2, 3, 2, 4, 2)


print(minha_tupla.index(2))   # Saída: 1

print(minha_tupla.index(2, 2))  # Saída: 3

print(minha_tupla.index(2, 2, 4))  # Saída: 3

# Dicionários
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}
print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])    # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"

# Métodos de dicionários
# keys(): retorna uma visualização de todas as chaves do dicionário.
# values(): retorna uma visualização de todos os valores do dicionário.
# items(): retorna uma visualização de todos os pares chave-valor do dicionário.
# update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])

print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])


# Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])
print(pessoa.items())


pessoa.update({"profissao": "Engenheiro"})
# Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}
print(pessoa)


# Conjuntos (set)
frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])
# Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

# Métodos de conjuntos
# add(elemento): adiciona um elemento ao conjunto.
# remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
# discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
# clear(): remove todos os elementos do conjunto.
frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()
