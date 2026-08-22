numeros = [] #lista para armazenar os números

for c in range(0, 10): # laço de 0 a 10
    novo_numero = int(input(f'Digite o {c + 1} número: ')) # variavel que recebe o input do novo número
    numeros.append(novo_numero) # função de array que adiciona o número ao final da lista 

print(numeros) # lista completa 