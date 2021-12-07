import random

number = random.randint(0, 101)
print("*****************")
print("Magic number game")
print("*****************")


guess = -1
while guess != number:
    if guess > number:
        print("Your guess is too high...")
        guess = int(input("Enter your guess between 0 and 100... \n"))
    elif guess < number:
        print("Your guess is too low...")
        guess = int(input("Enter your guess between 0 and 100... \n"))
    else:
        print("🚨🚨🚨 invalid input 🚨🚨🚨")
        guess = int(input("Enter your guess between 0 and 100... \n"))

print(f"Congrats! You're right, the magic number was {number}")
