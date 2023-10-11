is_hot = False
# is_hot = True
# is_cold = True
is_cold = False

if is_hot:
    print('Its a hot day')
    print('Go back to your house')
    print('Drink plenty of water')
elif is_cold:
    print('Its a cold day')
    print('Wear warm clothes')
else:
    print('Its a lovely day')
print('Enjoy your day')

print('**************************')
print()

# Homework
price = 1000000
good_credit = True

if good_credit:
    print(f"${0.1*price} down payment required")
else:
    print(f"${0.2*price} down payment required")


