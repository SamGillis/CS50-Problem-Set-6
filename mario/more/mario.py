from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break
for i in range(height):
    for y in range(height):
        if (y + 1 >= height - i):
            print("#", end="")
        else:
            print(" ", end="")
    print("  ", end="")
    for y in range(i + 1):
        print("#", end="")
    print("\n", end="")