import random

print('Welcome to Tic Tac Toe!\n')


players = ['Player 1','Player 2']
board = [" "] * 10

def clear_output():
    print("\n"*100)

def display_board(board):
    print(" " + board[7] + "|" + board[8] + "|" + board[9])
    print("-------")
    print(" " + board[4] + "|" + board[5] + "|" + board[6])
    print("-------")
    print(" " + board[1] + "|" + board[2] + "|" + board[3])
    print("\n")


def player_input():
    marker  = ''
    while marker not in ["X","O"]: # marker != 'X' and marker != "O"
        marker = input("Player 1, choose X or O: \n").upper()
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return (player1,player2)


def choose_first():
    return players[random.randint(0,1)]


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,mark):
    # tmp = []
    # for i in range(1,len(board)):
    #     # check rows (1,2,3) (4,5,6)
    #     return mark * 3 in "".join(board)
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal



def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    emptys = list(filter(lambda item: item == " ", board))[1:]
    return not len(emptys) > 0


def player_choice(board,player):
    inp_pos = 0

    while not inp_pos in range(1,10) or not space_check(board,inp_pos):
        try:
            inp_pos = int(input(f"{player}, Choose your next position: (1-9) \n"))
        except ValueError:
            print(f"{player}, please input a number between 1-9 \n")
            continue

    return inp_pos


def replay():
    global board
    board = [" "] * 10
    choice = input("Do you want to play again? Enter Yes or No \n")
    return choice.lower() == "yes"

#
# def full_board_check(board):
#     emptys = list(filter(lambda item: item == " ", board))
#     return not len(emptys) > 0



while True:
    player1_mark, player2_mark = player_input()
    turn = choose_first()
    print(turn + " goes first \n")

    ready = input("Ready to play? y or n? \n").lower()

    if ready == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == players[0]:
            # display the board
            display_board(board)
            position = player_choice(board,turn)
            place_marker(board,player1_mark,position)

            if win_check(board,player1_mark):
                display_board(board)
                print(players[0] + " HAS WON!\n")
                game_on = False

            # if no win, check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!\n")
                    game_on = False

                # if no win and it's no tie, then game is on and it is Player 2's turn
                else:
                   turn = players[1]
        else:
            # display the board
            display_board(board)
            position = player_choice(board,turn)
            place_marker(board, player2_mark, position)

            if win_check(board, player2_mark):
                display_board(board)
                print(players[1] + " HAS WON!\n")
                game_on = False

            # if no win, check if there is a tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!\n")
                    game_on = False

                # if no win and it's no tie, then game is on and it is Player 2's turn
                else:
                    turn = players[0]

    if not replay():
        break


