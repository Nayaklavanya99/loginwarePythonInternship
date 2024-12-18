rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    spaces = rows - i
    for _ in range(spaces):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
