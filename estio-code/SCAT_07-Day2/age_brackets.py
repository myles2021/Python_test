age = input("What is your age? \n")

if int(age) < 20:
    print("You're below 20!")
elif int(age) >= 20 and int(age) <= 50:
    print("You're between 20 and 50!")
elif int(age) > 50 and int(age) <= 85:
    print("You're between 51 and 85!")
else:
    print("You're above 85!")
