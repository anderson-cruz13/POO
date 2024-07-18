# @property - um getter Pythônico
# getter - obtem um atributo
# @property é uma propriedade do objeto que comporta-se como atributo
# - como getter
# - evita quebra código cliente (código que usa seu código)
# - habilitar setter
# - executar ação afim de obter um atributo
# Código cliente é o código que usa a classe
# private protected public:
# getter -> obter valor (property)
# Atributos que começam com um ou dois underlines não
# devem ser usados fora do escopo da classe

class Caneta:
    def __init__(self, cor) -> None:
        # Caso mude a var, o código não é quebrado
        self._cor = cor # Isso não deve ser alterado
    

    def get_cor(self): # Aqui é um método, precisa usar o ()
        return self._cor


    @property
    def cor(self): # Aqui não usa () -> comporta-se como atributo
        return self._cor


    @cor.setter # Isso é um setter que vem da property (é um método)
    def cor(self, valor):
        self._cor = valor


#################################################
# Código cliente

azul = Caneta('Azul')
print(azul.get_cor()) # Método
print(azul.cor) # Propriedade que comporta-se como atributo

azul.cor = 'Rosa' # Ao mudar o valor da classe, o setter da classe é executado
print(azul.cor)