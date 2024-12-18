temp = float(input("enter temperature number: "))
scale = input("enter Scale Celsium(C) or Farehenite (F): ").upper()
if scale == "C":
    print((temp * 9 / 5) + 32)
elif scale == "F":
    print((temp - 32) * 5 / 9)
