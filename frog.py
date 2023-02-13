from BaseAnimal import *

class Frog(BaseAnimal):

    def __init__(self, name, age, food):
        super().__init__("Frog", name, age, food)
        self.foodTypes = "мухи"
        self.biom = "тропики"
        self.square = 10
        self.nutrition = "хищник"
        self._sound = "qwe"

    def DoSound(self):
        print(self.name, "квакнула", self._sound)





