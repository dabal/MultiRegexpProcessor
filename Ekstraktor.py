import re
import ListaWykluczen

class Ekstraktor:
	def __init__(self, listaRegexp):
		self.__listaWykluczen=ListaWykluczen.ListaWykluczen()
		for i in listaRegexp:
			self.__listaWykluczen.add(re.compile(i))
	
	def czyPoprawna(self, str):
		self.__listaWykluczen.checkIsItOnTheList(str)
		return True
