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

# print from 0 to 9 and then when x is equal to 3 break the programme, and print the else statement
for x in range(10):
    if x == 3: break
    print(x)
    time.sleep(0.5)
else:
    print("Finished counting!")

print("on to the next...")

# print the array of people including "Siamak", but break the programme when x is equal "Siamak"
people = ["Joseph", "Alma", "Siamak"]
for x in people:
    print(x)
    time.sleep(0.5)
    if x == "Siamak":
        break

print("on to the next...")

# print the array of people but not "Siamak", and break the programme when x is equal "Siamak"
people = ["Joseph", "Alma", "Siamak"]
for x in people:
    if x == "Siamak":
        break
    print(x)
    time.sleep(0.5)


print("on to the next...")

# print the array of people and continue the programme even if x is equal "Siamak"
people = ["Joseph", "Alma", "Siamak"]
for x in people:
    if x == " Siamak":
        continue
    print(x)
    time.sleep(0.5)

print("on to the next...")

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
