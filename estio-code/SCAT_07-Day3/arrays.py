import time

# my array
my_fruit = ["banana", "cherry", "strawberry", "orange"]
print("my fruit")
print(my_fruit)
print("\n")
time.sleep(0.5)

# appending Grapefruit into array
my_fruit.append("Grapefruit")
print("appending Grapefruit into array")
print(my_fruit)
print("\n")
time.sleep(0.5)

# removing banana from array
my_fruit.remove("banana")
print("removing banana from array")
print(my_fruit)
print("\n")
time.sleep(0.5)

# removing element 0 from array
my_fruit.pop(0)
print("removing element 0 from array")
print(my_fruit)
print("\n")
time.sleep(0.5)

# inserting Pineapple into element 0 in the array
my_fruit.insert(0, "Pineapple")
print("inserting Pineapple into element 0 in the array")
print(my_fruit)
print("\n")
time.sleep(0.5)

# insert Grapefruit into the array but each letter is it's own element
my_fruit.extend("Grapefruit")
print("insert Grapefruit into the array but each letter is it's own element")
print(my_fruit)
print("\n")
time.sleep(0.5)

# print the index of grapefruit
print("print the index of grapefruit")
print(my_fruit.index("Grapefruit"))
print(my_fruit)
print("\n")
time.sleep(0.5)

# print the number of Grapefruit in the array
print("print the number of Grapefruit in the array")
print(my_fruit.count("Grapefruit"))
print(my_fruit)
print("\n")
time.sleep(0.5)

# reverse the order of my fruit in the array
print("reverse the order of my fruit in the array")
my_fruit.reverse()
print(my_fruit)
print("\n")
time.sleep(0.5)

# turn the array into a string and join all elements of the array together with a comma and space
print("turn the array into a string and join all elements of the array together with a comma and space")
print(", ".join(my_fruit))
