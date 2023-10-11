myList = [5,2,5,2,2]

# for item in myList:
#     print(item * 'x')

# my approach
# for item in myList:
#     for i in range(item):
#         print('x',end='')
#     print()


for item in myList:
    output = ""
    for i in range(item):
        output += "x"
    print(output)