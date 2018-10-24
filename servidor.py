import sys
import Pyro4
import pessoa

uri = "PYRONAME:example.filial"
#input("Enter the uri of the warehouse: ").strip()
filial = Pyro4.Proxy(uri)
print(filial.veiculos)

#filial.cadastraPessoa('Jo', 2)
#filial.procuraCliente('Jo',2)
#PYRO:example.filial@localhost:62375