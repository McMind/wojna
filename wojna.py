import itertools
import random
import pandas
class talia():
    def __init__(self):
        self.wartosc = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.kolor = ['♠','♥','♦','♣']
    def tasuj(self):
        self.wk = []
        for element in itertools.product(self.wartosc,self.kolor):
            self.wk.append(element)
        random.shuffle(self.wk)
class gracze():
    def __init__(self, imie, nr):
        self.imie = imie
        self.nr = nr
    def rozdaj(self, talia, ilosc):
        self.reka = []
        for i in range(self.nr,len(talia),ilosc):
            self.reka.append(talia[i])
    def wyloz(self):
        self.wylozona = self.reka.pop(0)
        self.wylozonaSTR = ' '.join(self.wylozona)
    
        

#print(talia.shuffle(talia()))
#                          ilosc = int(input("Ilu gra graczy? (2,3,4)"))
ilosc = 4
tal = talia()
tal.tasuj()
gracz = [None] * ilosc
for i in range(ilosc):
    gracz[i] = gracze("tom",i)
    gracz[i].rozdaj(tal.wk,ilosc)

gracz[0].wyloz()
gracz[1].wyloz()
gracz[2].wyloz()
gracz[3].wyloz()
print(pandas.DataFrame([gracz[0].wylozonaSTR,gracz[1].wylozonaSTR,gracz[2].wylozonaSTR,gracz[3].wylozonaSTR],[gracz[0].imie,gracz[1].imie,gracz[2].imie,gracz[3].imie]))

