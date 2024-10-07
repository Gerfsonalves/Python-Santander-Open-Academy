# Entrada de dados do usuário
# Para obter informações do usuário durante a execução do programa, podemos utilizar a função input().
# Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")


print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")

# A função input() sempre retorna uma cadeia de texto.
# Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes,
# deve realizar uma conversão explícita utilizando funções como int() ou float().
idade = int(input("Insira sua idade: "))


if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Saída de dados
# Podemos utilizar a f-string (formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.
nome = "Juan"
idade = 25


print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

# Leitura de arquivos
# Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo de leitura ("r").
# Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Escrita de arquivos
# Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open().
# Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

# OBS:
# Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
