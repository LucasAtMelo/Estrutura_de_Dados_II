# 1. Definição da "Struct" Funcionario
class Funcionario:
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

# Lista para armazenar os dados e constante para o número de cadastros
funcionarios = []
TOTAL_CADASTROS = 10 

# ==========================================
# ETAPA 1: Cadastro dos Funcionários
# ==========================================
print(f"--- Sistema Integrado: Cadastro de {TOTAL_CADASTROS} Funcionários ---")
for i in range(TOTAL_CADASTROS):
    print(f"\n[ Funcionário {i+1} ]")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cargo = input("Cargo: ")
    salario = float(input("Salário: R$ "))
    
    funcionarios.append(Funcionario(nome, idade, cargo, salario))

# ==========================================
# ETAPA 2: Processamento de Dados
# ==========================================
soma_salarios = 0.0
maior_salario = 0.0
nome_maior_salario = ""

print("\n" + "="*65)
print("                      LISTA DE FUNCIONÁRIOS")
print("="*65)

# Varrendo a lista para mostrar todos e calcular os totais
for f in funcionarios:
    # Exibe todos os funcionários formatados em colunas
    print(f"Nome: {f.nome:12} | Idade: {f.idade:2} | Cargo: {f.cargo:12} | Salário: R$ {f.salario:8.2f}")
    
    # Acumula o salário para a média
    soma_salarios += f.salario
    
    # Verifica quem tem o maior salário
    if f.salario > maior_salario:
        maior_salario = f.salario
        nome_maior_salario = f.nome

# Calcula a média salarial
media_salarial = soma_salarios / TOTAL_CADASTROS

# ==========================================
# ETAPA 3: Relatório e Estatísticas
# ==========================================
print("\n" + "="*65)
print("                      ESTATÍSTICAS")
print("="*65)
print(f"-> Maior salário: {nome_maior_salario} recebendo R$ {maior_salario:.2f}")
print(f"-> Média salarial da empresa: R$ {media_salarial:.2f}")

print("\n--- Funcionários com salário ACIMA da média ---")
# Precisamos de um segundo laço para comparar o salário de cada um com a média final já calculada
encontrou_acima_media = False
for f in funcionarios:
    if f.salario > media_salarial:
        print(f"- {f.nome} (R$ {f.salario:.2f}) - Cargo: {f.cargo}")
        encontrou_acima_media = True

if not encontrou_acima_media:
    print("Nenhum funcionário recebe acima da média (todos ganham o mesmo valor).")