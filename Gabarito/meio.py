# Faça um programa para ler n números inteiros e armazene numa lista, retorne o valor do meio dessa lista
# Se a lista tiver tamanho par, retorne a média dos dois valores do meio
# Exemplo: [1, 2, 3, 4, 5] -> 3
# Exemplo: [1, 2, 3, 4] -> (2 + 3) / 2 = 2.5

numeros = []

# Quantidade de numeros que se quer colocar na lista
quantidadeNumeros = int(input("Quantos números você deseja testar: "))

# Preencher a lista com numeros usando for loop
for i in range(quantidadeNumeros):
    numero = int(input(f"Digite o {i + 1}º número a ser digitado: "))
    numeros.append(numero)

meio = quantidadeNumeros // 2

# Se a quantidade de numeros for par (resto da divisão por 2 for 0):
if quantidadeNumeros % 2 == 0:
    print(f"{numeros} -> ({numeros[meio]} + {numeros[meio - 1]}) / 2 = {(numeros[meio] + numeros[meio - 1]) / 2}")

# Se a quantidade de numeros não for par (for ímpar)
else:
    print(f"{numeros} -> {numeros[meio]}")