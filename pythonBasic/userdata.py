# var1 = int(input("enter a number: "))
#rang = int(input("enter a range: "))
'''i=0
i+=1
print(f"{var1} x {i} = {(var1*i)}")
i+=1
print(f"{var1} x {i} = {(var1*i)}")
i+=1
print(f"{var1} x {i} = {(var1*i)}")
i+=1
print(f"{var1} x {i} = {(var1*i)}")
i+=1
print(f"{var1} x {i} = {(var1*i)}")
'''

#print(f"first number {var1} and second number {var2} \nSum of these two numbers {(var1+var2)}")
'''for i in range(1,rang+1):
    print(f"{var1} x {i} = {(var1*i)}")'''
    
var1 = int(input("enter a number: "))
var2 = int(input("enter second number: "))
print("before swap: ",var1,var2)
var1 = var1+var2
var2 = var1-var2
var1 = var1 - var2

print("after swap: ",var1,var2)
var1,var2 = var2,var1
print("unswapped= ",var1,var2)

