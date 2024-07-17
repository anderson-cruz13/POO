# Hard coded - Algo escrito diretamente no código
# class usa PascalCase
# O escopo é "privado"

class Carro:
    def __init__(self, nome):
        self.nome = nome

    
    def acelerar(self): # Métodos em instâncias  
        print(f"{self.nome} acelerando... ")


fusca = Carro('Fusca')
fusca.acelerar()
