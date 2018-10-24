
class Pessoa(object):
    nome = ""
    numero = None
    def __init__(self, name, num):
        self.nome = name
        self.numero = num

    def getNome(self):
        return self.nome
    def getNumero(self):
        return self.numero

