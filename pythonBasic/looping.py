
# for a in  range(1,6):
#     print("lavanya")
# for i in range(0,11):
#     print(f"{x if i%2}")

# for a in range(0,10,2):
#     print("lavanya nayak")
    
# for i in range(10,0,-1):
#     print(i)
# name ="" 
# i=0
# while(i < 10):
#     print('lavanya')
#     i+=1  
# for i in ["lavanya"]:
#     name= " ".join(i)
# print(name)
# for i in "lavanya":
#     print(i, end =' ')
# i = 1.5    
# while(i<6):
#     print("lava")
#     i+=1


num = int(input("enter a number:  "))
rang = int(input("enter a range: "))

for i in range(1,rang+1):
    print(f"{num} * {i} = {num* i}")
i=1   
while(i <= rang):
    print(f"{num} * {i} = {num* i}")
    i+=1