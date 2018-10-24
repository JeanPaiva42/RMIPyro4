import pessoa
import Pyro4
import json
import threading


def startServer():
    Pyro4.Daemon.serveSimple(
        {
            Filial: "example.filial"
        },
        host="127.0.0.1", port=8000, ns=False, verbose=True)


@Pyro4.expose
# @Pyro4.behavior(instance_mode="single")
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
        self.id = '1'
        self.uri = "PYRO:example.servidor@127.0.0.1:8080"
        self.servidor = Pyro4.Proxy(self.uri)
        print('jk')

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
            if (i['nome'] == nome and i['numero'] == numero) and (self.consultaDebito(i['nome'], i['numero']) == False):
                d = {}
                d['cliente'] = i
                d['debito'] = True
                cli = self.procuraCliente(i['nome'],i['numero'])
                if cli is not None:
                    self.debitos.append(d)
                    self.saveJson()
                    self.loadJson()
                else:
                    self.servidor.alugaServer(d)
                pass

        print("Cliente não encontrado na base")

    def procuraCliente(self, nome, numero):
        for i in self.pessoas:
            if i['nome'] == nome and i['numero'] == numero:
                return i
        return None

    def devolve(self, nome, numero):
        cli = self.procuraCliente(nome, numero)
        if cli is not None:
            for i in self.debitos:
                if i['cliente'] == cli:
                    self.debitos.remove(i)
                    pass
        else:
            print("Devolvendo em outra filial")
            result = self.servidor.getDebitos({"nome": nome, "numero": numero})
            print(result)
            return result

    def consultaDebito(self, nome, numero):
        cli = self.procuraCliente(nome, numero)
        if cli is not None:
            for i in self.debitos:
                if i['cliente'] == cli:
                    return True
            return False
        else:
            print("Procurando em outra filial...")
            return self.servidor.getDebitos({"nome": nome, "numero": numero})

    def loadJson(self):
        try:
            with open("debitos.json", "r") as read_file:
                self.debitos = json.load(read_file)
        except:
            self.debitos = []
        try:
            with open("pessoas.json", "r") as read_file:
                self.pessoas = json.load(read_file)
        except:
            self.pessoas = []

    def saveJson(self):
        with open("debitos.json", "w") as write_file:
            json.dump(self.debitos, write_file)
        with open("pessoas.json", "w") as write_file:
            json.dump(self.pessoas, write_file)

    def getVeiculos(self):
        return self.veiculos

    def getPessoas(self):
        return self.pessoas

    def getDebitos(self):
        return self.debitos

    def getId(self):
        return self.id

    def servidorOi(self):
        self.servidor.oi()


def main():

    t = threading.Thread(target=startServer)
    t.start()
    '''filial = Filial()
    filial.cadastraPessoa("A", 22)
    filial.cadastraPessoa("b", 22)
    filial.cadastraPessoa("c", 22)
    filial.aluga("b", 22)
    filial.aluga("c", 22)
    print(filial.pessoas)
    print(filial.debitos)
    filial.devolve("b", 22)
    filial.devolve("aa", 22)
    print(filial.debitos)
    filial.saveJson()
'''

if __name__ == "__main__":
    main()