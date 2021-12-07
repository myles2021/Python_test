import random

i = random.randint(0, 100)

if i % 2 == 0:
    boolean = True
else:
    boolean = False

if boolean == True:
    print("The truth has been spoken")
else:
    print("Liar Liar!")
