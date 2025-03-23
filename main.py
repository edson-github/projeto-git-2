# exemplo de herança POO

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def comer(self):
        print(f"{self.nome} está comendo")

    def dormir(self):
        print(f"{self.nome} está dormindo")


class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo")


class Gato(Animal):
    def miar(self):
        print(f"{self.nome} está miando")
