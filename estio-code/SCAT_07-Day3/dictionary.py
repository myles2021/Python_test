cool_cows = "Winnie the Moo", "Moolan", "Milkshake", "Mooana"

print(cool_cows[0])
print("Hello World"[3:8])

farm = "Pepperidge Farm", ["Winnie", "Moo"], 1850

print(farm)

farm_name, cool_cows, farm_size = farm

print(farm_name)
print(cool_cows)
print(farm_size)

## DICTIONARIES

noises = {"cow": "moo", "sheep": "baa"}
print(noises["cow"])
noises["chicken"] = "cluck"
print(noises["chicken"])
noises["sheep"] = "meh"
print(noises)
print(noises.keys())
print(noises.values())
print(noises.items())

print("\n")

if "moo" in noises.values():
    print(True)
else:
    print(False)

print("\n")

my_words = {"hello": "hola", "thank-you": "gracias"}

print(my_words.get("hello"))
my_words.pop("hello")
print(my_words)
my_words.update({"beer": "cerveza", "hello": "ey"})
print(my_words)


### LISTS

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]

print(cool_cows[2])
print(cool_cows[-1])
print(cool_cows[1:3])
print(cool_cows[1:])
cool_cows[0] = "Aladdin but a cow"
print(cool_cows[0])
del cool_cows[0]
print(cool_cows)

if "Moolan" in cool_cows:
    print(True)

cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]
cool_animals = [cool_cows, cool_sheep, cool_pigs]
print(cool_animals)
print(cool_animals[2][2])
print(cool_animals[0][1])

farm = ["Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850]
print(farm[0])
print(farm[1])
print(farm[2])
