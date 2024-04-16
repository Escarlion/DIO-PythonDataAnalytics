def Titulo(texto):
    print("\n",texto.center(30,"-"),"\n")

#CONVERSÃO DE TIPOS

Titulo("Conversão de tipos")

valor_int = 2
valor_float = 3.5
valor_string = "2"

print(f"valores originais: {valor_float} | {valor_int} | {valor_string}")
#usa constructs p mudar o valor da variavel 
print(f"valores alterados: {int(valor_float)} | {float(valor_int)} | {float(valor_string)}")

#ENTRADA E SAIDA

Titulo("Entrada e saida")

nome = "Pedro"
sobrenome = "Matias"

#end = adiciona uma string no final de cada linha
#sep = adiciona uma string entre cada variavel

print(nome, sobrenome, sep=" | ")

#nome = input("Digite seu nome: ")
#sobrenome = input("Digite seu sobrenome: ")

print(f"Olá {nome} {sobrenome}", end=".\n")

#OPERADORES 

# ** = exponenciação (^)
# % = modulo (resto da divisão)
# utiliza AND ou OR inves de && e || 
# utiliza NOT para negação

Titulo("Operadores")

valor1 = 10
valor2 = 2
valor3 = 5

print(valor1 > valor2 and valor2 < valor3) 
print(not valor1 != valor2) #originalmente retornaria true, porem nega o resultado usando NOT

#Identidade: usando IS e NOT IS, é possivel checar se 2 objetos ocupam a mesma região de memoria 

print(valor1 is 10)

#Associação: checa se algo está ou não em uma sequencia usando IN e NOT IN

lista_generos = ["romance", "terror", "ação"]
busca = "terror"

print(f"O genero {busca} está na lista de generos? ({lista_generos}) ",busca in lista_generos)

#Tambem é possivel encontrar se uma palavra está em uma frase 

frase = "Eu gosto de frango"
palavra = "frango"

print(f"A palavra {palavra} está na frase {frase}? ",palavra in frase)

#ESTRUTURA DE DECISÃO E REPETIÇÃO

Titulo("Estrutura de decisão e repetição")

#Identação: python não utiliza {} e similares, assim os blocos são determinados usando : e a identação

saldo = 1000
saque = 500

def sacar(valor):
    if valor <= saldo:
        print(f"Valor sacado: {valor}")
    else:
        print("Saldo da conta insuficiente.")

sacar(saque)

#Utiliza ELIF inves de ELSE IF

status= "Sucesso" if saldo >= saque else "Falha" #If Ternario 

print(status)

ABC = ["A", "B", "C"]

for letra in ABC:
    print(letra)

print(list(range(0 , 11, 2)))

#MANIPULAÇÃO DE STRINGS

Titulo("Manipulação de strings")

#maiscula, minuscula e titulo

exemplo = "pYtHOn"

print(exemplo.upper())
print(exemplo.lower())
print(exemplo.title())

#remover espaços vazios 

exemplo = " Python "

print(exemplo.strip()) #retira todos os espaços 
print(exemplo.lstrip()) #retira da esquerda
print(exemplo.rstrip()) #retira da direita 

#junções e centralização 

exemplo = "Python"

print(exemplo.center(12,"#")) #quantidade de caracteres, caracteres que vão ser usados para centralizar (começo e fim), caso nn coloque o ultimo campo, é usado espaço vazio (recomendado usar numeros pares)
print("-".join(exemplo)) #coloca o primeiro campo entre cada caracter do segundo campo (exclui a primeira e ultima letra)

#interpolação de variaveis (o recomendado é sempre utilizr f"")

#Old Style (%)
# %s = string, %d = int, %f = float

exemplo1 = "Pedro"
exemplo2 = 24

print("Meu nome é %s, eu tenho %d anos." % (exemplo1, exemplo2))

#Format ({} e .format)

print("Meu nome é {}, eu tenho {} anos.".format(exemplo1, exemplo2))

# f-string (f"")

print(f"Meu nome é {exemplo1}, eu tenho {exemplo2} anos.")

#f-string com formatação 

exemplo3 = 2500.5798

print(f"Meu nome é {exemplo1}, eu tenho {exemplo2} anos e ganho {exemplo3:.2f}") #valor fica arredondado 

#fatiamento

exemplo = "Pedro Souza Nunes"

print(exemplo[0]) #apenas a 1a letra
print(exemplo[:5]) #para na 5a letra
print(exemplo[6:]) #começa na 6a letra
print(exemplo[6:10]) #começa na 6a e termina na 10a
print(exemplo[0:5:2]) #começa na 1a, termina na 5a e pula 1 letra
print(exemplo[:: -1]) #espelhado

def DividirNome(nome_completo):
    i = 0
    for letra in nome_completo:
        if letra == " ":
            break
        i += 1
    return i

print(DividirNome(exemplo))
print(f"""Nome: {exemplo[:DividirNome(exemplo)]}
Sobrenome: {exemplo[DividirNome(exemplo) + 1:]}""" )

#LISTAS

Titulo("Listas")

print(list("Pyhton")) #usar list() em uma string, retorna todos os char dela

dados = ["Pedro", "Mathias Soares", 85458, 119652338755, 9.5, "São Paulo - SP"] #(ficticio) uma lista pode armazenar valores de diferentes tipos
print(dados)
print(f"Nome: {dados[0]}\nSobrenome: {dados[1]}")

print(dados[2:]) #fatiamento também funciona com lista

matriz = [
    ["a", "b", "c"],
    [1,2,3],
    [1,"b,3"]
]

print(f"0,1= {matriz[0][1]}")

for indice, dado in enumerate(dados): #enumerate retorna um indice para cada valor
    print(f"{indice}o: {dado}")

#filtro

numeros = [1,2,3,4,5,6]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

dados.append("Solteiro") #APPEND adiciona um valor a lista
print(dados)

dados.remove("Solteiro") #REMOVE retira o valor de uma lista, podendo passar o valor pelo indice ou pelo valor em si
print(dados)

dados.clear() #limpa

dados = [1,2,3]
copia = dados.copy() #cria uma copia dos valores da lista naquele momento
print(copia)

dados.append(1)
print(dados.count(1)) #retorna a quantidade de vezes que algum valor aparece na lista

dados = [1,2,3]
novos_dados = [2,1]
dados.extend(novos_dados) #funde a lista com os valores de uma lista nova
print(dados)

print(dados.index(1)) #mostra a posição de algum valor (apenas na primeira vez que ele aparecer)

print(dados.pop()) #retira o ultimo elemento da lista
print(dados.pop(1)) #tambem pode retirar em algum indice especifico 

dados = ["Primeiro", "Segundo", "Terceiro"]
dados.reverse() #inverte a lista
print(dados)

dados = ["d", "c", "z", "a", "g"]
dados.sort() #organiza em ordem alfabetica 
print(dados)
dados.sort(reverse=True) #faz a organização ao contrario 
print(dados)
dados = ["de", "uga uga", "aga"]
dados.sort(key=lambda x: len(x)) #ordena do menor para o maior
print(dados)
dados.sort(key=lambda x: len(x), reverse=True) #ordena do menor para o maior e inverte
print(dados)

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])

#TUPLAS

Titulo("Tuplas")
#tuplas funcionam como lista, porem são imutaveis. Os valores são determinados usando "()" inves de "[]" e deve-se ter "," no final do conjunto de valores
#fora isto, é possivel localizar dados usando as mesmas funções de uma lista comum, apenas não sendo possivel alterar seus valores

palavra = "Python"
letras = tuple(palavra)
pais = ("Brasil",) #sempre usar , no final dos valores de uma tupla, pode gerar problemas com o Python
print(letras, pais)

#Conjuntos

Titulo("Conjuntos")
#não é possivel acessar os valores de um conjunto por meio de indexação, assim precisando transforma-lo em uma lista 

conjunto = set(["Pedro", "Moises","Adolfo", "Pedro"]) #elimina duplicatas, não aceita objetos como valor e não garante a ordem
print(conjunto)

numeros = {1, 1, 2, 3, 2, 4} #utilizar "{}" cria automaticamente um conjunto sem precisar usar o SET
print(numeros)

numeros = list(numeros)
print(numeros[1])

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

print(conjunto_a.union(conjunto_b)) #UNION junta os valores de 2 conjuntos, eliminando duplicatas 
print(conjunto_a.intersection(conjunto_b)) #INTERSECTION mostra apenas os valores que são duplicados em 2 conjuntos 
print(conjunto_a.difference(conjunto_b)) #DIFFERENCE mostra tudo o que tem no conjunto X e não tem no conjunto Y
print(conjunto_a.symmetric_difference(conjunto_b)) #SYMMETRIC DIFFERENCE mostra tudo o que é diferente nos dois conjuntos
print(conjunto_a.issubset(conjunto_b)) #ISSUBSET retorna um valor booleando dizendo se os elementos de X estão TODOS ou não em Y
print(conjunto_a.issuperset(conjunto_b)) #ISSUPERSET retorna um valor booleando dizendo se os elementos de X NÃO estão TODOS em Y
print(conjunto_a.isdisjoint(conjunto_b)) #ISDISJOINT retorna um valor booleano se todos os elementos dos conjuntos são diferentes

conjunto_a.add(5) #adiciona um novo elemento caso ele ainda não exista no conjunto
print(conjunto_a)
conjunto_a.add(2)
print(conjunto_a)

conjunto_a.discard(2) #retira um valor desejado (não dá erro caso o valor não exista)
print(conjunto_a)

#também é possivel usar CLEAR, POP e COPY

#DICIONARIOS

Titulo("Dicionários")

'''
dados = {"nome": "Pedro", "Idade": 20} #primeiro passa a chave e depois o valor
dados = dict(nome="Pedro", Idade= 28) #mesma forma de criar um dicionario 
dados["Sobrenome"] = "Matias" #adiciona uma nova chave com o valor desejado

print(dados["Sobrenome"]) #retorna o valor da chave

contatos = { 
    "pauloMatias@gmail.com": {"Nome": "Paulo", "Sobrenome": "Matias"}, #usa o email como chamave e armazena os valores do dicinario nele, funciona como matriz
    "pedroMatos@gmail.com": {"Nome": "Pedro", "Sobrenome": "Matos"}
} 

print(contatos["pauloMatias@gmail.com"]["Nome"]) #metodo de buscar os dados, primeiro a chave, depois o valor desejado

#é possivel utilizar COPY, 



dict.fromkeys(["Nome", "Telefone"]) #cria chaves em um dicionario sem adicionar nenhum valor
dict.fromkeys(["Nome", "Telefone"], "vazio") #adiciona as chaves com um valor padrão

dict.get("Key") #retorna o valor da chave, caso a chave não exista, retorna um valor none (se não usar get, pode dar erro caso nn aja chave)
dict.get("Key", {}) #retorna certo valor caso a chave não exista (caso exista, ela ignora o 2o atributo)

dict.items() #retorna uma lista de tuplas com os dados

dict.keys() #retorna apenas as chaves do dict

dict.pop("Key") #retira o ultimo valor de uma chave
dict.popitem() #retira o ultimo valor do dict

dict.setdefault("Key", "Atributo") #caso a key não exista no dicionario, irá adiciona-la junto do atributo como seu valor (caso a chave exista, adiciona o valor)

dict.update({"key" : {"key": "atributo"}}) #atualiza um dicionario colocando este novos valores (muda completamente)

dict.values() #retorna apenas os valores de um dict

"key" in dict #verifica se certa chave existe em um dicionario (retorna bool)

del dict["key"]["Value"] #retira o valor de uma chave ou a chave inteira
'''
#FUNÇÕES

Titulo("Funções")

def func(): #funções são criadas usando DEF
    print("Minha função")

def func(texto):
    print(texto)

print(func("Minha função"))

def dados(nome, sobrenome, idade):
    print(f"{nome} | {sobrenome} | {idade}")

print(dados("Pedro", "Matias", 18))
print(dados(nome="Pedro", sobrenome="Matias", idade=18)) #é possivel passar os valores fazendo referencia as chaves da função, assim evitando erros pelo compilador
#func(**{"nome": "Pedro", "sobrenome": "Matias", "idade": 18}) #passa os valores em forma de dict

 #*args = tuplas **kwargs = dict

def poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"\n{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

poema("Segunda, 15 de Abril de 2024", "Antes adeus do que olá.", "Eu quero te olhar mas tenho medo de te ver.", "Eu sinto sua falta", autor="Pedro Matias", ano=2077) 
#o *args recebe todos os valores que são passados apenas utilizando a ",", pois entra como tupla, após isso, os valores atribuidos como key=value, entra no campo de dict

#ATRIBUTOS: a função por padrão recebe valores posicionais, ao colocar "/" no campo de atributos, o que vier depois disso são atribudos que só podem
#   ser adicionados usando keyword (key=value) ou posicional, e após colocar "*" apenas por keyword

def dados(nome, sobrenome, /, idade, *, cep): #ao utilizar a /, os valores antes dela são OBRIGATORIAMENTE apenas posicionais 
    print(nome,sobrenome,idade,cep)

dados("Pedro", "Matias", 18, cep="08947-568")

def soma(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def conta(a,b,func): #é possivel criar funções que recebam outras funções como atributo
    return  func(a,b)

print(f"Operação com soma: {conta(1,5,soma)}") #não é necessario chamar a função usando "()"
print(f"Operação com subtração: {conta(1,5,subtrair)}")

money = 500

def more_money():
    global money 
    money += 500
    print(money)

more_money()


