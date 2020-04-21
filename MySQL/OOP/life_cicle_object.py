class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am cnstructed')

    def party(self):
        self.x = self.x + 1
        print('So far {}.'.format(self.x))

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('An contains', an)    
