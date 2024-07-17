# Métodos
# Self (instância) -> Cls (model {classe})
# @classmethod - cls, método de classe
# Recebe a própria clase como parâmetro ao invés de sua instância

# @staticmethod (não usa self, cls) não são muitos úteis em Python

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

    @classmethod
    def metodo_classe(cls):
    # Pode chamar diretamente o método
        print("Olá!")

    
    @classmethod
    def metodo_50_anos(cls, nome):
        return cls(nome, 50)


Pessoa.metodo_classe()
p1 = Pessoa.metodo_50_anos("João")
print(p1.nome, p1.idade)



class Nascimento:
    @classmethod
    def register(cls, nome, sobrenome, idade):
        certidao = cls()
        certidao.nome = nome
        certidao.sobrenome = sobrenome
        certidao.idade = idade

        return certidao

p = Nascimento.register("Anderson", "Gabriel", 25)
print(p.nome, p.sobrenome, p.idade)
