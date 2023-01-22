from random import randint

pc = randint(0,10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('qual seu palpite: '))

    palpites += 1


    if jogador == pc:
        acertou = True
    else:
        if jogador > pc:
            print('\033[31m menos,tente novamente\033[38m')
        if jogador < pc:
            print('\033[33m mais, tente novamente')

print(f'foram {palpites} tentantivas ')