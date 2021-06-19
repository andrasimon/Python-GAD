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


if __name__ == '__main__':
    print(real_sum(1, 5, -3, 'random', [5, 6, 7, 8], param=7, param2='hi'))
    print(real_sum(4, 8, 9, 'real'))
    print(real_sum())