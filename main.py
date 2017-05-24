import sys
import FileReaderAndWriter
import Ekstraktor

fin=open('D:\\Gtesty\\7.TXT;1', 'r')
fout=open('test.txt','w')
fraw=FileReaderAndWriter.FileReaderAndWriter()
ekstraktor=[r'^\x0c',r'^=+', r'^  Nr Rachunku ', r'^   S.A. \(',r'^ *$',\
r'^  Data   Data         Nr    Kod           Kwota:  ',\
r'^         Efek.:       Kol.: Tran.:']
e=Ekstraktor.Ekstraktor(ekstraktor)
integrator=[r'^\d\d/\d\d/\d\d']
#integrator=[]
i=Ekstraktor.Ekstraktor(integrator)
fout=fraw.perform(fin,fout,e,i)
fout.close()
fin.close()
exit(0)
