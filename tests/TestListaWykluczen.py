import unittest
import ListaWykluczen
import ListaWykluczenError
import re

class TestListaWykluczen(unittest.TestCase):
	def testDodajISprawdzCzyJest(self):
		tmp=ListaWykluczen.ListaWykluczen()
		tmp.add(re.compile(r'^\d\d'))
		self.assertEquals(tmp.getPattern(re.compile(r'^\d\d')),r'^\d\d')

	def testDodajISprawdzCzyRzucaWyjatek(self):
		tmp=ListaWykluczen.ListaWykluczen()
		tmp.add(re.compile(r'\d\d'))
		with self.assertRaises(ListaWykluczenError.ListaWykluczenError):
			tmp.getPattern(re.compile(r'^\d\d'))

	def testCheckIsItOnTheList(self):
		tmp=ListaWykluczen.ListaWykluczen()
		tmp.add(re.compile(r'^\d\d'))
		self.assertTrue(tmp.checkIsItOnTheList('a00'))
		with self.assertRaises(ListaWykluczenError.ListaWykluczenError):
			tmp.checkIsItOnTheList('00')