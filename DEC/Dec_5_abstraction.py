from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark..Bark....")

# obj_ref =  Dog("puff")
# obj_ref.make_sound()


class Gearbox(ABC):
    @abstractmethod
    def setGear(self):
        pass

class Engine(Gearbox):
    @abstractmethod
    def start(self):
        super().setGear()
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):
    def start(self):
        print("starting")

    def stop(self):
        print("stopping")

    def setGear(self):
        print("setting gear")

    def drive(self):
        self.setGear()
        self.start()
        self.stop()


car_obj = Car()
car_obj.drive()


