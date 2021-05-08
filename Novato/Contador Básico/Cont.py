import time

Contador = 0

while True:
    Add = input('Deseja continuar contando? s/n \n')
    if Add == 's':
        Contador += 1
        time.sleep(0.5)
        print('Por enquanto você contou até', Contador,'\n')
        time.sleep(0.5)
    elif Add != 's':
        break

print('Você contou até', Contador)