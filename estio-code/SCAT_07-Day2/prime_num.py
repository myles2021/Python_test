num_primes = 50
num_primes_per_line = 10
count = 0
number = 2

print("the first 50 numbers are")

while count < num_primes:
    is_prime = True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        count += 1
        print(format(number, "5d"), end = "")
        if count % num_primes_per_line == 0:
            print()
    number += 1
