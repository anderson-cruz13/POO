# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# x -> public (Usada em qualquer local)
# _x -> protected (Não deve ser usado fora da classe ou subclasses)
# __x -> private (Só deve usar na própria classe)

class Foo:
    def __init__(self) -> None:
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'
    
    def metodo_publico(self):
        ...

    def _metodo_protected(self):
        ...

    def __metodo_private(self):
        ...