import threading, time, random

class Piloto(threading.Thread):
    def __init__(self, namePiloto):
        threading.Thread.__init__(self)
        self.namePiloto=namePiloto
        self.tempoGP=0
        
    def run(self):
        tempoVolta=0
        for i in range(1,66):

            print('O piloto ', self.namePiloto, 'deu a volta ', i)
            tempoVolta=random.random()
            self.tempoGP+=tempoVolta
            time.sleep(tempoVolta)
        print('Bandeirada: ', self.namePiloto)

p1 = Piloto('Felipe Massa')
p2 = Piloto('Lewis Hamilton')

p1.start()
p2.start()

p1.join() 
p2.join()


if p1.tempoGP > p2.tempoGP:
    print(p2.namePiloto, 'CRUZA A LINHA DE CHEGADA e é o vencedor! ')
elif p1.tempoGP < p2.tempoGP:
    print(p1.namePiloto, 'CRUZA A LINHA DE CHEGADA e é o vencedor! ')
else: 
    print('INCRÍVEL! Cruzaram a linha no mesmo instante.')
    