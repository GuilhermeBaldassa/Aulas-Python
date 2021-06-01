from aula7_televisao import Televisao
from aula7_Calculadora2 import Calculadora
from aula8_contador_letras import contador_letras

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora()
print(calculadora.soma(5,10))
lista = ['cachorro', 'gato','elefante']
total_letras = contador_letras(lista)
print('O total de letras de cada palavra é: {}'.format(total_letras))