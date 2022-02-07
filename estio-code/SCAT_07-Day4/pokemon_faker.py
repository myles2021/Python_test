from faker import Faker

Faker::Games::Pokemon.name

emptyList = []

running = True

while running:
    for number in range(0, 1000):
        emptyList.append(number)
    running = False

print(f"There are {len(emptyList)} items in this list:")
print(emptyList)
