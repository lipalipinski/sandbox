#============================================
#
#                TicTacToe v1
#                2022 by JL
#
#========== DISPLAY MAIN MATRIX =============
from random import randint

def display(m):

    matrix =[
    '                  /////        /////////        ///////     ',
    '                 /     /        /       /      /            ',
    '                /       /       /       /      /            ',
    '                /////////       ////////       /            ',
    '                /       /       /       /      /            ',
    '                /       /       /       /      /            ',
    '               ///     ///     /////////        ///////     ',
    '                                                            ',
    '       /                   ][              ][               ',
    '     / /                   ][              ][               ',
    '    /  /                   ][              ][               ',
    '       /                   ][              ][               ',
    '       /                   ][              ][               ',
    '       /                   ][              ][               ',
    '       /                   ][              ][               ',
    '      ///                  ][              ][               ',
    '             ============================================== ',
    '                           ][              ][               ',
    '    /////                  ][              ][               ',
    '   /     /                 ][              ][               ',
    '         /                 ][              ][               ',
    '        /                  ][              ][               ',
    '       /                   ][              ][               ',
    '     /                     ][              ][               ',
    '   ///////                 ][              ][               ',
    '             ============================================== ',
    '    /////                  ][              ][               ',
    '   /     /                 ][              ][               ',
    '         /                 ][              ][               ',
    '    /////                  ][              ][               ',
    '         /                 ][              ][               ',
    '         /                 ][              ][               ',
    '   /     /                 ][              ][               ',
    '    /////                  ][              ][               '] #W = 60ch


    large_x = [
    '  \\\    // ',
    '   \\\  //  ',
    '    \\\//   ',
    '    //\\\   ',
    '   //  \\\  ',
    '  //    \\\\ ']

    large_o = [
    '  //====\\\  ',
    ' //      \\\ ',
    ' ||      || ',
    ' ||      || ',
    ' \\\\      // ',
    '  \\\\====//  ']


    for y in [0,1,2]:      #row
        for x in [0,1,2]:  #column
            if m[y][x] == 'O':
                for i, line in enumerate(large_o):
                    matrix[9+(y*9)+i] = matrix[9+(y*9)+i][:(14+(16*x))] + line + matrix[10+(y*9)+i][26+(16*x):]
            elif m[y][x] == 'X':
                for i, line in enumerate(large_x):
                    matrix[9+(y*9)+i] = matrix[9+(y*9)+i][:(14+(16*x))] + line + matrix[10+(y*9)+i][25+(16*x):]

    for line in matrix:
        print(line)
#============ MAIN MENU ===================
def main_menu():
    '''
    1 - single player, 2- multiplayer 3, quit
    '''

    option = 0
    logo =[
    '  |/////||/||///|   |/////|  /  |///|   |/////||////||///|  ',
    '    |/|  |/||/   ///  |/|   /_/ |/   ///  |/|  |/||/||//|   ',
    '    |/|  |/||///|     |/|  /   /|///|     |/|  |////||///|  ',
    '                                                  by JL     ',
    '                                                            ',
    '                                                            ']

    for line in logo:
        print(line)

    print('{0:^60}\n{1:^60}\n{2:^60}\n{3:^60}'.format('MENU:','1 - single player','2 - multi player','3 - quit')+'\n'*5)
    while option not in [1,2,3]:
        choice = input()
        if choice.isdigit():
            option = int(choice)
        else:
            continue

    return option
#========= DISPLAY PLAYER =================

def display_turn(char):
    print(f"\nIt's {char}'s turn:\n")


#========== USER MOVE INPUT ================
def user_position(m):

    move = ['' , '']   #[column_abc, row_123]
    range_123 = [1 , 2 , 3]
    range_abc = {'a' : 0 , 'b' : 1 , 'c' : 2}
    free = False


    while free == False:                                      # check if desired position is free

        while move[0] not in range_123 or move[1] not in range_abc.keys():
            inp = input('Type your move (e.g. a1, b2), and hit [ENTER]: ')

            if inp == 'Q':                                           # QUIT TO MENU
                return False

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
def player_b(m, last_move, player_mrk):
    """
    m - matryca gry
    last_move - [0-2, 02]
    player_mrk - ''
    """


    m_dep = []
    m_depx = []
    m_depy = []
    m_depd = []

    i = 2
    for x in [0,1,2]:
        m_dep.append((m[x][x],(x,x)))
        m_depd.append((m[i][x],(i,x)))
        i -= 1
        for y in [0,1,2]:
            m_depx.append((m[x][y],(x,y)))
            m_depy.append((m[y][x],(y,x)))
            pass


    m_dep += m_depd + m_depx + m_depy


    w = 0                                           # check for winning oportunity
    while w < len(m_dep)-2:
        m_check = [m_dep[w], m_dep[w+1], m_dep[w+2]]
        for i in [0,1,2]:
            print(m_check[-i][0],m_check[1-i][0], m_check[2-i][0])
            if m_check[0-i][0] == ' ' and m_check[1-i][0] == m_check[2-i][0] == player_mrk:
                return m_check[0-i][1]
                pass
            w += 1

    w = 0                                           # check for block oportunity
    while w < len(m_dep)-2:
        m_check = [m_dep[w], m_dep[w+1], m_dep[w+2]]
        for i in [0,1,2]:
            print(m_check[-i][0],m_check[1-i][0], m_check[2-i][0])
            if m_check[0-i][0] == ' ' and m_check[1-i][0] == m_check[2-i][0] == 'X':
                return m_check[0-i][1]
                pass
            w += 1

    q = []

    while len(q) != 6:
        p = randint(0,5)
        if p not in q:
            q.append(p)

    for i in q:
        if i == 0 and m[1][1] == ' ':                              #if center is free, go for it
            return [1 , 1]
        elif i == 1 and m[0][0] == ' ':
            return [0 , 0]
        elif i == 2 and m[0][2] == '':
            return [0 , 2]
        elif i == 3 and m[2][0] == ' ':
            return [2 , 0]
        elif i == 4 and m[2][2] == ' ':
            return [2 , 2]
        elif i == 5 and m[last_move[1]][last_move[0]] == ' ':
            return [last_move[1] , last_move[0]]

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
    m_depd = []

    i = 2
    for x in [0,1,2]:
        m_dep.append(m[x][x])
        m_depd.append(m[i][x])
        i -= 1
        for y in [0,1,2]:
            m_depx.append(m[x][y])
            m_depy.append(m[y][x])
            pass


    m_dep += m_depd + m_depx + m_depy




    w = 0
    while w < len(m_dep)-2:
        if m_dep[w] == m_dep[w+1] == m_dep[w+2] != ' ':
            print(f'\n"{m_dep[w]}" HAS WON!!!')
            return True
        w += 3

    for i in range(0, len(m_dep)):                          # tie case check
        if m_dep[i] == ' ':
            break
    else:
        return 'TIE'

    return False
# ============= STAT DISPLAY =====================
def stat_display(stats):
    print('{0:>28} {1:>5} : {2:<5} {3:<28}\n\n'.format('Player X',stats[0], stats[1],'Player O'))
    #print(f'Player X {x} : {y} Player O')



#============== PLAY AGAIN PROMPT ================
def play_again(menu):
    wanna = ''
    while wanna not in ['y', 'Y', 'n', 'N']:
        wanna = input('\nDo you want play again (Y/N): ')


    if wanna in ['y' , 'Y']:
        return menu
    else:
        return 0


#============ GOODBYE =========================
def goodbye():
    print('\nBye! \nTicTacToe by JL 2022')
#============ CLEAR SCREEN =====================
def clr_scr():
    print('\n'*100)


# ========================== PLAY THE GAME =====================================

quit_game = False
turn = False
game_ended = False
new_game = True
first_move = True
menu = 0


while menu != 3:

    if new_game:
        clr_scr()
        if menu == 0:
            menu = main_menu()                  # 1 - single player, 2 - multiplayer, 3 - quit
            stats = [0,0]                       # reset stats
        if menu == 3:
            break

        matrix = [[' ',' ',' '],                # clean up main matrix
                  [' ',' ',' '],
                  [' ',' ',' ']]
        if first_move:                          #if first move = true player starts the game
            turn = True
        else:                                   #else - AI starts
            turn = False
        first_move = not first_move             #make the other player start next game
        new_game = False                        # turn off new game prompt


    if turn:                                    # check which player moves
        player = 'X'
    else:
        player = 'O'

    clr_scr()
    stat_display(stats)
    if turn:                                    # human moves
        display(matrix)
        display_turn(player)                    # who's turn it is
        move = user_position(matrix)
        if move == False:                       # Quit to the menu
            menu = 0
            new_game = True
            pass
        else:
            matrix = put_x(move , player , matrix)  # update matrix

    else:
        if menu == 1:                                  # ai moves
            move = player_b(matrix, move, 'O')
            matrix = put_x(move , player , matrix)  # update matrix
            clr_scr()
        elif menu == 2:                             #
            display(matrix)
            display_turn(player)                    # who's turn it is
            move = user_position(matrix)
            if move == False:                       # Quit to the menu
                menu = 0
                new_game = True
                pass
            else:
                matrix = put_x(move , player , matrix)  # update matrix




    if winner_check(matrix) == True:
        if turn == True:                        #update stats
            stats[0] += 2
        else:
            stats[1] += 2
        clr_scr()
        stat_display(stats)
        display(matrix)
        winner_check(matrix)                    # check if game has been won
        menu = play_again(menu)                     # yes = play again, no = show main menu
        new_game = True                         # turn on new game prompt


    elif winner_check(matrix) == False:         # if game is not won, continue
        pass

    else:
        stats[0] += 1
        stats[1] += 1
        clr_scr()
        stat_display(stats)
        display(matrix)                         # if it's a REMIS
        print("\nIt's a tie!")                  # say it
        menu =  play_again(menu)            # ask for new game
        new_game = True                         # turn on new game prompt


    turn = not turn                             # change player

goodbye()
clr_scr()
