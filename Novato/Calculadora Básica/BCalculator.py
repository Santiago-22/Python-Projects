print('Seja bem-vindo a Calculadora do pombo!\n')

Num1, Num2 = map(int, input('Digite os dois numeros que deseja utilizar\n').split())

Operação = input('Qual operação deseja realizar?(+ ; - ; * ; /)\n')

if Operação == '+':
    print('Então você quer somar:')
    print(Num1, '+', Num2, 'é igual a', Num1 + Num2)

elif Operação == '-':
    print('Então você quer subtrair:')
    print(Num1, '-', Num2, 'é igual a', Num1 - Num2)

elif Operação == '*':
    print('Então você quer multiplicar:')
    print(Num1, '*', Num2, 'é igual a', Num1 * Num2)

elif Operação == '/':
    print('Então você quer dividir:')
    print(Num1, '/', Num2, 'é igual a', Num1/Num2)
