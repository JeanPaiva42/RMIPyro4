import sys
import Pyro4
import pessoa

#input("Enter the uri of the warehouse: ").strip()
uri = "PYRO:example.filial@127.0.0.1:8000"
filial = Pyro4.Proxy(uri)
uri1 = "PYRO:example.filial2@127.0.0.1:8001"
filial1 = Pyro4.Proxy(uri1)
#filial.procuraCliente("JJ",11)
filial.cadastraPessoa("Paulo", 45)
filial.aluga("Paulo", 45)
filial1.aluga("Paulo", 45)
print(filial.getDebitos())
print(filial.getPessoas())
print(filial1.getDebitos())
#filial.procuraCliente('Jo',2)
#PYRO:example.filial@localhost:62375