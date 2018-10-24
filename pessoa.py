import random


class Pessoa(object):
    nome = ""
    numero = None

    def __init__(self, name):
        self.nome = name
        self.numero = 3

    def getNome(self):
        return self.nome

    def getNumero(self):
        return self.numero
