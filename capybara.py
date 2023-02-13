from BaseAnimal import *

class Capybara(BaseAnimal):

    def __init__(self, name, age, food):
        super().__init__("Capybara", name, age, food)
        self.foodTypes = "плоды"
        self.biom = "тропики"
        self.square = 10
        self.nutrition = "травоядное"
        self._sound = "yiy"

    def DoSound(self):
        print(self.name, "издала прелестный звук:", self._sound)


