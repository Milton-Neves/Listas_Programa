class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, objeto):
        self.bucho.append(objeto)

    def verBucho(self):
        print("Estomago: ")
        for i in self.bucho:
            print(i)
        print("...")

    def digerir(self):
        print("Digerindo...")
        self.verBucho()
        self.bucho = []


macaco1 = Macaco('hum')
macaco2 = Macaco('dois')

print('\n Alimentando Hum')
print(20*'-')
macaco1.comer('Banana')
macaco1.comer('Macaxeira')
macaco1.comer('Jaca')

print('\n Alimentando Dois')
print(20*'-')
macaco2.comer('Melão')
macaco2.comer('Uva')
macaco2.comer('Melancia')

print('\n Tentando canibalismo')
print(30*'-')
macaco1.comer(macaco2)
macaco2.comer(macaco1)
