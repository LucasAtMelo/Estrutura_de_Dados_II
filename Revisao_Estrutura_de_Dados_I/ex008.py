# 1. Criando a "Struct" Produto usando uma Classe
class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

# Lista para armazenar os produtos cadastrados
estoque = []

# 2. Cadastrar cinco produtos
print("--- Cadastro de Produtos ---")
for i in range(5):
    print(f"\nProduto {i+1}:")
    nome = input("Nome: ")
    codigo = int(input("Código: "))
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade: "))
    
    # Instanciamos o Produto (criamos a struct) e adicionamos na lista
    novo_produto = Produto(nome, codigo, preco, quantidade)
    estoque.append(novo_produto)

# Variáveis de controle para achar o maior valor
maior_valor = 0
produto_maior_valor = ""

print("\n" + "="*40)
print("       RELATÓRIO DE ESTOQUE")
print("="*40)

# 3. Processar e mostrar os dados
for p in estoque:
    # Fórmula: valor em estoque = preço × quantidade
    valor_total_produto = p.preco * p.quantidade
    
    # Mostrando os dados de cada produto
    print(f"Nome: {p.nome} | Código: {p.codigo}")
    print(f"Preço: R$ {p.preco:.2f} | Qtd: {p.quantidade} un.")
    print(f"Valor total em estoque: R$ {valor_total_produto:.2f}")
    print("-" * 40)
    
    # 4. Verificar se este produto tem o maior valor em estoque
    if valor_total_produto > maior_valor:
        maior_valor = valor_total_produto
        produto_maior_valor = p.nome

# Resultado final
print(f"\n=> PRODUTO COM MAIOR VALOR EM ESTOQUE:")
print(f"O produto '{produto_maior_valor}' totaliza R$ {maior_valor:.2f} investidos no estoque.")