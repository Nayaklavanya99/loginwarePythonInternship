size = int(input("Enter size of square: "))
for i in range(size):
    if i == 0 or i == size - 1:
        print("* " * size)
    else:
        line = "*"
        for j in range(size - 2):
            line += "  "
        line += " *"
        print(line)
