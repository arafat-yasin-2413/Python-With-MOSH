'''

myList =[1,2,3,4,5]
popped_value = myList.pop()
print(f'popped value: {popped_value}')
print(myList)

print(myList.index(3))

print()
numbersList = [10,20,20,30,40,20,50]
# print(40 in numbersList)
if 50 in numbersList:
    idx = numbersList.index(50)

print(idx)

print(numbersList.count(20))

print()

nums=[10,20,70,80,40,35]
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)

print()

lst1 = [10,20,30]
lst2 = lst1.copy()
print(lst1)
print(lst2)
lst1.append(40)
print(lst1)
print(lst2)


'''




# remove duplicate from a list

myList = [10,20,30,40,20,50,20,30,20]
print(myList)

# আরেকটা খালি লিস্ট নিবো। এই মাইলিস্টের উপর লুপ চালিয়ে
# ... চেক করতে থাকবো যে, নতুন লিস্ট টার মধ্যে মাইলিস্টের কেউ
# ... আছে কিনা। 'in' অপারেটর ব্যবহার করতে পারি।

another_list =[]
for numbers in myList:
    if numbers not in another_list:
        another_list.append(numbers)

print(another_list)
