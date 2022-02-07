import time

colour_list = ["Blue", "Red", "Orange", "Green", "Purple", "White", "Black"]

for x in colour_list:
    q = "e"
    if q in x:
        print(f"'{q}' is included in {x}")
        time.sleep(0.4)
    else:
        print(f"There is no '{q}' in {x}")
