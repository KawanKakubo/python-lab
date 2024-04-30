def fatorial(num, show=False):
    if show is False:
        f = 1
        for v in range(num, 0, -1):
            f *= v
        return f
    else:
        f = 1
        for v in range(num, 0, -1):
            f *= v
            print(f'{v}', end='')
            if v > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        return f


print(fatorial(8))
