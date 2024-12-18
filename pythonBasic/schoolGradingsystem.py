score  = float(input("enter student Score:  "))
extra_circulum = input("participated in extra circular activities? (Yes/No):  ")
extra_circulum = extra_circulum.lower()
if (score > 90):
    if(extra_circulum == "yes"):
        print("Grade: A+")
    else:
        print("Grade: A")        
elif(score > 60 and score<=90):
    print("Grade: B")
elif(score <= 60):
    print("Grade: C")
else:
    print("Invalid input")