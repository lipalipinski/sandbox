#============================================
#
#                TicTacToe v2
#                 v2022 by JL
#
#========== DISPLAY MAIN MATRIX =============
from random import randint

def clr_scr():
    print('\n'*100)
    pass

#===================== abstr class player ====================
class Player():

    def __init__(self, symbol):
         self.symbol = symbol       # str 'X'/'O'
         self.score = 0             # match score
         pass

    def move(self, m):           # m - current 3x3
        '''
        Returns 3x3 updated with a valid move
        '''
        return m

#===================== class human player =========================
class HumanPlayer(Player):

    def move(self, m):
        '''
        asks for a move, returns updated 3x3 m
        '''

        move = ['' , '']   #[Y, X]
        range_123 = [1 , 2 , 3]
        range_abc = {'a' : 0 , 'b' : 1 , 'c' : 2}
        free = False


        while True:                                      # check if desired position is free

            while move[0] not in range_123 or move[1] not in range_abc.keys():
                inp = input(f'Player {self.symbol}: type your move (e.g. a1, b2), and hit [ENTER]: ')

                #if inp == 'Q':                                           # QUIT TO MENU !!!!!!!!!!!!!!!!!!!!!!!!!
                #    return False

                if len(inp) == 2:                                       #len(inp) check
                    move[1] = inp[0]
                else:
                    continue

                if inp[1].isdigit() and int(inp[1]) in range_123:       #user input validation
                    move[0] = int(inp[1])
                else:
                    print('Entered value is not valid')
                    continue


            move[1] = range_abc[move[1]]                            # maping user-friendly input values to array
            move[0] = move[0] -1

            if m[move[0]][move[1]] != ' ':                          # check if position is free
                print('This position has already been taken')
                continue
            else:
                break

        m[move[0]][move[1]] = self.symbol
        return m


#======================= class AI player =================================
class AiPlayer(Player):

    def move(self, m):

        move = None # [y,x]
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
                if m_check[0-i][0] == ' ' and m_check[1-i][0] == m_check[2-i][0] == self.symbol:

                    move = m_check[0-i][1]
                    m[move[0]][move[1]] = self.symbol
                    return m

                w += 1

        w = 0                                           # check for block oportunity
        while w < len(m_dep)-2:
            m_check = [m_dep[w], m_dep[w+1], m_dep[w+2]]
            for i in [0,1,2]:
                if m_check[0-i][0] == ' ' and m_check[1-i][0] == m_check[2-i][0] == 'X':
                    move = m_check[0-i][1]
                    m[move[0]][move[1]] = self.symbol
                    return m
                w += 1

        q = []

        while len(q) != 5:
            p = randint(0,4)
            if p not in q:
                q.append(p)

        for i in q:
            if i == 0 and m[1][1] == ' ':                              #if center is free, go for it
                move = (1 , 1)
                m[move[0]][move[1]] = self.symbol
                return m
            elif i == 1 and m[0][0] == ' ':
                move = (0 , 0)
                m[move[0]][move[1]] = self.symbol
                return m
            elif i == 2 and m[0][2] == '':
                move = (0 , 2)
                m[move[0]][move[1]] = self.symbol
                return m
            elif i == 3 and m[2][0] == ' ':
                move = (2 , 0)
                m[move[0]][move[1]] = self.symbol
                return m
            elif i == 4 and m[2][2] == ' ':
                move = (2 , 2)
                m[move[0]][move[1]] = self.symbol
                return m

        for i in [0,1,2]:
            for j in [0,1,2]:
                if m[i][j] == ' ':
                    move = (i , j)
                    m[move[0]][move[1]] = self.symbol
                    return m


#======================== class menu ========================
class Menu():

    def __init__(self):
        self.state = 0
        pass

    def display(self):
        '''
        1 - single player, 2- multiplayer 3, quit
        '''
        logo =[
        '  |/////||/||///|   |/////|  /  |///|   |/////||////||///|  ',
        '    |/|  |/||/   ///  |/|   /_/ |/   ///  |/|  |/||/||//|   ',
        '    |/|  |/||///|     |/|  /   /|///|     |/|  |////||///|  ',
        '                                                  by JL     ',
        '                                                            ',
        '                                                            ']

        clr_scr()
        for line in logo:
            print(line)

        print('{0:^60}\n{1:^60}\n{2:^60}\n{3:^60}'.format('MENU:','1 - single player','2 - multi player','3 - quit')+'\n'*5)

        while self.state not in [1,2,3]:
            choice = input()
            if choice.isdigit():
                self.state = int(choice)
            else:
                continue

        pass

    def play_again(self):
        '''
        changes menu state to 0 if player doesn't want to play again
        '''
        wanna = ''
        while wanna not in ['y', 'Y', 'n', 'N']:
            wanna = input('Do you want play again (Y/N): ')


        if wanna in ['y' , 'Y']:
            pass
        else:
            self.state = 0
        return

#====================== class board ==========================
class Board():

    def __init__(self):
        self.m = []                             # [y,x] 3x3
        self.match_counter = 0
        self.first_turn = randint(0,1) == 1     # first turn randomisation
        self.turn = None                        # True - player_x / False - player_o
        self.winner = None                      # None
        pass

    def new_game(self):
        self.m = [[' ',' ',' '],                # [y,x]
                  [' ',' ',' '],
                  [' ',' ',' ']]
        self.first_turn = not self.first_turn   # make the other player begin
        self.turn = self.first_turn
        self.winner = None
        pass

    def next_turn(self):
        self.turn = not self.turn
        pass

    def check(self):
        '''
        check for winner / tie
        '''

        m_dep = []
        m_depx = []
        m_depy = []
        m_depd = []

        i = 2
        for x in [0,1,2]:
            m_dep.append(self.m[x][x])
            m_depd.append(self.m[i][x])
            i -= 1
            for y in [0,1,2]:
                m_depx.append(self.m[x][y])
                m_depy.append(self.m[y][x])
                pass


        m_dep += m_depd + m_depx + m_depy




        w = 0
        while w < len(m_dep)-2:
            if m_dep[w] == m_dep[w+1] == m_dep[w+2] != ' ':
                self.winner = m_dep[w]
            w += 3

        for i in range(0, len(m_dep)):                          # tie case check
            if m_dep[i] == ' ':
                break
        else:
            self.winner = 0

        pass

    def display(self, score1, score2): # stats1,2 - players scores
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
                if self.m[y][x] == 'O':
                    for i, line in enumerate(large_o):
                        matrix[9+(y*9)+i] = matrix[9+(y*9)+i][:(14+(16*x))] + line + matrix[10+(y*9)+i][26+(16*x):]
                elif self.m[y][x] == 'X':
                    for i, line in enumerate(large_x):
                        matrix[9+(y*9)+i] = matrix[9+(y*9)+i][:(14+(16*x))] + line + matrix[10+(y*9)+i][25+(16*x):]

        clr_scr()

        print(' '*12+'{0:^48}'.format(f'Match {self.match_counter}'))
        print('{0:>28} {1:>5} : {2:<5} {3:<28}\n'.format('Player X',score1, score2,'Player O'))
        for line in matrix:
            print(line)
        pass

        if self.winner == 0:
            print('\n'+' '*12+'{0:^48}'.format(f"Tie game!"))
        elif self.winner != None:
            print('\n'+' '*12+'{0:^48}'.format(f'Player {self.winner} has won!'))
        else:
            pass

        print('\n')

# ====================== THE GAME ============================
main_menu = Menu()

while main_menu.state != 3:

    if main_menu.state == 0:       # new game start
        main_menu.display()
        game = Board()
        game.new_game()
        game.match_counter += 1

        if main_menu.state == 1:    # single player
            player_x = HumanPlayer('X')
            player_o = AiPlayer('O')

        elif main_menu.state == 2:  # multiplayer
            player_x = HumanPlayer('X')
            player_o = HumanPlayer('O')

        elif main_menu.state == 3:  # quit game
            break

    game.display(player_x.score, player_o.score)

    if game.turn == True:           # player_x turn
        game.m = player_x.move(game.m)
    else:
        game.m = player_o.move(game.m)

    game.display(player_x.score, player_o.score)
    game.check()
    game.next_turn()

    if game.winner != None:
        if game.winner == 'X':
            player_x.score += 2
        elif game.winner == 'O':
            player_o.score += 2
        elif game.winner == 0:
            player_x.score += 1
            player_o.score += 1


        game.display(player_x.score, player_o.score)
        main_menu.play_again()
        game.new_game()
        game.match_counter += 1

clr_scr()
print('\nBye! \nTicTacToe by JL 2022')
