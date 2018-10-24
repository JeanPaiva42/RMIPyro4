import Pyro4
import json
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Server(object):

    cadastrados = None
    uri = None
    filial = None
    uri2 = None
    filial2 = None
    uri2 = None
    filial2= None
    enderecos = []
    ready = None
    def __init__(self):
        self.loadJson()
        self.ready = False

        pass

    def getDebitos(self, dicc):
        print("Consultado debitos de filiais ")
        if self.ready == False:
            self.enderecos = {"1": "PYRO:example.filial@127.0.0.1:8000", "2": "PYRO:example.filial2@127.0.0.1:8001",
                              "3": "PYRO:example.filial3@127.0.0.1:8002"}
            self.uri = self.enderecos['1']
            self.filial = Pyro4.Proxy(self.uri)
            self.uri2 = self.enderecos['2']
            self.filial2 = Pyro4.Proxy(self.uri)
            self.uri3 = self.enderecos['3']
            self.filial3 = Pyro4.Proxy(self.uri)
            self.ready = True
        print("Procurando debitos")
        for i in self.cadastrados:
            if i['nome'] == dicc['nome'] and i['numero'] == dicc['numero']:
                if(i['idOrigem'] == '1'):
                    return self.filial.consultaDebito(i['nome'], i['numero'])
                if (i['idOrigem'] == '2'):
                    return self.filial2.consultaDebito(i['nome'], i['numero'])
                if (i['idOrigem'] == '3'):
                    return self.filial3.consultaDebito(i['nome'], i['numero'])
        pass

    def salvaOrigem(self, dicc):
        self.cadastrados.append(dicc)
        self.saveJson()
        if self.ready == False:
            self.enderecos = {"1": "PYRO:example.filial@127.0.0.1:8000", "2": "PYRO:example.filial2@127.0.0.1:8001",
                              "3": "PYRO:example.filial3@127.0.0.1:8002"}
            self.uri = self.enderecos['1']
            self.filial = Pyro4.Proxy(self.uri)
            self.uri2 = self.enderecos['2']
            self.filial2 = Pyro4.Proxy(self.uri)
            self.uri3 = self.enderecos['3']
            self.filial3 = Pyro4.Proxy(self.uri)
            self.ready = True
        print("Novo cadastro efetuado no servidor")
        pass

    def devolveServidor(self, dicc):
        if self.ready == False:
            self.enderecos = {"1": "PYRO:example.filial@127.0.0.1:8000", "2": "PYRO:example.filial2@127.0.0.1:8001",
                              "3": "PYRO:example.filial3@127.0.0.1:8002"}
            self.uri = self.enderecos['1']
            self.filial = Pyro4.Proxy(self.uri)
            self.uri2 = self.enderecos['2']
            self.filial2 = Pyro4.Proxy(self.uri)
            self.uri3 = self.enderecos['3']
            self.filial3 = Pyro4.Proxy(self.uri)
            self.ready = True
        print("Procurando debitos")
        for i in self.cadastrados:
            if i['nome'] == dicc['nome'] and i['numero'] == dicc['numero']:
                if(i['idOrigem'] == '1'):
                    return self.filial.devolve(i['nome'], i['numero'])
                if (i['idOrigem'] == '2'):
                    return self.filial2.devolve(i['nome'], i['numero'])
                if (i['idOrigem'] == '3'):
                    return self.filial3.devolve(i['nome'], i['numero'])
        pass
    def loadJson(self):
        try:
            with open("cadastrosServer.json", "r") as read_file:
                self.cadastrados = json.load(read_file)
        except:
            self.cadastrados = []

    def saveJson(self):
        with open("cadastrosServer.json", "+w") as write_file:
            json.dump(self.cadastrados, write_file)
    def oi(self):
        print('koe')

def main():
    Pyro4.Daemon.serveSimple(
        {
            Server: "example.servidor"
        },
    host = "127.0.0.1", port = 8080, ns = False, verbose = True)
    print("Conectado")

if __name__ == "__main__":
    main()