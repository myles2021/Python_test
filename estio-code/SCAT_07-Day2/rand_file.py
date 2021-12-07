import random

number = random.randint(10, 100)
bank = 0
guess = (input("Take a guess at the lottery! \n"))

print(number)
decimal = number / 10
digit_one = number // 10
print(decimal)
print(digit_one)

guess_digit_one = number / 10
print(guess_digit_one)

guess_digit_two = (decimal - digit_one) * 10
print(guess_digit_two)

digit_two = decimal % 2
print(digit_two)

if guess == number:
    bank += 10000
    print("You've won £10,000")
    print(f"Total: £{bank}")
elif guess_digit_one == digit_one or digit_two and guess_digit_two == digit_one or digit_two:
    bank += 5000
    print("You've won £5,000")
    print(f"Total: £{bank}")
elif guess_digit_one == digit_one or digit_two:
    bank += 1000
    print("You've won £1,000")
    print(f"Total: £{bank}")
elif guess_digit_two == digit_one or digit_two:
    bank += 1000
    print("You've won £1,000")
    print(f"Total: £{bank}")
else:
    print("No money for you...")



# lottery = random.randint(0, 99)
# guess = eval(input("Enter your lottery pick two digits: "))
# lotteryDigit1 = lottery // 10
# lotteryDigit2 = lottery % 10
# guessDigit1 = guess // 10
# guessDigit2 = guess % 10

# print("The lottery number is", lottery)

# if guess == lottery:
#     print("Exact match: you win £10,000")
# elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
#     print("Match all digits: you win £3,000")
# if (guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2):
#     print("Match one digit: you win £1,000")
# else:
#     print("Sorry, no match")
