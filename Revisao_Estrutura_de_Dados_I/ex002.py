maior_numero = pos_menor = pos_maior =  0 # declarando as variavéis
numeros = [] #lista que vai comportar os números

for c in range(0, 10): #laço de repetição 0 a 10
    novo_numero = int(input('Digite o novo número: ')) # variável que recebe o novo número
    if c == 0: # se for o primeiro laço atribui a nova entrada como menor número
        menor_numero = novo_numero

    else: # caso não seja o primeiro laço faz a comparação do novo com o menor 
        if menor_numero > novo_numero:
            menor_numero = novo_numero
            pos_menor = c #armazena a posição do menor

    if novo_numero > maior_numero: #comparação do maior com o novo
        maior_numero = novo_numero
        pos_maior = c #armazena a posição do maior 

    
    numeros.append(novo_numero) #adiciona ao fim da lista 

print(f'Lista de números adicionados: {numeros}')

print(f'Maior número: {maior_numero} Posição na lista : {pos_maior} ')
print(f'Menor número: {menor_numero} Posição na lista {pos_menor}')

