import json

CAMINHO_ARQUIVO = 'doc_004.json'

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = People("João", 33)
p2 = People("Maria", 45)
p3 = People("Anderson", 25)
data_base = [vars(p1), vars(p2), vars(p3)]

def fazer_dumpr():
    with open(CAMINHO_ARQUIVO, "w+") as arquivo:
        json.dump(data_base, arquivo, ensure_ascii=False, indent=2)
    
if __name__ == "__main__":
    fazer_dumpr()