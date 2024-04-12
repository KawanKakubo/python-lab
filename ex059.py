import time

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

acao = input("""    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
>>>>>Qual sua opção?
""").strip()

while acao in '1234':
    print(acao)
    if acao == '1':
        soma = num1 + num2
        print(f"A soma entre {num1} e {num2} é igual à {soma}!")
        time.sleep(1)
        print("Retornando ao menu principal!")
        time.sleep(1)
    elif acao == '2':
        mult = num1 * num2
        print(f"A multiplicação entre {num1} e {num2} é igual à {mult}!")
        time.sleep(1)
        print("Retornando ao menu principal!")
        time.sleep(1)
    elif acao == '3':
        if num1 > num2:
            print(f"O maior número é o {num1}.")
        else:
            print(f"O maior número é o {num2}.")
        time.sleep(1)
        print("Retornando ao menu principal!")
        time.sleep(1)
    elif acao == '4':
        print("Você escolheu digitar novos números:")
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        time.sleep(1)
        print("Retornando ao menu principal!")
        time.sleep(1)
    else:
        print("Opção inválida! Retornando ao menu original!")
        time.sleep(1)
    acao = input("""        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
    >>>>>Qual sua opção?
    """).strip()
