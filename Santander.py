# IF
idade = 18


if idade >= 18:
    print("Você é maior de idade.")

# IF-ELSE
idade = 15


if idade >= 18:
    print("Você é maior de idade.")

else:
    print("Você é menor de idade.")


# IF-ELIF-ELSE
nota = 85


if nota >= 90:
    print("Excelente")

elif nota >= 80:
    print("Muito bom")

elif nota >= 70:
    print("Bom")

else:
    print("Precisa melhorar")

# Loops
# For
frutas = ["maçã", "banana", "laranja"]


for fruta in frutas:
    print(fruta)

# While
contador = 0


while contador < 5:

    print(contador)
    contador += 1

# Controle de loops
# Break
contador = 0


while True:

    print(contador)
    contador += 1

    if contador == 5:
        break

# Continue
# Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

# Pass
# A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.
# A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.
for i in range(5):
    pass

#
