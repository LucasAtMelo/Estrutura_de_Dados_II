# 1. Criando a "Struct" Aluno
class Aluno:
    def __init__(self, nome, idade, nota1, nota2, nota3):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

# Lista para armazenar os alunos
turma = []

# Variáveis de controle para o relatório final
qtd_aprovados = 0
qtd_reprovados = 0
maior_media = -1 # Começa negativa para garantir que a primeira média a substitua
aluno_maior_media = ""

# 2. Cadastrar cinco alunos
print("--- Cadastro de Alunos ---")
for i in range(5):
    print(f"\nAluno {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    # Criamos o objeto e adicionamos à lista
    novo_aluno = Aluno(nome, idade, nota1, nota2, nota3)
    turma.append(novo_aluno)

print("\n" + "="*40)
print("          BOLETIM DA TURMA")
print("="*40)

# 3. Processar os dados: calcular médias e classificar
for aluno in turma:
    # Cálculo da média aritmética
    media = (aluno.nota1 + aluno.nota2 + aluno.nota3) / 3
    
    # Verificação de aprovação
    if media >= 7.0:
        situacao = "Aprovado"
        qtd_aprovados += 1
    else:
        situacao = "Reprovado"
        qtd_reprovados += 1
        
    # Exibir os dados do aluno atual
    print(f"Nome: {aluno.nome} (Idade: {aluno.idade})")
    print(f"Notas: {aluno.nota1:.1f}, {aluno.nota2:.1f}, {aluno.nota3:.1f}")
    print(f"Média: {media:.2f} -> Situação: {situacao}")
    print("-" * 40)
    
    # 4. Verificar se é a maior média da turma
    if media > maior_media:
        maior_media = media
        aluno_maior_media = aluno.nome

# 5. Exibir o relatório final
print("\n=> RELATÓRIO FINAL:")
print(f"Total de Aprovados: {qtd_aprovados}")
print(f"Total de Reprovados: {qtd_reprovados}")
print(f"Aluno com maior média: {aluno_maior_media} (Média: {maior_media:.2f})")