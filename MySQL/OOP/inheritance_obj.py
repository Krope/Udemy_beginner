import PartyAnimal

class CriketFan(PartyAnimal):
    points = 0
    def six(self):
        self.ponts = self.points + 6
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricetFan("Jim")
j.party()
j.six()
print(dir(j))
