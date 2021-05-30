import re


def is_int(string):
    regex = bool(re.search(r'^[+-]?\d+$', string))
    return regex


def is_float(string):
    regex = bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', string))
    return regex


while True:
    numero = input('Digite um número: ')

    if is_int(numero):
        numero = int(numero)
        print(f'Número convertido para inteiro: {numero}\n')
        continue
    else:
        print('Não foi possível converter o número para inteiro.')

    if is_float(numero):
        numero = float(numero)
        print(f'Número convertido para float: {numero}\n')
    else:
        print('Não foi possível converter o número para float.\n')
