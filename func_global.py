x = 50


def func():
    global x
    print('x равен', x)
    x = 2
    print('Замена глобального x на', x)


func()
print('Значение х равняется', x)
