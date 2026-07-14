# inheritance=it allows the class and methods from another class to be used in a new class

class Animal:
    def __init__(self,name,species,age,legs,hands,is_wild):
        self.name = name
        self.species = species
        self.age = age
        self.legs = legs
        self.hands = hands
        self.is_wild = is_wild

    def make_sound(self):
        print("the animal will make sound like roar")


class Dog(Animal):
    def __init__(self,name,species,age,legs,hands,is_wild,breed):
        super().__init__(name,species,age,legs,hands,is_wild)
        self.breed=breed

    def activity(self):
        print("the dog will bark and play fetch")

dog1=Dog("Buddy","Canine",3,4,0,False,"Golden Retriever")
print(f"Name: {dog1.name}, Species: {dog1.species}, Age: {dog1.age}, Legs: {dog1.legs}, Hands: {dog1.hands}, Is Wild: {dog1.is_wild}, Breed: {dog1.breed}")
dog1.make_sound()
dog1.activity()

#  multiple inheriantance
# when a class inherits from more than one base class

class Vehicle:
    def __init__(self,company,model):
        self.company=company
        self.model=model

    def start(self):
        print("the vehicle will start")

class Car:
    def __init__(self,car_type):
        self.car_type=car_type

    def ownership(self):
        print("the car is owned by a person")

# derived class inheriting from both Vehicle and Car
class ElectricCar(Vehicle,Car):
    def __init__(self,company,model,car_type,battery_capacity):
        Vehicle.__init__(self,company,model)
        Car.__init__(self,car_type)
        self.battery_capacity=battery_capacity

    def charge(self):
        print("the electric car is charging")

electric_car1=ElectricCar("Tesla","Model S","Sedan",100)
electric_car1.start()
electric_car1.ownership()
electric_car1.charge()
print(f"Company: {electric_car1.company}, Model: {electric_car1.model}, Car Type: {electric_car1.car_type}, Battery Capacity: {electric_car1.battery_capacity} kWh")