# voter eligibility
age1 = int(input("enter age of person1 : "))
age2 = int(input("enter age of person2 : "))



if(age1>=18):
    print("person1 is eligible to vote")
else:
    print("person1 is not  eligible for voting")
if(age2>=18):
    print("person2 is eligible to vote")
else:
    print("person2 is not  eligible for voting")

    
def elibility(age):
    return age>18

print(f"person1 is eligible for voting: {elibility(age1)}")

print(f"person2 is eligible for voting: {elibility(age2)}")