# funcție care primește un număr nedefinit de parametrii și calculeaza suma parametrilor care reprezintă
# numere întregi sau reale
def real_sum(*args, **kwargs):
    suma = 0
    for elem in args:
        if isinstance(elem, (int, float)):
            suma += elem
    for elem in kwargs.values():
        if isinstance(elem, (int, float)):
            suma += elem
    return suma


# suma tuturor numerelor de la [0, n] recursiv
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)


# suma numerelor pare de la [0, n]
def sum_n_even(n):
    n = n - n % 2
    if n == 0:
        return 0
    return n + sum_n_even(n - 2)


# suma numerelor impare de la [0, n]
def sum_n_odd(n):
    n = n - int(not (n % 2))
    if n == 1:
        return 1
    return n + sum_n_odd(n - 2)


if __name__ == '__main__':
    print('real_sum 1st run --> {}'.format(real_sum(1, 5, -3, 'random', [5, 6, 7, 8], param=7, param2='hi')))
    print('real_sum 2nd run --> {}'.format(real_sum(4, 8, 9, 'real')))
    print('real_sum 3rd run --> {}'.format(real_sum()))

    print('sum_n(3) --> {}'.format(sum_n(3)))

    print('sum_n_even(5) --> {}'.format(sum_n_even(5)))

    print('sum_n_odd(6) --> {}'.format(sum_n_odd(6)))
