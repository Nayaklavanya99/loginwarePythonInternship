# i=1
# while(i<=20):
#     if(i%2==0):
#         print(f"even {i}\n")
#     else:
#         print(f"odd {i}", end="\t\t")
    
#     i+=1 

# for num in range(1,51):
#     if(num % 2 == 0 and num % 3 !=0 ):
#         print("😂")
#     elif(num%3 == 0 and num% 2 !=0):
#         print("🐸")
#     elif(num%2 ==0 and num%3==0):
#         print("Fizz Buzz")
#     else:
#         print(num)
#rang = int(input("enter a range:  "))
rang= 5
count= 1
for i in range(1,rang):
    for j in range(i):
        print(f"{count}", end=" ")
        count+=1
    print()