from random import randrange

def initialize_board():
    return [[str(i+1) for i in range(j*3,(j+1)*3)] for j in range(3)]

def print_board(board):
    print("+-------+------+------+")
    for row in board:
        print(f"|   {row[0]}   |   {row[1]}  |   {row[2]}  |")
        print("|       |      |      |")
        print("+-------+------+------+")
        
def check_winner(board):
    #check row and columns for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
        
        
        #check diagonals for winner
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]
        
        #check for tie
        for row in board:
            if any(cell.isdigit() for cell in row):
                return None
        return 'Tie'
    
def make_move(board, position, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == str(position):
                board[row][col] = player
                return True
    return False

def computer_move(board):
    while True:
        position = randrange(1,10)
        if make_move(board,position,'X'):
            break
        
def play_game():
    board = initialize_board()
    print_board(board)
    
    #computers first move
    make_move(board,5,'X')
    
    while True:
        #user move
        while True:
            try:
                user_input = int(input("Enter your move: "))
                if 1<= user_input <=9 and make_move(board, user_input, 'O'):
                    break
                else:
                    print("invalid, try again")
            except ValueError:
                print("please enter valid num")
        
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("Its a tie")
            else:
                print(f"{winner} won!")
            break
        
        #computer move
        computer_move(board)
        print_board(board)
        winner = check_winner(board)

        if winner:
            if winner == 'Tie':
                print("Its a tie")
            else:
                print(f"{winner} won!")
            break

if __name__ == "__main__":
    play_game()