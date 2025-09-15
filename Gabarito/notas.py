# Faça um programa para ler a nota da prova de n alunos e armazene numa lista, calcule e imprima a media geral
# Depois, imprima a quantidade de alunos com nota acima da média 5
# Exemplo: [7, 8, 9, 6, 5] -> (7 + 8 + 9 + 6 + 5) / 5 = 7.0 -> 4 alunos acima da média
# -> == próxima linha

# Quantidade de notas que se quer colocar na lista
quantidadeNotas = int(input("Quantas notas deseja inserir: "))

# Soma das notas e quantidade de alunos acima da média (inicializados em 0)
somaNotas = 0.0
alunosAcimaMedia = 0

# Para cada nota, ler a nota, somar na soma total e verificar se está acima da média
for i in range(quantidadeNotas):
    nota = float(input(f"Digite a {i + 1}º nota: "))
    somaNotas += nota
    if nota >= 5:
        alunosAcimaMedia += 1

# Calcular a média geral
mediaGeral = somaNotas / quantidadeNotas

# Imprimir os resultados
print(f"A média geral da turma foi de {mediaGeral:.2f}")
print(f"{alunosAcimaMedia} alunos ficaram acima da média")



