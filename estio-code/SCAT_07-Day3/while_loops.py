import time

# increment i by one and print i until it reaches 6, then the loop finishes
i = 1
while i < 6:
    print(i)
    i += 1
    time.sleep(0.5)

print("on to the next...")

# increment i by one and print i until it reaches 6, then the loop finishes. But if i is equal to 3 then break the programme
i = 1
while i < 6:
    print(i)
    time.sleep(0.5)
    if i == 3:
        break
    i += 1

print("on to the next...")

# increment i by one and print i until it reaches 6, then the loop finishes. But if i is equal to 3, the programme can continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    time.sleep(0.5)

print("on to the next...")

# increment i by one and print i until it reaches 6, then the loop finishes and prints the else statement
i = 1
while i < 6:
    print(i)
    time.sleep(0.5)
    i += 1
else:
    print("i is no longer less than 6")
