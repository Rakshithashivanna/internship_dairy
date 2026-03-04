from abc import ABC,abstractclassmethod
class Animal(ABC):
    @abstractclassmethod
    def sound(self):
        pass
    def sleep(self):
        print("Animal sleep ")

class Dog(Animal):
    def sound(self):
        print("Bark")
    
class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")

cow=Cow()
cat=Cat()
dog=Dog()

dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()