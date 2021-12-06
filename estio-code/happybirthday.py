import humanize
import time

age = int(input("Please enter your age: "))
name = input("Please enter your name: ")
counter = 1
while age >= counter:
    print(f"Happy {humanize.ordinal(counter)} Birthday, {name.capitalize()}!")
    counter += 1
    time.sleep(0.5)

print(f"Hi {name.capitalize()}, you don't look {age} 🤨")

# edit for git
