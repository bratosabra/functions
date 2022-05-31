def printMax(x, y):
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'big')
    else:
        print(y, 'big')


printMax(3, 5)
print(printMax.__doc__)
