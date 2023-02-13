from BaseAnimal import *
from frog import *
from capybara import *
from chinchilla import *

class Cage:

    def __init__(self, title, biom, square):

        self.title = title
        self.biom = biom
        self.square = square

        self.animals = []

    def addAnimal(self, newAnimal: BaseAnimal):
        self.animals.append(newAnimal)



    def RemoveAnimal(self, name):
        self.animals.remove(name)

    def FeedAnimals(self):
        for i in self.animals:
            print(i, "теперь может кушать")


    def animals(self):
        print(self.animals)


    













