class Dog:
    energy = "high"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()

print(bilbo_waggins.energy)
bilbo_waggins.speak()

chewbarka = Dog()
chewbarka.energy = "low"
print(chewbarka.energy)
chewbarka.speak()

class Cat:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy

cat1 = Cat("Meowth", "Pokemon", "Chaotic")
print(cat1.name)
print(cat1.breed)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Kane = Student("Kane", "27")
Alia = Student("Alia", "26")
Myles = Student("Myles", "26")
Alex = Student("Alex", "18")
Sam = Student("Sam", "18")

print(getattr(Kane, "age"))
print(getattr(Myles, "age"))
print(getattr(Sam, "name"))


class Animal:
    babies = 0

    def reproduce(self):
        self.babies += 1

class Dog(Animal):
    def reproduce(self):
        self.babies += 6


john = Dog()
john.reproduce()
print(john.babies)


class Athlete:
    def __init__(self, name):
        self.name = name

# class Footballer:
