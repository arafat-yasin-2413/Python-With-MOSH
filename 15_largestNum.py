myList = [10,20,40,30]

# mx = -1
mx = myList[0]
for numbers in myList:
    if numbers > mx:
        mx = numbers

print(f"Largest number is : {mx}")