import os
import re
import FileReaderAndWriter
import Ekstraktor

fraw=FileReaderAndWriter.FileReaderAndWriter()
ekstraktor=[r'^\x0c',r'^=+', r'^  Nr Rachunku ', r'^   \(',r'^ *$',\
r'^  Data   Data         Nr    Kod           Kwota:  ',\
r'^         Efek.:       Kol.: Tran.:']
e=Ekstraktor.Ekstraktor(ekstraktor)
integrator=[r'^\d\d/\d\d/\d\d']
#integrator=[]
i=Ekstraktor.Ekstraktor(integrator)
for z in [x for x in os.listdir('D:\\Gtesty\\') if re.search('\d{12}.TXT',x)]:
    fin=open('D:\\Gtesty\\'+z, 'r')
    fout=open('D:\\Gtesty\\done\\'+z+'_done.txt','w')
    fout=fraw.perform(fin,fout,e,i)
    fout.close()
    fin.close()
exit(0)
