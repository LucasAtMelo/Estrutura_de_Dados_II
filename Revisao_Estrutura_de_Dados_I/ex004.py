numeros = [] #lista dos números

for c in range(0, 10): #loop de 0 a 10
    novo_numero = int(input(f'Digite o {c + 1} valor: ')) # recebe o novo número
    numeros.append(novo_numero) #adiciona ao fim da lista 

print(f'Vetor original: {numeros}') 
print(f'Vetor invertido: {numeros[::-1]}') #usa fatiamento para mostrar o vetor invertido