

while True:
    height = int(input("Height: "))
    if height > 0 and height < 9:
        break
for i in range(height):
    for y in range (height):
        if (y + 1 >= height - i):
            print("#", end="")
        else:
            print(" ", end="")
    print("\n", end="")