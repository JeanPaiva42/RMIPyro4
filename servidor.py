import sys
import Pyro4
import pessoa

#input("Enter the uri of the warehouse: ").strip()
uri = "PYRO:example.filial@localhost:61478"
filial = Pyro4.Proxy(uri)

#filial.procuraCliente("JJ",11)
filial.cadastraPessoa('Jo', 2)
filial.cadastraPessoa('Paulo', 45)
print(filial.getPessoas())
print(filial.getVeiculos())
filial.aluga("Paaa",22)
filial.aluga("Paulo",45)
print(filial.getDebitos())
filial.devolve("Paulo",45)
print(filial.getDebitos())
#filial.procuraCliente('Jo',2)
#PYRO:example.filial@localhost:62375