import random
from time import sleep

def build_game():
    matrix = [['   ' for r in range(3)] for r in range(3)]
    return matrix

def show_matrix(matrix):
    for r in matrix:
        print(r)

# para o jogador
def winner_diagonal(matrix):
    win = False
    if matrix[0][0] == ' X ' and matrix[1][1] == ' X ' and matrix[2][2] == ' X ':
        win = True
        print('d1')

    if matrix[0][2] == ' X ' and matrix[1][1] == ' X ' and matrix[2][0] == ' X ':
        win = True
        print('d2')

    return win

def winner_colum(matrix):
    win = False
    if matrix[0][0] == ' X ' and matrix[1][0] == ' X ' and matrix[2][0] == ' X ':
        win = True
        print('c1')

    if matrix[0][1] == ' X ' and matrix[1][1] == ' X ' and matrix[2][1] == ' X ':
        win = True
        print('c2')

    if matrix[0][2] == ' X ' and matrix[1][2] == ' X ' and matrix[2][2] == ' X ':
        win = True
        print('c3')
    
    return win

def winner_row(matrix):
    win = False
    count_r0 = 0
    count_r1 = 0
    count_r2 = 0
    
    for r in matrix[0]:
        for c in r:
            if c == ' X ':
                count_r0 += 1
    
    for r in matrix[1]:
        for c in r:
            if c == ' X ':
                count_r1 += 1
    
    for r in matrix[2]:
        for c in r:
            if c == ' X ':
                count_r2 += 1

    if count_r0 == 3 or count_r1 == 3 or count_r2 == 3:
        win = True
        print(f'wr0 = {count_r0}\nwr1 = {count_r1}\nwr2 = {count_r2}')
    return win

def win(matrix):
    win = False
    if winner_diagonal(matrix) == True or winner_colum(matrix) == True or winner_row(matrix) == True:
        win = True
        show_matrix(matrix)
        print('Parabéns! Você é o vencedor!')
    return win

# para o pc
def cpu_mov():
    r = random.choice(range(3))
    c = random.choice(range(3))
    return r, c

def loser_diagonal(matrix):
    lose = False
    if matrix[0][0] == ' O ' and matrix[1][1] == ' O ' and matrix[2][2] == ' O ':
        lose = True
        print('d1')
        
    if matrix[0][2] == ' O ' and matrix[1][1] == ' O ' and matrix[2][0] == ' O ':
        lose = True
        print('d2')   
    return lose

def loser_colum(matrix):
    lose = False
    if matrix[0][0] == ' O ' and matrix[1][0] == ' O ' and matrix[2][0] == ' O ':
        lose = True
        print(f'c1')
    
    if matrix[0][1] == ' O ' and matrix[1][1] == ' O ' and matrix[2][1] == ' O ':
        lose = True
        print('c2')
        
    if matrix[0][2] == ' O ' and matrix[1][2] == ' O ' and matrix[2][2] == ' O ':
        lose = True
        print('c3')
    return lose

def loser_row(matrix):
    lose = False
    count_r0 = 0
    count_r1 = 0
    count_r2 = 0
    
    for r in matrix[0]:
        for c in r:
            if c == ' O ':
                count_r0 += 1
    
    for r in matrix[1]:
        for c in r:
            if c == ' O ':
                count_r1 += 1
    
    for r in matrix[2]:
        for c in r:
            if c == ' O ':
                count_r2 += 1

    if count_r0 == 3 or count_r1 == 3 or count_r2 == 3:
        lose = True
        print(f'\nlr0 = {count_r0}\nlr1 = {count_r1}\nlr2 = {count_r2}')
    return lose

def lose(matrix):
    lose = False
    if loser_diagonal(matrix) == True or loser_colum(matrix) == True or loser_row(matrix) == True:
        lose = True
        show_matrix(matrix)
        print(f'Que pena... Tente novamente!')
    return lose


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
    if (countX == 4 and countO == 4):
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
    r = int(input('Em qual linha quer jogar? '))
    while r < 1 or r > 3:
        r = int(input('Digite um número entre 1 e 3. '))
    c = int(input('Em qual coluna quer jogar? '))
    while c > 3 or c < 1:
        c = int(input('Digite um número entre 1 e 3. '))
    return r - 1, c - 1

#  preenchimento
def fill_matrix(matrix, play, jogador, r, c):
    matrix[r][c] = play[jogador]

def player_play(matrix, play, jogador):
    r, c = get_mov_valid()
    if is_mov_valid(matrix, r, c):
        try:
            fill_matrix(matrix, play, jogador, r, c)
        except:    
            r, c = get_mov_valid()
            fill_matrix(matrix, play, jogador, r, c)
            pass
    
# jogo
def play_game():
    jogador = 0
    play = [' X ', ' O ']
    matrix = build_game()
    while draw_match(matrix) == False and not win(matrix) and not lose(matrix):
        show_matrix(matrix)
        if jogador % 2 == 0:
            player_play(matrix, play, jogador)
            jogador = (jogador+1) % 2
        else:
            r, c = cpu_mov()
            if is_mov_valid(matrix, r, c):
                try:
                    print('Jogando...')
                    sleep(0.7)
                    fill_matrix(matrix, play, jogador, r, c)
                    jogador = (jogador+1) % 2
                except:    
                    print('Jogando...')
                    sleep(0.7)
                    r, c = cpu_mov()
                    fill_matrix(matrix, play, jogador, r, c)
                    pass

if __name__ == '__main__':
    play_game()