# Mantendo estados dentro da classe

class Camera:
    # Camera.atributo
    atributo = "Marca" # Pode ser usado a qualquer momento na classe

    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando=filmando
    

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} Já está filmando")
            return
        
        print(f"{self.nome} está fimando...")
        self.filmando = True
    
    
    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar filmando")
            return

        print(f"{self.nome} está fotografando")

    
    def parar_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando")
        
        print(f"{self.nome} está parando de filma")
        self.filmando = False

c1 = Camera("Canon")
c2 = Camera("Sony")
c1.filmar()
print(c2.filmando) # False, pois não está filmando
c1.filmar() # Preserva o estado anterior e retorna a condição de já está filmando
c1.parar_filmar()
c1.fotografar()