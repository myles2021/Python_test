import time
import random

correct_count = 0
count = 0
num_of_questions = 5

start_time = time.time()

while count < num_of_questions:
    number_one = random.randint(0, 9)
    number_two = random.randint(0, 9)
    if number_one < number_two:
        number_one, number_two = number_two, number_one

    answer = eval(input(f"Equation {count + 1}: {number_one} + {number_two} = "))

    if number_one + number_two == answer:
        print("You're right!")
        correct_count += 1
        count += 1
    else:
        print(
            f"Wrong answer \n {number_one} + {number_two} = {number_one + number_two}")
        count += 1

end_time = time.time()

test_time = int(end_time - start_time)

print(f"Correct count is {correct_count}, out of {num_of_questions} in {test_time} seconds.")
