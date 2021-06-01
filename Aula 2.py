a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#.colocar chaves dentro das aspas e . format(....) concatena qualquer variável.
print('Soma: {soma}'
      ' \nSubtração: {subtracao}'
      '\nMultiplicação: {multiplicacao}'
      '\nDivisâo: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))


