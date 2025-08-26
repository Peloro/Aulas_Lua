# ARRAY: LISTA DE ITENS
# Uma lista é uma coleção de itens que podem ser de tipos diferentes.
# Listas são mutáveis, ou seja, seus itens podem ser alterados após a criação
# Itens em uma lista são indexados, começando do índice 0

# CRIAÇÃO DE UMA LISTA
frutas = ["maçã", "banana", "laranja", "uva"]

# ACESSANDO ITENS DA LISTA
print(frutas[0])  # Acessa o primeiro item (maçã)
print(frutas[2])  # Acessa o terceiro item (laranja)
print(frutas[-1]) # Acessa o último item (uva)

# MODIFICANDO ITENS DA LISTA
frutas[1] = "abacaxi"  # Altera o segundo item para abacaxi
print(frutas)

# ADICIONANDO ITENS À LISTA
frutas.append("manga")  # Adiciona manga ao final da lista
print(frutas)

# REMOVENDO ITENS DA LISTA
frutas.remove("laranja")  # Remove laranja da lista
print(frutas)

# PERCORRENDO ITENS DA LISTA COM FOR
for fruta in frutas:
    print("Eu gosto de", fruta)

# PERCORRENDO ITENS DA LISTA COM INDICES
for i in range(len(frutas)):
    print(f"Fruta no índice {i} é {frutas[i]}")

# TAMANHO DA LISTA
print("Número de frutas na lista:", len(frutas))

# VERIFICANDO SE UM ITEM ESTÁ NA LISTA
if "uva" in frutas:
    print("Uva está na lista de frutas")

if "laranja" not in frutas:
    print("Laranja não está na lista de frutas")

# ORDENANDO A LISTA
frutas.sort()  # Ordena a lista em ordem alfabética / crescente
print("Frutas ordenadas:", frutas)

# REVERTENDO A ORDEM DA LISTA
frutas.reverse()  # Inverte a ordem dos itens na lista / decrescente
print("Frutas em ordem reversa:", frutas)

# LIMPAR A LISTA
frutas.clear()  # Remove todos os itens da lista
print("Lista de frutas após limpar:", frutas)
