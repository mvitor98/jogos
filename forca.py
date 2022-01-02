import random
def mensagem_abertura():
    print('*' * 40)
    print('Bem vindo ao jogo de forca!')
    print('*' * 40)

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_escolhida = random.choice(palavras)
    palavra_secreta = palavra_escolhida.upper()
    return palavra_secreta #Deu um erro ('NoneType' object is not iterable) antes pq não coloquei esse return da variável

def letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input('\nDigite uma letra: ')
    chute = chute.strip().upper()
    while chute.isalpha() == False:
        print('Valor não reconhecido. Digite apenas letras!')
        chute = input('Digite uma letra: ')
        chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, acertos, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            acertos[index] = letra
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    acertos = letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(f'Palavra:\n'
          f'{acertos}')

    while (not acertou and not enforcou):

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, acertos, palavra_secreta)
        else:
            erros += 1
            print((f'Você errou! A letra {chute} não existe na palavra.\n'))
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = '_' not in acertos
        print(acertos)


    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(enforcou)

        print(f'\nPalavra:\n'
              f'{acertos}\n')
        print('Próxima tentativa...')


    print('Fim do jogo.')

if __name__ == '__main__':
    jogar()