def func_outer():
    x = 2
    print('х равен', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Лок х сменился на', x)


func_outer()
