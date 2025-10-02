#klase
class Car:
    def __init__ (self, brand, year):
        self.brand = brand
        self.year = year
    def drive(self):
        print("Mašīna {brand} brauc!")
#objekts
car1 = Car("Toyota", 2015)
car2 = Car ( "Mercedes" , 2010)
car3 = Car ( "BMW" , 2012)

print("car 1:", car1.brand, car1.year)
print("car 2:", car2.brand, car2.year)
print("car 3:", car3.brand, car3.year)

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        print(f"Sveiks, {self.name}, tev ir {self.age} gadi!")

p1 = Person ("Lietotājs", 17 )

class Animal:
    def make_sound(self):
        print(f"Dzīvnieks izdod skaņu")

class Dog (Animal):
    def make_sound(self):
        print("Animal:'dzīvnieka skaņa'")
dog1 = Dog()
dog1.make_sound()
