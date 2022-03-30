import random
from time import sleep
import os

def build_game():
    matrix = [['   ' for r in range(3)] for r in range(3)]
    return matrix

def show_matrix(matrix):
    for r in matrix:
        print(r)

def winner_diagonal(matrix):
    win = None
    lose = None
    if matrix[0][0] == ' X ' and matrix[1][1] == ' X ' and matrix[2][2] == ' X ':
        win = 'win'
        print('d1')
        return win

    if matrix[0][2] == ' X ' and matrix[1][1] == ' X ' and matrix[2][0] == ' X ':
        win = 'win'
        print('d2')
        return win

    if matrix[0][0] == ' O ' and matrix[1][1] == ' O ' and matrix[2][2] == ' O ':
        lose = 'lose'
        print('d1')
        return lose
        
    
    if matrix[0][2] == ' O ' and matrix[1][1] == ' O ' and matrix[2][0] == ' O ':
        lose = 'lose'
        print('d2')
        return lose

def winner_colum(matrix):
    win = None
    lose = None
    if matrix[0][0] == ' X ' and matrix[1][0] == ' X ' and matrix[2][0] == ' X ':
        win = 'win'
        print('c1')
        return win
    
    if matrix[0][1] == ' X ' and matrix[1][1] == ' X ' and matrix[2][1] == ' X ':
        win = 'win'
        print('c2')
        return win

    if matrix[0][2] == ' X ' and matrix[1][2] == ' X ' and matrix[2][2] == ' X ':
        win = 'win'
        print('c3')
        return win

    if matrix[0][0] == ' O ' and matrix[1][0] == ' O ' and matrix[2][0] == ' O ':
        lose = 'lose'        
        print('c1')
        return lose
    
    if matrix[0][1] == ' O ' and matrix[1][1] == ' O ' and matrix[2][1] == ' O ':
        lose = 'lose'
        print('c2')
        return lose

    if matrix[0][2] == ' O ' and matrix[1][2] == ' O ' and matrix[2][2] == ' O ':
        lose = True
        print('c3')
        return lose

def winner_row(matrix):
    win = None
    lose = None
    countX_r0 = 0
    countO_r0 = 0
    countX_r1 = 0
    countO_r1 = 0
    countX_r2 = 0
    countO_r2 = 0
    for c in matrix[0]:
        if c == ' X ':
            countX_r0 += 1
        elif c == ' O ':
            countO_r0 += 1
    for c in matrix[1]:
        if c == ' X ':
            countX_r1 += 1
        elif c == ' O ':
            countO_r1 += 1
    for c in matrix[2]:
        if c == ' X ':
            countX_r2 += 1
        elif c == ' O ':
            countO_r2 += 1
    if countX_r0 == 3 or countX_r1 == 3 or countX_r2 == 3:
        win = 'win'
        return win
    elif countO_r0 == 3 or countO_r1 == 3 or countO_r2 == 3:
        lose = 'lose'
        return lose

def win(matrix):
    if winner_diagonal(matrix) == 'win' or winner_colum(matrix) == 'win' or winner_row(matrix) == 'win':
        win = True
        show_matrix(matrix)
        print('Parabéns! Você é o vencedor!')
        return win
    
    elif winner_diagonal(matrix) == 'lose' or winner_colum(matrix) == 'lose' or winner_row(matrix) == 'lose':
        lose = True
        show_matrix(matrix)
        print('Que pena, você perdeu...')
        return lose
# para o pc
def cpu_mov():
    r = random.choice(range(3))
    c = random.choice(range(3))
    return r, c
# empate
def counter(matrix):
    countX = 0
    countO = 0
    for r in matrix:
        for c in r:
            if c ==' X ':
                countX += 1
            elif c == ' O ':
                countO += 1
    return countX, countO

def draw_match(matrix):
    draw = False
    countX, countO = counter(matrix)
    if (countX == 5 and countO == 4) or (countX == 4 and countO == 5) and not win(matrix):
        show_matrix(matrix)
        print('Jogo empatado!')
        draw = True
    return draw
# validação do jogo
def is_mov_valid(matrix, r, c):
    ok = True
    if matrix[r][c] != '   ':
        ok = False
        print(f'Posição ({r+1}, {c+1}) ocupada. Tente novamente.')
    return ok

def get_mov_valid():
    try:
        r = int(input('Em qual linha quer jogar? '))
    except ValueError:
        r = int(input('Digite um número válido. '))
        while r < 1 or r > 3:
            r = int(input('Digite um número entre 1 e 3. '))
    try:
        c = int(input('Em qual coluna quer jogar? '))
    except ValueError:
        c = int(input('Digite um número válido. '))
        while c > 3 or c < 1:
            c = int(input('Digite um número entre 1 e 3. '))
    return r - 1, c - 1
#  preenchimento
def fill_matrix(matrix, play, player, r, c):
    matrix[r][c] = play[player]   
# jogo
def play_game():
    os.system('cls')
    sleep(0.5)
    print(f'\nIniciando a partida...')
    sleep(1.3)
    os.system('cls')
    player = 0
    play = [' X ', ' O ']
    matrix = build_game()
    while not draw_match(matrix) and not win(matrix):
        show_matrix(matrix)
        if player % 2 == 0:
            r, c = get_mov_valid()
            if is_mov_valid(matrix, r, c):
                try:
                    fill_matrix(matrix, play, player, r, c)
                    player = (player+1) % 2
                except:    
                    r, c = get_mov_valid()
                    fill_matrix(matrix, play, player, r, c)
                    pass
        else:
            r, c = cpu_mov()
            if is_mov_valid(matrix, r, c):
                try:
                    print('Jogando...')
                    sleep(0.7)
                    fill_matrix(matrix, play, player, r, c)
                    player = (player+1) % 2
                except:    
                    print('Jogando...')
                    sleep(0.7)
                    r, c = cpu_mov()
                    fill_matrix(matrix, play, player, r, c)
                    pass
        os.system('cls')

if __name__ == '__main__':
    play_game()
