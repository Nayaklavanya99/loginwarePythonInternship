print("Please Insert your card")

lang = int(input("Select a language\n1.English\t2.Kannada\t3.Hindi: "))
choose_acc = int(input("Choose Account type:\n1.Saving\t2.Current: "))
choice = int(input("Choose the below options\n1.Withdraw\t2.Account balance\t3.Deposite: "))
orig=9999
depo_money= 1500
user_balance = 25000
bank_amt = 50000
password = int(input("enter your password: "))
if(password == orig):
    if(choice ==1):
        print("WITHDRAW")
        amt = int(input("enter amount to be withdraw: "))
        if(amt<= 0):
            print("Invalid input Try Again")
            print("YOUR TRANSACTION FAILED!")
        else:
            if(amt > bank_amt):
                print("Amount you have entered is high")
                print("Please visit later, Sorry for inconvience")
                print("TRANSACTION INTRUPTED!")
        print("Please Collect Your Money!")
    if(choice == 2):
        print(f"Total Amount: {user_balance}")
    if(choice == 3):
        print("Please insert your money ")
        inserted = True
        if (inserted == False):
            print("kindly Put Your Money inside the box")
        else:
            print(f"{depo_money} has been deposited\nThank you!")
else:
    print("You have entered wrong Password")
        
