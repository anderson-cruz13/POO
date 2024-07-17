# Exemplos de Programação Orientada a Objetos em Python

Este repositório contém exemplos de código que demonstram os conceitos e práticas da programação orientada a objetos (POO) em Python.

## Conteúdo

- [Introdução](#introdução)
- [Conceitos Básicos](#conceitos-básicos)
  - [Classe](#classe)
  - [Objeto](#objeto)
  - [Herança](#herança)
  - [Polimorfismo](#polimorfismo)
  - [Encapsulamento](#encapsulamento)
- [Exemplos de Código](#exemplos-de-código)
  - [Classe Básica](#classe-básica)
  - [Herança](#exemplo-de-herança)
  - [Polimorfismo](#exemplo-de-polimorfismo)
  - [Encapsulamento](#exemplo-de-encapsulamento)

## Introdução

A Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza "objetos" e suas interações para projetar e programar aplicativos de computador. Em Python, tudo é um objeto, o que torna essa linguagem muito poderosa e flexível para POO.

## Conceitos Básicos

### Classe

Uma classe é um modelo (blueprint) para criar objetos. Ela define um conjunto de atributos e métodos que os objetos criados a partir da classe podem ter.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
```
### Objeto
Um objeto é uma instância de uma classe. Ele representa uma entidade específica do mundo real.

```python
pessoa1 = Pessoa("Alice", 30)
print(pessoa1.saudacao())  # Saída: Olá, meu nome é Alice e eu tenho 30 anos.
```

### Herança
Herança é o mecanismo pelo qual uma classe pode herdar atributos e métodos de outra classe.

```python
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def saudacao(self):
        return f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e sou {self.cargo}."
```

### Polimorfismo
Polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme.

```python
pessoas = [Pessoa("Alice", 30), Funcionario("Bob", 25, "Engenheiro")]

for pessoa in pessoas:
    print(pessoa.saudacao())
```

### Encapsulamento
Encapsulamento é o princípio de esconder os detalhes internos de um objeto e expor apenas o que é necessário através de métodos públicos.

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # __saldo -> o double torna-o privado

    def depositar(self, quantia):
        self.__saldo += quantia

    def sacar(self, quantia):
        if quantia <= self.__saldo:
            self.__saldo -= quantia
        else:
            print("Saldo insuficiente")

    def obter_saldo(self):
        return self.__saldo
```

## Exemplos de Código
## Classe Básica
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

```
## Exemplo de Herança
```python
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def saudacao(self):
        return f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e sou {self.cargo}."

```
## Exemplo de Polimorfismo
```python
pessoas = [Pessoa("Alice", 30), Funcionario("Bob", 25, "Engenheiro")]

for pessoa in pessoas:
    print(pessoa.saudacao())

```
## Exemplo de Encapsulamento
```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, quantia):
        self.__saldo += quantia

    def sacar(self, quantia):
        if quantia <= self.__saldo:
            self.__saldo -= quantia
        else:
            print("Saldo insuficiente")

    def obter_saldo(self):
        return self.__saldo

```