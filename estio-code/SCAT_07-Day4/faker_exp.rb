require "faker"

Faker::Games::Pokemon.name

emptyList = []

running = True

while running
    for number in range(0, 1000):
        emptyList.append(number)
    end
    running = False
end

print "There are #{len(emptyList)} items in this list:"
print emptyList
