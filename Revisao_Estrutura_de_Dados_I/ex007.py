# Cria uma matriz 4x3 preenchida com zeros
notas = [[0.0 for _ in range(3)] for _ in range(4)]

# 1. Leitura das notas
for i in range(4):
    print(f"\nInserindo notas do Aluno {i+1}:")
    for j in range(3):
        notas[i][j] = float(input(f"Nota da P{j+1}: "))

# 2. Exibição da matriz formatada
print("\n" + "-"*30)
print("          P1    P2    P3")

for i in range(4):
    print(f"Aluno {i+1} ", end="")
    for j in range(3):
        # :5.1f formata o número com 1 casa decimal e garante 5 espaços de largura para alinhar
        print(f"{notas[i][j]:5.1f} ", end="")
    print() # Quebra a linha ao final das 3 notas do aluno
print("-"*30)