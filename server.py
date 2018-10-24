import Pyro4
import json
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Server(object):

    cadastrados = None
    uri = None
    filial = None
    def __init__(self):
        self.loadJson()
        self.uri = "PYRO:example.servidor@localhost:61443"
        self.filial = Pyro4.Proxy(self.uri)
        pass

    def getDebitos(self, dicc):
        for i in self.cadastrados:
            if i['nome'] == dicc['nome'] and i['numero'] == dicc['numero']:
                fili = 'filial'+i['idOrigem']
                
        pass

    def salvaOrigem(self, dicc):
        self.cadastrados.append(dicc)
        self.saveJson()
        pass
    def loadJson(self):
        try:
            with open("cadastrosServer.json", "r") as read_file:
                self.cadastrados = json.load(read_file)
        except:
            self.cadastrados = []

    def saveJson(self):
        with open("cadastrosServerjson", "w") as write_file:
            json.dump(self.cadastrados, write_file)

def main():
    Pyro4.Daemon.serveSimple(
        {
            Server: "example.servidor"
        },
        ns=False)

if __name__ == "__main__":
    main()