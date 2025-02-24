from math import sqrt

"""
Questão 1: Converter as seguintes expressões para o interpretador Python:
a) 10 + 20 × 30
b) 42 ÷ 30
c) (94 + 2) × 6 − 1
"""
a = 10 + 20 * 30
print(a)
b = 4**2 / 30
print(b)
c = (9**4 + 2) * 6 - 1
print(f'{c}\n')

""" 
Questão 2: o interpretador Python (ou num arquivo.py) resolva a expressão: 10%3 × 102 + 1 − 10 × 4/2. Resolva também usando apenas lápis e papel. 
O resultado a ser encontrado é 81.0
"""

d = 10**3 * 10**2 + 1 - 10 * 4/2
print(f'{d}\n')

"""
Questão 3: Faça um programa que resolva a soma de três variáveis e imprima o resultado na tela.
"""
def soma(a, b, c):
    return a + b + c

e = soma(1, 2, 10)
print(f'{e}\n')

"""
Questão 4: Considerando um salário de R$ 750.00, determine numericamente um aumento de 15%
"""
salario = 750
aumento = 15
print(f'{salario + (salario + aumento / 100)}\n')

"""
Questão 5: Escreva um programa que, a partir da entradas dos valores de dias, horas, minutos e segudos,
calcule o tempo total em segundos.
"""
dias = int(input('Digite um tempo em dias: '))
horas = int(input('Digite um tempo em horas: '))
minutos = int(input('Digite um tempo em minutos: '))
segundos = int(input('Digite um tempo em segundos: '))

total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print(f'\nO total de segundos é: {total} segundos\n')

"""
Questão 6: Escreva um programa que pergunte três números para o usuário e que devolva como resposta
qual o maior deles.
"""
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira mais um número: '))

maior = max(n1, n2, n3)

print(f'O maior número é: {maior}\n')

"""
Questão 7: Escreva um programa em Python que verifique se um número é primo.
"""
import math

num = int(input("Digite um número: "))

def eh_primo(n):
    if n <= 1:
        return False  
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:
            return False  
    return True  

if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
