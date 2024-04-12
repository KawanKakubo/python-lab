print('!CALCULADORA DE IMC!')
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Você está abaixo do peso, com imc = {imc}.')
elif 18.5 < imc <= 25:
    print(f'Você se encontra com o peso ideal, com imc = {imc}.')
elif 25 < imc <= 30:
    print(f'Você se encontra em sobrepeso, com imc = {imc}.')
elif 30 < imc <= 40:
    print(f'Infelizmente você é gordaum, está na obesidade :( com imc = {imc}.')
else:
    print(f'Você está com obesidade mórbida com imc = {imc}. Procure procurar por um médico imediatamente.')
