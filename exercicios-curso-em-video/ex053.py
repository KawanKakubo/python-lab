frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f"A frase {junto} é um palíndromo, porque a ela invertida é {inverso} que é igual à original!")
else:
    print(f"A frase {junto} não é um palíndromo, porque ela invertida é {inverso} que é diferente da original!")