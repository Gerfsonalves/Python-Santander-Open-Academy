# Loops
# Neste exemplo, o loop for itera sobre a lista frutas. Em cada iteração, a variável fruta assume o valor de um elemento da lista, e o bloco de código dentro do loop é executado. Neste caso, cada fruta é impressa em uma linha separada.
# For

frutas = ["maçã", "banana", "laranja"]


for fruta in frutas:
    print(fruta)
#
# While
# O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira.
# Neste exemplo, o loop while é executado enquanto a variável contador for menor que 5.
contador = 0


while contador < 5:

    print(contador)
    contador += 1

# Controle de loops
# A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição. Quando um break é encontrado, o loop é interrompido.
# Break
contador = 0


while True:

    print(contador)
    contador += 1

    if contador == 5:
        break

# Neste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range(). Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %. Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, fazendo com que o restante do bloco de código seja pulado e passando para a próxima iteração do loop.
# Continue
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

# A instrução pass é uma operação nula que não faz nada. Neste exemplo, o loop for itera sobre os números de 0 a 4, mas nenhuma ação é realizada dentro do loop devido à instrução pass. Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.
# Pass
for i in range(5):
    pass
