import pessoa
import Pyro4
import json

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Filial(object):
    veiculos = []
    pessoas = None
    debitos = None
    def __init__(self):
        self.veiculos = ['fusca', 'opala', 'ogromovel']
        self.pessoas = []
        self.debitos = []
    def cadastraPessoa(self, nome, numero):
            self.pessoas.append(pessoa.Pessoa(nome,numero))

    def aluga(self, nome, numero):
        for i in self.pessoas:
            if i.getNome() == nome and i.getNumero() == numero:
                d = {}
                d['cliente'] = i
                d['debito'] = True
                self.debitos.append(d)
                pass
        print("Cliente não encontrado na base")

    def procuraCliente(self, nome, numero):
        for i in self.pessoas:
            if i.getNome() == nome and i.getNumero() == numero:
                return i
        return None

    def devolve(self,nome,numero):
        cli = self.procuraCliente(nome,numero)
        if cli is not None:
            for i in self.debitos:
                if i['cliente'] == cli:
                    self.debitos.remove(i)
                    pass
        print("Cliente não encontrado na base")


    def consultaDebito(self, nome, numero):
        cli = self.procuraCliente(nome,numero)
        if cli is not None:
            for i in self.debitos:
                if i['cliente'] == cli:
                    return True
            return False
        return False

    def loadJson(self):
        with open("debitos.json", "r") as read_file:
            self.debitos = json.load(read_file)
        with open("debitos.json", "r") as read_file:
            self.pessoas = json.load(read_file)

    def saveJson(self):
        with open("debitos.json", "w") as write_file:
            write_file.write(json.encode(self.debitos))
        with open("pessoas.json", "w") as write_file:
            write_file.write(json.encode(self.pessoas))

def main():
    Pyro4.Daemon.serveSimple(
            {
                Filial: "example.filial"
            },
            ns = True)

if __name__=="__main__":
    main()
