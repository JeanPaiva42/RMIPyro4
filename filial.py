import pessoa
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


