# Classe Paciente
class Paciente:
    def __init__(self, nome, idade, estado):
        self.nome = nome
        self.idade = idade
        self.estado = estado

    # Retorna o nível de prioridade (quanto maior, mais prioritário)
    def nivel_prioridade(self):
        if self.estado.lower() in ['crítico', 'critico']:
            return 2
        elif self.idade >= 60:
            return 1
        else:
            return 0

    def __str__(self):
        nivel = self.nivel_prioridade()
        if nivel == 2:
            etiqueta = "CRÍTICO"
        elif nivel == 1:
            etiqueta = "PRIORIDADE (Idade)"
        else:
            etiqueta = "Normal"
            
        return f"{self.nome} - {self.idade} anos - Estado: {self.estado.capitalize()} [{etiqueta}]"

# Classe Node
class Node:
    def __init__(self, paciente):
        self.dado = paciente
        self.proximo = None

# Classe FilaClinica
class FilaClinica:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    # Verifica se a fila está vazia
    def esta_vazia(self):
        return self.inicio is None

    # Retorna o tamanho da fila
    def tamanho(self):
        return self._tamanho

    # Adiciona um paciente na fila respeitando as prioridades
    def adicionar(self, paciente):
        novo = Node(paciente)

        # Se a fila estiver vazia
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            atual = self.inicio
            anterior = None

            # Percorre a fila enquanto a prioridade do paciente na fila
            # for MAIOR OU IGUAL à prioridade do novo paciente.
            # O "igual" garante que pacientes com a mesma prioridade entrem no final do seu grupo (FIFO).
            while atual is not None and atual.dado.nivel_prioridade() >= paciente.nivel_prioridade():
                anterior = atual
                atual = atual.proximo

            # Se 'anterior' for None, significa que o novo paciente tem prioridade
            # maior que o primeiro da fila (insere no início)
            if anterior is None:
                novo.proximo = self.inicio
                self.inicio = novo
            else:
                # Insere no meio ou no final
                novo.proximo = atual
                anterior.proximo = novo
                
                # Se inseriu no final, atualiza o ponteiro 'fim'
                if novo.proximo is None:
                    self.fim = novo
                    
        self._tamanho += 1

    # Atende o primeiro paciente da fila
    def atender(self):
        if self.esta_vazia():
            print("Não há pacientes para atender.")
            return None
            
        paciente = self.inicio.dado
        self.inicio = self.inicio.proximo

        # Se a fila ficou vazia após o atendimento
        if self.inicio is None:
            self.fim = None
            
        self._tamanho -= 1
        print(f"Atendendo: {paciente.nome}")
        return paciente
 
    # Lista todos os pacientes
    def listar(self):
        if self.esta_vazia():
            print("A fila está vazia.")
            return
            
        atual = self.inicio
        print("\n--- FILA DA CLÍNICA ---")
        while atual is not None:
            print(atual.dado)
            atual = atual.proximo
        print("-----------------------")


# TESTANDO O PROGRAMA

fila = FilaClinica()

# Pacientes com diferentes idades e estados
p1 = Paciente("Ana", 25, "estável")       # Normal (Nível 0)
p2 = Paciente("Carlos", 65, "estável")    # Idoso (Nível 1)
p3 = Paciente("Maria", 40, "crítico")     # Crítico (Nível 2)
p4 = Paciente("João", 70, "crítico")      # Crítico e Idoso (Nível 2 - Estado crítico sobrepõe idade)
p5 = Paciente("Pedro", 30, "estável")     # Normal (Nível 0)
p6 = Paciente("Lúcia", 80, "estável")     # Idoso (Nível 1)

# Adicionando os pacientes (a ordem de inserção é misturada de propósito)
fila.adicionar(p1)
fila.adicionar(p2)
fila.adicionar(p3)
fila.adicionar(p4)
fila.adicionar(p5)
fila.adicionar(p6)

# Listando a fila (Deve mostrar: Críticos primeiro, depois Idosos, depois Normais)
fila.listar()

# Mostrando o tamanho
print("\nTamanho da fila:", fila.tamanho())

# Atendendo pacientes
print("\n--- ATENDIMENTO ---")
fila.atender() # Atende Maria (Crítico)
fila.atender() # Atende João (Crítico)
fila.atender() # Atende Carlos (Prioridade Idade)

# Listando novamente para ver como ficou a fila após os atendimentos
fila.listar()
