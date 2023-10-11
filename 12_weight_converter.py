weight = int(input('Enter weight : '))
# print(type(weight))

print(f"Given weight was in kg or pound? ")
format = input('Type K or L : ')


if format.upper() == 'K':
    result = (weight//0.454)
    print(f'You are {result} pounds')
elif format.upper() == 'L':
    result = weight*0.454
    print(f'You are {result} kg')

