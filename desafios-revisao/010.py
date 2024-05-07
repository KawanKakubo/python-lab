def f1(funcao):
    return funcao()


def f2():
    return 1 + 2


exe = f1(f2)
print(exe)