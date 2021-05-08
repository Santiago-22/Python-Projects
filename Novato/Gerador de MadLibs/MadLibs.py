import time 

print('Vamos brincar de MadLibs?\n\n')

print('Digite a opção dejesada\n')

print('1 - Jogar')
print('2 - Regras\n')

Opção = int(input())

if Opção == 1:
    print('Vamos começar!\n')
    Nacionalidade, Adjetivo1 = map(str, input('A pizza foi inventada por um(Digite uma Nacionalidade e um Adjetivo)\n').split())
    Nome = input('chamado (digite um nome).\n')
    Substantivo1 = input('Para fazer uma pizza você precisa de uma pitada de (digite um ingediente),\n')

    print('Então você quer dizer que')
    print('A pizza foi inventada por um', Nacionalidade, Adjetivo1, 'chamado', Nome+'.', 'Para fazer uma pizza você precisa de', Substantivo1)

if Opção == 2:
    print('MadLibs é um jogo popular nos Estados Unidos')
    time.sleep(3)
    print('O objetivo é criar uma história maluca.')
    time.sleep(3)
    print('Para isso você deve preencher os espaços em branco de uma dada história\ne no final os espaços brancos que você preencheu formarão a história')
    time.sleep(7)
