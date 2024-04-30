def contador(inicio, fim, passo):
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(f'{i} ', end='')
    if fim < inicio:
        passo = -passo
        fim -= 2
        for i in range(inicio, fim+1, passo):
            print(f'{i} ', end='')


print('Contador personalizado!')
ini = int(input("Início: "))
f = int(input("Fim: "))
pas = int(input("Passo: "))
contador(ini, f, pas)
