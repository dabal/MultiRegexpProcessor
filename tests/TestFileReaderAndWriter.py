import unittest
from FileReaderAndWriter import *
import Ekstraktor
import sys
from io import StringIO

class TestFileReaderAndWriter(unittest.TestCase):
    def test_perform1(self):
        testString=unicode("""jakas linia z 99
        jakas linia do zapisania1
        jakas linia do zapisania2
        jakas linia co ma na koncu ala""")
        resultString=unicode("""\r\n        jakas linia do zapisania1\r\n        jakas linia do zapisania2\r\n""")
        infile=StringIO()
        infile.write(testString)
        infile.seek(0)
        outfile=StringIO()
        obj=FileReaderAndWriter()
        regexp=[r'\d\d', r'ala$']
        #regexp=[]
        ekstraktor=Ekstraktor.Ekstraktor(regexp)
        integrator=Ekstraktor.Ekstraktor([r'j'])
        outfile=obj.perform(infile, outfile,ekstraktor,integrator)
        outfile.seek(0)
        content = outfile.read()
        #print '******'+content+'*********\r\n'
        self.assertEqual(content,resultString)

    def test_perform2(self):
        testString=unicode("""jakas linia z 99
        jakas linia do zapisania1
        jakas linia do zapisania2
        jakas linia co ma na koncu ala
        jakas linia do zapisania3""")
        resultString=unicode("""        jakas linia do zapisania1        jakas linia do zapisania2        jakas linia do zapisania3\r\n""")
        infile=StringIO()
        infile.write(testString)
        infile.seek(0)
        outfile=StringIO()
        obj=FileReaderAndWriter()
        regexp=[r'\d\d', r'ala$']
        #regexp=[]
        ekstraktor=Ekstraktor.Ekstraktor(regexp)
        integrator=Ekstraktor.Ekstraktor([])
        outfile=obj.perform(infile, outfile,ekstraktor,integrator)
        outfile.seek(0)
        content = outfile.read()
        #print '******'+content+'*********\r\n'
        self.assertEqual(content,resultString)

#python -m unittest tests.TestFileReaderAndWriter
