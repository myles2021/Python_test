import random

def arithmetic(num1, num2):
    print(f"{num1} x {num2} = {num1 * num2}")
    print(f"{num1} % {num2} = {num1 / num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} + {num2} = {num1 + num2}")


arithmetic(random.randint(0, 10), random.randint(0, 10))


def arithmetic_two(method):
    num_one = random.randint(0, 101)
    num_two = random.randint(0, 101)
    if method == "multiply":
        guess = eval(input(f"Equation 1 \n {num_one} x {num_two} = "))
        if guess == (num_one * num_two):
            print("Correct answer!")
        else:
            print("Wrong answer...")
    elif method == "divide":
        guess = eval(input(f"Equation 1 \n {num_one} % {num_two} = "))
        if guess == (num_one / num_two):
            print("Correct answer!")
        else:
            print("Wrong answer...")
    elif method == "subtract":
        guess = eval(input(f"Equation 1 \n {num_one} - {num_two} = "))
        if guess == (num_one - num_two):
            print("Correct answer!")
        else:
            print("Wrong answer...")
    else:
        guess = eval(input(f"Equation 1 \n {num_one} + {num_two} = "))
        if guess == (num_one + num_two):
            print("Correct answer!")
        else:
            print("Wrong answer...")


arithmetic_two("add")
