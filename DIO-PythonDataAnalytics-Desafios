
#Desafio 01:

quantidade_passos = int(input())

#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

if quantidade_passos > 0:
  for passos in range(quantidade_passos):
    passos += 1
    if passos > 1:
        print(f"Explorador: {passos} passos") 
    else:
        print(f"Explorador: {passos} passo")
elif quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")

#Desafio 02:

itens = []

#TODO: Solicite os itens ao usuário

for i in range(3):
    itens.append(str(input()))

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")

#Desafio 3

capacidade_atual, aumento_percentual = map(int, input().split())

#TODO: Calcule a nova capacidade do disco de Mithril

nova_capacidade = capacidade_atual + (capacidade_atual * (aumento_percentual / 100))

#TODO: Imprima a nova capacidade

print(int(nova_capacidade))
