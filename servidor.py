import sys
import Pyro4
import pessoa

#input("Enter the uri of the warehouse: ").strip()
uri = "PYRO:example.filial@127.0.0.1:8000"
filial = Pyro4.Proxy(uri)

#filial.procuraCliente("JJ",11)

'''print(filial.getPessoas())'''
filial.aluga("Paulo",45)

#filial.procuraCliente('Jo',2)
#PYRO:example.filial@localhost:62375