num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

choice = int(input("enter your choice\n1.addition\t2.subtraction\t3.multiplication\t4.division\t5.modulus:  "))

if (choice == 1):
    print(f"{num1} + {num2}\n{num1+num2}")
elif(choice == 2):
    print(f"{num1} - {num2}\n{num1-num2}")
elif(choice == 3):
    print(f"{num1} * {num2}\n{num1*num2}")
elif(choice == 4):
    if(num2 == 0):
        print("division by zero is not possible")
    else:
        print(f"{num1} / {num2}\n{float(num1/num2)}")
elif(choice == 5):
    if(num2 == 0):
        print("division by zero is not possible")
    else:
        print(f"{num1} % {num2}\n{float(num1%num2)}")


    
    
    