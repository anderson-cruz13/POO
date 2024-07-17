# __dict__ e varis para atributos de instância
# métodos os quais os dados da classe especifica estão armazenados
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

# Criando a instância de classe Pessoa
p1 = Pessoa("João", 35)

# Obtendo os dados da instância utilizando __dict__
# Também é possível obter por dados = var(p1)
dados = p1.__dict__

# Criando nova instância utilizando os dados desempacotados
p2 = Pessoa(**dados)

print(p2.nome, p2.idade) # Itens desempacotados

#print(p1.__dict__) # Aqui é possivel wr
#print(vars(p1)) # Aqui somente r