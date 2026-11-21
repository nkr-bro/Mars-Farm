day = 1
water = 3
watered = False
grow = 0
harvest = 0
for _ in range(2):
    change = input("Water the plant (y/n)")
    if change == "y":
        if watered:
            pass
        else:
            if water >= 1:
                water -= 1
                watered = True
    else:
        pass

    if watered:
        grow += 1
    if grow >= 2:
        harvest += 1
        grow = 0
    day += 1
    watered = False
    water = 3

print(harvest)
print(day)
print(water)
print(grow)