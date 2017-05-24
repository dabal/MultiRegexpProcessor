import unittest
from Ekstraktor import *
import ListaWykluczenError

class TestEkstrator(unittest.TestCase):
	def testcalaLinia(self):
		e=Ekstraktor(('jakis tekst', 'ala'))
		with self.assertRaises(ListaWykluczenError.ListaWykluczenError):
			e.czyPoprawna('jakis tekst')

	def testczesciowaLinia(self):
		e=Ekstraktor(('jakis tekst',))
		self.assertTrue(e.czyPoprawna('jakis'))

	def testwielkoscLiterLinia(self):
		e=Ekstraktor(('jakis tekst',))
		self.assertTrue(e.czyPoprawna('jakis'))

	def testregexpLiniaNiepoprawna(self):
		e=Ekstraktor((r'\d\d',))
		with self.assertRaises(ListaWykluczenError.ListaWykluczenError):
			e.czyPoprawna(e.czyPoprawna('00'))

	def testregexpLiniaPoprawna(self):
		str=r'^\d\d'
		e=Ekstraktor((str,))
		self.assertTrue(e.czyPoprawna('a00'))





#python -m unittest tests.TestEkstraktor
