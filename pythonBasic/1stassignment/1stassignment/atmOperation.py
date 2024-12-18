balance = 0
while True:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current Balance:", balance)
    elif choice == 2:
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print("Deposited:", deposit)
    elif choice == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Withdrawn:", withdraw)
        else:
            print("Insufficient balance")
    elif choice == 4:
        break
    else:
        print("Invalid choice")
