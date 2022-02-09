#========== DISPLAY 3x3 MATRIX =============
def display(m):
    print(f'  a b c')
    print(f'1 {m[0][0]}|{m[0][1]}|{m[0][2]}')
    print(' -------')
    print(f'2 {m[1][0]}|{m[1][1]}|{m[1][2]}')
    print(' -------')
    print(f'3 {m[2][0]}|{m[2][1]}|{m[2][2]}')


#========= DISPLAY PLAYER =================

def display_turn(char):
    print(f"It's {char}'s turn:")


#========== USER MOVE INPUT ================
def user_position(m):

    move = ['' , '']
    range_123 = [1 , 2 , 3]
    range_abc = {'a' : 0 , 'b' : 1 , 'c' : 2}
    free = False


    while free == False:                                      # check if desired position is free

        while move[1] not in range_abc.keys():                # column input validation
            move[1] = input('Choose a column (a, b, c): ')
            if move[1] not in range_abc.keys():
                print('a, b, or c?')

        while move[0] not in range_123:                         # row input validation
            move[0] = input('Choose a row (1, 2, 3): ')
            if move[0].isdigit() and int(move[0]) in range_123:
                move[0] = int(move[0])
            else:
                print('1, 2, or 3?')



        move[1] = range_abc[move[1]]                            # maping user-friendly input values to matrix
        move[0] = move[0] -1

        if m[move[0]][move[1]] != ' ':                          # check if position is free
            print('This position has already been taken')
            continue
        else:
            free = True

    return move



#========== PUT 'char' INTO MATRIX ===============
def put_x(move , char , m):
    m[move[0]][move[1]] = char
    return m





#=============== WINNER CHECK ===============
def winner_check(m):
    m_dep = []
    m_depx = []
    m_depy = []

    for x in [0,1,2]:
        for y in [0,1,2]:
            m_depx.append(m[x][y])
            m_depy.append(m[y][x])


    for i in [2,1,0]:
        for j in [0,1,2]:
            m_depx.append(m[j][j])
            m_depy.append(m[i][j])

    m_dep = m_depx + m_depy

    for w in range(0, len(m_dep)-2):
        if m_dep[w] == m_dep[w+1] == m_dep[w+2] != ' ':
            print(f'{m_dep[w]} HAS WON!!!')
            return True

    return False


#============== PLAY AGAIN PROMPT ================
def play_again():
    ans = ''
    while ans not in ['y', 'Y', 'n', 'N']:
        ans = input('Do you want play again (Y/N): ')
    if ans in ['y' , 'Y']:
        return True
    else:
        return False

#============================================== PLAY THE GAME ========================
quit_game = False
turn = True
game_ended = False
new_game = True

while quit_game == False:

    if new_game:
        print('Welcome to the new game!')
        matrix = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]
        new_game = False

    if turn:
        player = 'x'
    else:
        player = 'o'

    display(matrix)
    display_turn(player)
    move = user_position(matrix)
    put_x(move , player , matrix)
    display(matrix)


    if winner_check(matrix):
        user_quit = not play_again()
        new_game = True

    turn = not turn

print('Bye!')
