# List
# var1 = [1,2,3,4,5,6,7,8,9,10]
# print("int: ",type(var1),var1)


# var2 = [2.3333,4.5,7.7,8.8]
# print("float: ",type(var2),var2)

# var3 = ["lavanya","shantala","chandan"]
# print("String: ",type(var3),var3)

# var4 = [var1,var2,var3,True,False,None]
# print("All: ",type(var4),var4)
# print("")
# print(var3.index("lavanya"))
# var3.insert(0,"sahil")
# print(var3)


# var4 = var3.copy()

# print(var4)
# del var4[-1]
# print(var4)

# print("Tuple")
# var1 = (1,1.0,"loginware",True)
# print(type(var1))

# dict = {"name":"lavanya",'age': 20}
# print(dict["name"])
# print(dict.keys(),": ",dict.values())
# print(dict.items())
# dict.update({"name":"lava"})

# a
# var1 = "     lavanya nayak"
# print(var1[-5:])
# print(var1.strip())
# print(var1.split(",")[0])

# var2 = "lOGINWARE IS IN @BANGALORE"
# var2 = var2.replace("BANGALORE","blore")
# var3= " "
# print(var2.split(" "))
# print(var2.isalnum())
# var4 = var2.split(" ") 
# print("".join(var4))
# li =[ 1,2,3,4]
# li.reverse()
# print(sorted(li))
# print(li)

keys = ["name","place","gender","contact"]
values = ["lavanya","bangalore","female",1234567890]

# dict = {keys[i]:values[i] for i in range(len(keys))}
dict1 = {keys[i]:values[i] for i in range(len(keys))}
print(dict1)
dict2 =dict(zip(keys,values))
print(dict2)