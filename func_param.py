def printMax(a, b):
    if a > b:
        print(a, 'max')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'max')


printMax(15, 5)
x = int(input())
y = int(input())
printMax(x, y)
