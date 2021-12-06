import random
number = random.randint(0, 100)

print("Guess a magic number between 1 and 100...")

guess = -1

while guess != number:
    guess = eval(input("Choose your number!\n"))
    if guess == number:
        print("Wow, genius 😳")
    elif guess > number:
        print("Waaaaaay too high! 🥺")
    else:
        print("Eeeeeeek, guess higher!! 😵‍💫")
