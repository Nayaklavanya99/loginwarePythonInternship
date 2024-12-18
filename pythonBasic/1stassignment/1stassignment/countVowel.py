s = input("Enter a string: ")
vowels = "aeiouAEIOU"
lists = []
count = 0
for char in s:
    if char in vowels:
        count += 1
        lists.append(char)
        
print("Number of vowels:", count)
print(lists)
