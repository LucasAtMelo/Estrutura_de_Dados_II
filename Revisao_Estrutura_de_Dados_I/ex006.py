# Cria uma matriz 4x4 vazia
matriz = [[0 for _ in range(4)] for _ in range(4)]

# 1. Ler os valores (simulando a entrada do exemplo)
print("Digite os valores da matriz 4x4:")
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Valor [{i}][{j}]: "))

# 2. Processar a diagonal principal
diagonal = []
soma = 0

# Como a diagonal principal tem linha == coluna, precisamos de apenas 1 loop
for i in range(4):
    valor_diagonal = matriz[i][i]
    diagonal.append(str(valor_diagonal)) # Converte para string para facilitar o print
    soma += valor_diagonal

# 3. Mostrar os resultados no formato solicitado
print("\nDiagonal principal:")
print(" ".join(diagonal))

print("\nSoma:")
print(soma)