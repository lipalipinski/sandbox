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

    move = ['' , '']   #[abc, 123]
    range_123 = [1 , 2 , 3]
    range_abc = {'a' : 0 , 'b' : 1 , 'c' : 2}
    free = False


    while free == False:                                      # check if desired position is free

        while move[0] not in range_123 or move[1] not in range_abc.keys():
            inp = input('Type your move (e.g. a1, b2), and hit [ENTER]: ')
            if len(inp) == 2:                                       #len(inp) check
                move[1] = inp[0]
            if inp[1].isdigit() and int(inp[1]) in range_123:
                move[0] = int(inp[1])
            else:
                print('Entered value is not valid')
                continue


        move[1] = range_abc[move[1]]                            # maping user-friendly input values to matrix
        move[0] = move[0] -1

        if m[move[0]][move[1]] != ' ':                          # check if position is free
            print('This position has already been taken')
            continue
        else:
            free = True

    return move



#============================ PLAYER B =========================
def player_b(m, last_move):
    if m[1][1] == ' ':
        return [1, 1]
    elif m[last_move[1]][last_move[0]] == ' ':
        return [last_move[1] , last_move[0]]
    else:
        for i in [0,1,2]:
            for j in [0,1,2]:
                if m[i][j] == ' ':
                    return [i , j]



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



    w = 0
    while w < len(m_dep)-2:
        if m_dep[w] == m_dep[w+1] == m_dep[w+2] != ' ':
            print(f'{m_dep[w]} HAS WON!!!')
            return True
        w += 3

    for i in range(0, len(m_dep)):                          # REMIS case check
        if m_dep[i] == ' ':
            break
    else:
        return 'REMIS'

    return False


#============== PLAY AGAIN PROMPT ================
def play_again():
    wanna = ''
    while wanna not in ['y', 'Y', 'n', 'N']:
        wanna = input('Do you want play again (Y/N): ')


    if wanna in ['y' , 'Y']:
        return True
    else:
        return False


quit_game = False
turn = True
game_ended = False
new_game = True

while quit_game == False:

    if new_game:
        print('Welcome to the new game!')
        matrix = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        new_game = False

    if turn:
        player = 'x'
    else:
        player = 'o'

    display(matrix)
    display_turn(player)
    if turn:
        move = user_position(matrix)
    else:
        move = player_b(matrix, move)
    put_x(move , player , matrix)
    display(matrix)


    if winner_check(matrix) == True:
        quit_game = not play_again()
        new_game = True
        turn = not turn
    elif winner_check(matrix) == False:
        pass
    else:
        print("It's a remis!")
        quit_game = not play_again()
        new_game = True
        turn = not turn

    turn = not turn

print('Bye!')
