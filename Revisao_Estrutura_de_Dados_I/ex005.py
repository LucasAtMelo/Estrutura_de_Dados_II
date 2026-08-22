# Inicializa uma matriz 3x3 vazia
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0

# 1. Ler os valores
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))

# Define o maior valor inicial como o primeiro item lido (evita bugs com números negativos)
maior = matriz[0][0]

print("\n--- Matriz 3x3 ---")
# 2. Mostrar a matriz, calcular a soma e encontrar o maior valor
for i in range(3):
    for j in range(3):
        valor_atual = matriz[i][j]
        
        print(f"{valor_atual:4}", end="") # :4 ajuda a alinhar as colunas
        soma += valor_atual
        
        if valor_atual > maior:
            maior = valor_atual
    print() # Quebra a linha ao final de cada linha da matriz

# 3. Mostrar resultados
print(f"\nSoma de todos os elementos: {soma}")
print(f"Maior valor: {maior}")