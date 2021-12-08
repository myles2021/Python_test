import time

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
