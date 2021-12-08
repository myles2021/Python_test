import random

def greet():
    name = input("What's your name? ")
    print(f"Hello {name}")

greet()

def greet(name):
    return f"Hello {name}"

name = input("What is your name? ")
greet(name)

def greet(name, greeting="hello"):
    print(f"{greeting} {name}")

greet("Myles", greeting="Yo")


def add_calc(num1, num2):
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")


add_calc(random.randint(0, 101), random.randint(0, 101))
