import random
a = int(input('Enter the lower boundary: '))
b = int(input('Enter the upper Boundary: '))
if a > b:
    print('Lower boundary should be smaller than Upper boundary..')
else:
    value = random.randint(a, b)
    print('The random Integer is:', value)
    if value % 2 == 0:
        print(value, "is an even number ")
    else:
        print(value, "is an odd number  ")
    if value > 0:
        print(value, " is a positive number")
    elif value == 0:
        print("is a Zero")
    else:
        print(value, "is a negative number")
    factor_count = 0
    for i in range(1, value+1):
        factor = value % i
        if factor == 0:
            factor_count = factor_count+1
    if factor_count == 2:
        print(value, "is a prime number")
    else:
        print(value, "is a composite number")