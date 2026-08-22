pares = [] # lista dos pares
impares = [] #lista dos impares

for c in range(0, 20): #laço de 20 
    novo_numero = int(input(f'Digite o {c+1}: ')) # variavel que recebe novo número

    if novo_numero % 2 == 0: #teste de resto de divisão 
        pares.append(novo_numero) #adiciona a lista de pares 
    else:
        impares.append(novo_numero) #adiciona a lista de impares

print(f'Pares: {pares} | Há {len(pares)} números pares')
print(f'Impares: {impares} | Há {len(impares)} número impares')


