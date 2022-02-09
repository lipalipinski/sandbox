#========== DISPLAY MAIN MATRIX =============

def display(m):

    matrix =[
    '                 .          .....         ......    ',
    '                . .         .    .       .          ',
    '               .   .        .    .       .          ',
    '              .     .       .....        .          ',
    '              .......       .    .       .          ',
    '              .     .       .    .       .          ',
    '              .     .       .....         ......    ',
    '                                                    ',
    '           ---------------------------------------- ',
    '       .  |            ][            ][             ',
    '      ..  |            ][            ][             ',
    '     . .  |            ][            ][             ',
    '       .  |            ][            ][             ',
    '       .  |            ][            ][             ',
    '       .  |            ][            ][             ',
    '       .  |            ][            ][             ',
    '          |            ][            ][             ',
    '          |======================================== ',
    '   ....   |            ][            ][             ',
    '  .    .  |            ][            ][             ',
    '       .  |            ][            ][             ',
    '      .   |            ][            ][             ',
    '     .    |            ][            ][             ',
    '    .     |            ][            ][             ',
    '  ......  |            ][            ][             ',
    '          |            ][            ][             ',
    '          |======================================== ',
    '   ....   |            ][            ][             ',
    '  .    .  |            ][            ][             ',
    '       .  |            ][            ][             ',
    '   ....   |            ][            ][             ',
    '       .  |            ][            ][             ',
    '       .  |            ][            ][             ',
    '  .    .  |            ][            ][             ',
    '   ....   |            ][            ][             ']

    large_x = [
    ' \\\    //  ',
    '  \\\  //   ',
    '   \\\//    ',
    '   //\\\    ',
    '  //  \\\   ',
    ' //    \\\\  ']

    large_o = [
    '//======\\\ ',
    '||      || ',
    '||      || ',
    '||      || ',
    '||      || ',
    '\\\\======// ']

    mapa = [{'r1': 10, 'r2': 15, 'yl': 12, 'yr': 21}]   #r1, r2 - nr of first/last row; yl, yr - nr of first/last char


    for y in [0,1,2]:      #row
        for x in [0,1,2]:  #column
            if m[y][x] == 'O':
                for i, line in enumerate(large_o):
                    matrix[10+(y*9)+i] = matrix[10+(y*9)+i][:(12+(14*x))] + line + matrix[10+(y*9)+i][23+(14*x):]
            elif m[y][x] == 'X':
                for i, line in enumerate(large_x):
                    matrix[10+(y*9)+i] = matrix[10+(y*9)+i][:(12+(14*x))] + line + matrix[10+(y*9)+i][23+(14*x):]



    for line in matrix:
        print(line)

#========= DISPLAY PLAYER =================

def display_turn(char):
    print(f"\nIt's {char}'s turn:")


#========== USER MOVE INPUT ================
def user_position(m):

    move = ['' , '']   #[column_abc, row_123]
    range_123 = [1 , 2 , 3]
    range_abc = {'a' : 0 , 'b' : 1 , 'c' : 2}
    free = False


    while free == False:                                      # check if desired position is free

        while move[0] not in range_123 or move[1] not in range_abc.keys():
            inp = input('Type your move (e.g. a1, b2), and hit [ENTER]: ')

            if len(inp) == 2:                                       #len(inp) check
                move[1] = inp[0]
            else:
                continue

            if inp[1].isdigit() and int(inp[1]) in range_123:       #user input validation
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
            print(f'\n{m_dep[w]} HAS WON!!!')
            return True
        w += 3

    for i in range(0, len(m_dep)):                          # REMIS case check
        if m_dep[i] == ' ':
            break
    else:
        return '\nREMIS\n'

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

#============ CLEAR SCREEN =====================
def clr_scr():
    print('\n'*100)


# ========================== PLAY THE GAME =====================================

quit_game = False
turn = True
game_ended = False
new_game = True

while quit_game == False:

    if new_game:
        print('Welcome to the new game!')
        matrix = [[' ',' ',' '],                #clean up main matrix
                  [' ',' ',' '],
                  [' ',' ',' ']]
        new_game = False                        #turn of new game prompt

    if turn:                                    # check which player moves
        player = 'X'
    else:
        player = 'O'

    clr_scr()
    if turn:                                    # human moves
        display(matrix)
        display_turn(player)                    # who's turn it is
        move = user_position(matrix)
        matrix = put_x(move , player , matrix)  # update matrix

    else:                                       # ai moves
        move = player_b(matrix, move)
        matrix = put_x(move , player , matrix)  # update matrix
        clr_scr()




    if winner_check(matrix) == True:
        display(matrix)                         #check if game has been won
        quit_game = not play_again()            #if yes, play again menu
        new_game = True                         # turn on new game prompt

    elif winner_check(matrix) == False:         #if game is not won, continue
        pass

    else:
        display(matrix)                         #if it's a REMIS
        print("It's a remis!")                  # say it
        quit_game = not play_again()            #ask for new game
        new_game = True                         #turn on new game prompt


    turn = not turn                             #change player

print('Bye!')
