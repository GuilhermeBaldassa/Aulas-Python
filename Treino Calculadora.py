#Calculadora básica em python

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
x = str(input('Digite e operação desejada: '))

if x == '+':
    resultado = a + b
    print('O resultado é: {}'.format(resultado))

elif x == '-':
    resultado = a - b
    print('O resultado é: {}'.format(resultado))

elif x == '*':
    resultado = a * b
    print('O resultado é: {}'.format(resultado))

elif x == '/':
    resultado = a / b
    print('O resultado é: {}'.format(resultado))

