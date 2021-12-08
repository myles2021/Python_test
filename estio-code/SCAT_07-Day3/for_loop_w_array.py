my_fruit = ["Apple", "Banana", "Cherry", "Orange", "Strawberry"]

for fruit in my_fruit:
    print(fruit)

for num in range(5):
    print(num)

for char in "Hello World!":
    print(char)

for word in "Hello world".split():
    print(word)

for word in "Hello world".split("o"):
    print(word)

diction = {"key" : "value"}

for key in {"key" : "value"}:
    print(key)

for value in {"key" : "value"}.values():
    print(value)

for key, value in diction.items():
    print(key, value)


result = []
for x in range(5):
    result.append(x)
    print(result)


print([x for x in range(5)])
