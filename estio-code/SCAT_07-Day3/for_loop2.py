import time

# print from 0 to 9
for x in range(10):
    print(x)
    time.sleep(0.5)

print("on to the next...")

# print from 2 to 9
for x in range(2, 10):
    print(x)
    time.sleep(0.5)

print("on to the next...")

# print from 2 to 98 in increments of 3
for x in range(2, 100, 3):
    print(x)
    time.sleep(0.5)

print("on to the next...")

# print from 2 to 9 in increments of 3
for x in range(2, 10, 3):
    print(x)
    time.sleep(0.5)

print("on to the next...")

# print from 0 to 9 and then when the loop breaks, print the else statement
for x in range(10):
    print(x)
    time.sleep(0.5)
else:
    print("Finished counting!")

print("on to the next...")

# print from 0 to 9 and then when x is equal to 3 break the programme, and don't print the else statement
for x in range(10):
    if x == 3: break
    print(x)
    time.sleep(0.5)
else:
    print("Finished counting!")
