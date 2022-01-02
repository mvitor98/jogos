import random

def jogar():

    print('*'*40)
    print('Bem vindo ao jogo de adivinhação!')
    print('*'*40)

    print('\nSelecione a dificuldade:\n'
          '(1) Fácil\n'
          '(2) Médio\n'
          '(3) Difícil')
    dificuldade = int(input('Dificuldade desejada: '))
    # adicionar uma geração aleatória de números entre 1 e 100 > import random
    numero_secreto = random.randint(1, 100)
    # print(numero_secreto)
    tentativa = 0
    if dificuldade == 1:
        tentativa = 20
    elif dificuldade == 2:
        tentativa = 10
    else:
        tentativa = 5
    # rodada = 1

    pontos = 1000

    # Trocando while pelo for e a função range(inicio, fim, [passo])
    # while rodada <= tentativa:
    for rodada in range(1, tentativa+1):
        print(f'\nRodada {rodada} de {tentativa}.\n')
        chute = input('Digite um número entre 1 e 100: ')
        print(f'Você digitou o número {chute}.\n')
        chute = int(chute)
        if chute < 1 or chute > 100:
            print('Você digitou um número inválido. Digite um número entre 1 e 100.')
            continue

        acerto = numero_secreto == chute
        menor = numero_secreto > chute
        maior = numero_secreto < chute

        if acerto:
            print(f'Parabéns! Você acertou!\n'
                  f'Seus pontos são: {pontos}.')
            break
        else:
            if menor:
                print('Que pena... Você digitou um número menor que o número secreto. Tente outra vez.\n')
            elif maior:
                print('Que pena... Você digitou um número maior que o número secreto. Tente outra vez.\n')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        # rodada += 1

    print('Fim do jogo.')

if __name__ == '__main__':
    jogar()