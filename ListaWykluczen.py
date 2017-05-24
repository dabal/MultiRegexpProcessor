import re
import ListaWykluczenError

class ListaWykluczen:
	def __init__(self):
		self.__tablica=[]
	def add(self, compiled):
		self.__tablica.append(compiled)
	
	def getPattern(self, compiled):
		for i in self.__tablica:
			if(i.pattern==compiled.pattern) :
				return i.pattern
		raise ListaWykluczenError.ListaWykluczenError('brak wzoru')
	
	def checkIsItOnTheList(self, str):
		for i in self.__tablica:
			if i.search(str) is not None:
				raise ListaWykluczenError.ListaWykluczenError('jest na liscie')
		return True