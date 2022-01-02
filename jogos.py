import adivinhacao
import forca

def escolha_jogo():
    print('*'*40)
    print('**** Escolha um jogo! ****')
    print('*'*40)

    print('(1) Adivinhacao (2) Forca')

    jogo = int(input('Escolha um jogo: '))

    if jogo == 1:
        print('Jogando adivinhação...')
        adivinhacao.jogar()
    elif jogo == 2:
        print('Jogando forca...')
        forca.jogar()

if __name__ == '__main__':
    escolha_jogo()