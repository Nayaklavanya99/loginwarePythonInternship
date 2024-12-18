issue_date = input("enter date (format: DD-MM-YYYY): ")
today= "29-11-2024"

over_due = int(input("Enter for how many days due was there:  "))
if (over_due == 0 ):
    print("Yay you have successfully returned the book!")
elif (over_due <=5 and over_due > 0):
    print("You are returning late\nPlease Pay 50 Rs as FINE!")
elif (over_due > 5 and over_due<=10):
    print("You are returning late\nPlease Pay 100 Rs as FINE!")
elif(over_due>10):
    print("You have exceeded your returning time\nKindly pay the Fine Rs 100")
else:
    print("Invalid input")