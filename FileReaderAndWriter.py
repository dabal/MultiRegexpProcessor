import sys
import ListaWykluczenError
import Ekstraktor

class FileReaderAndWriter:
    def perform(self, fin,fout, ekstraktor,integrator):
        linia=''#unicode('')
        line=''#unicode('')
        for line in fin.readlines():
            try:
                ekstraktor.czyPoprawna(line)
                line=line.rstrip('\r\n')
                #print 'RRR: '+line+'\r\n'
                try:#dodac chomp tylko nie wiem jak to w python
                    integrator.czyPoprawna(line)#nie wiem czy tu to dobrze wyglada z if byloby lepiej - trzzeba by sie bylo moze odpoytac michal
                    linia=linia+line
                    line=''#unicode('')#niepotrzebrne
                except ListaWykluczenError.ListaWykluczenError:
                    fout.write(linia+'\r\n')#zamienic w przyszlosici na os EOL
                    #print 'D: '+linia
                    linia=line
                    #przypuszczlnie gubie ostatnia linie do weryfikacji na etapie testow
                    #lub przypuszczalnie dubluje ostantia linie
            except ListaWykluczenError.ListaWykluczenError:
                line=''#unicode('')
        fout.write(linia+'\r\n')
        return fout
