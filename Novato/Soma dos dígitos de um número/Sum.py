Numero = int(input('Digite o numero no qual você deseja somar os dígitos'))

Soma = 0

while Numero:
    Soma += Numero % 10
    Numero //= 10

print('A Soma é', Soma)