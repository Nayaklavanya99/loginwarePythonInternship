age = int(input("enter your age: "))


if(age >= 18 and age<60):
    income  = int(input("Enter your monthly income: "))
    co_signer = input("Do you have Co signer? (Yes/No): ")
    if (income >30000):
        print("You are Eligibile for Loan!")
    elif(income < 30000 and co_signer.lower()=="yes"):
        print("You are Eligibile for Loan!")
    else:
        print("You are NOT Eligibile for Loan!")
else:
    print(f"Sorry {age} aged person are not eligibile for loan(it should be between 18 to 60)")