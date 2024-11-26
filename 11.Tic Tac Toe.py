def print_board(board):
    for row in board:
        print("|".join(row))
        print("_ "*3)
def winner(board,player):
    for row in board:
        if(all(cell==player for cell in row)):
            return True
    for col in range(3):
        if(all(board[row][col]==player for row in range(3))):
            return True
    return False
def is_draw(board):
    return all(cell!=" " for row in board for cell in row)
def tic_tac_toe():
    players=['O','X']
    board=[[" " for i in range(3)] for j in range(3)]
    turn=0
    print_board(board)
    while True:
        player=players[turn%2]
        print(player,"Turn")
        row,col=map(int,input("Enter the row and column to place:").split())
        print()
        if row>3 or col>3 or board[row-1][col-1]!=" ":
            print("Invalid Selection");
            continue
        board[row-1][col-1]=player
        print_board(board)
        print()
        if(winner(board,player)):
            print(f"{player} Wins")
            break
        if(is_draw(board)):
            print("Game Draw")
            break
        turn+=1
tic_tac_toe()
