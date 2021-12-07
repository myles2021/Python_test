import random

number_1 = random.randint(0, 10)
number_2 = random.randint(0, 10)

if number_1 > number_2:
    number_1, number_2 = number_2, number_1

guess = eval(input(f"Subtraction equation: \n {number_2} - {number_1} = "))

answer = number_2 - number_1

while answer != guess:
    print("Incorrect answer, try again...")
    guess = eval(input(f"Subtraction equation: \n {number_2} - {number_1} = "))

print(f"{answer} is the correct answer, well done!")
