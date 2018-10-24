import pessoa
import Pyro4
import json

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Filial(object):
    veiculos = []
    pessoas = None
    debitos = None
    id = None
    uri = None
    servidor = None
    def __init__(self):
        self.veiculos = ['fusca', 'opala', 'ogromovel']
        self.loadJson()
        self.id = '3'
        self.uri = "PYRO:example.servidor@localhost:59982"
        self.servidor = Pyro4.Proxy(self.uri)
    def cadastraPessoa(self, nome, numero):
        try:
            # self.pessoas.append(pessoa.Pessoa(nome,numero))
            d = {"nome": nome, "numero": numero}
            self.pessoas.append(d)
            d['idOrigem'] = self.id
            self.servidor.salvaOrigem(d)
            print("dado cadastrado")
        except:
            print("Verificar o servidor")

    def aluga(self, nome, numero):
        for i in self.pessoas:
            if i['nome'] == nome and i['numero'] == numero and (self.consultaDebito(i['nome'],i['numero']) == False):
                d = {}
                d['cliente'] = i
                d['debito'] = True
                self.debitos.append(d)
                pass
        print("Cliente não encontrado na base")

    def procuraCliente(self, nome, numero):
        for i in self.pessoas:
            if i['nome'] == nome and i['numero'] == numero:
                return i
        return None


    def devolve(self,nome,numero):
        cli = self.procuraCliente(nome, numero)
        if cli is not None:
            for i in self.debitos:
                if i['cliente'] == cli:
                    self.debitos.remove(i)
                    pass
        else:
            print("Devolvendo em outra filial")
            return self.servidor.getDebitos({"nome": nome, "numero": numero})


    def consultaDebito(self, nome, numero):
        cli = self.procuraCliente(nome,numero)
        if cli is not None:
            for i in self.debitos:
                if i['cliente'] == cli:
                    return True
            return False
        else:
            print("Procurando em outra filial.. .")
            return self.servidor.getDebitos({"nome":nome,"numero":numero})


    def loadJson(self):
        try:
            with open("debitos3.json", "r") as read_file:
                self.debitos = json.load(read_file)
        except:
            self.debitos = []
        try:
            with open("pessoas3.json", "r") as read_file:
                self.pessoas = json.load(read_file)
        except:
            self.pessoas = []

    def saveJson(self):
        with open("debitos3.json", "w") as write_file:
            json.dump(self.debitos, write_file)
        with open("pessoas3.json", "w") as write_file:
            json.dump(self.pessoas, write_file)


    def getVeiculos(self):
        return self.veiculos
    def getPessoas(self):
        return self.pessoas
    def getDebitos(self):
        return self.debitos
    def getId(self):
        return self.id
def main():
    Pyro4.Daemon.serveSimple(
            {
                Filial: "example.filial3"
            },
        host="127.0.0.1", port=8002, ns=False, verbose=True)

if __name__=="__main__":
    main()
