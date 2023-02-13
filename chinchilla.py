from BaseAnimal import *

class Chinchilla(BaseAnimal):

    def __init__(self, name, age, food):
        super().__init__("Chinchilla", name, age, food)
        self.foodTypes = "зерна"
        self.biom = "пустыня"
        self.square = 10
        self.nutrition = "травоядное"
        self._sound = "frfrfr"

    def DoSound(self):
        print(self.name, "нафырчала:", self._sound)

