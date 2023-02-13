class BaseAnimal:

    def __init__(self, type, name, age, food):
        self.__type = type
        self.name = name
        self.__age = age
        self.__food = food



    @property
    def Type(self):
        return self.__type

    def DoSound(self):
        print(self.name, "сказал:", self._sound)

    def play(self):
        print(self.name, "играет")

    def IsFeeded(self, amount):
        return  amount >= self.__food

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        if (value is int):
            if (value >= 0):
                self.__age = value
            else:
                print("я не доволен, переделывай")

    def eat(self, foodType):
        if (foodType in self.foodTypes):
            print(self.name, ": Я покушал", foodType)
        else:
            print(self.name, ": Я не буду", foodType)





