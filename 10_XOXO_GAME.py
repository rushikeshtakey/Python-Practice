board = [1,2,3,4,5,6,7,8,9]

def show_board():
    i = 0
    while i<=8:
        print(board[i], end="  ")
        i = i + 1
        if i%3==0:
            print()

def check_winner():

    if (board[0]==board[4]) and (board[0]==board[8]):#left to right diagonal check
         return board[0]
    elif(board[2]==board[4]) and (board[2]==board[6]):#right to left diagonal check
        return board[2]
    else:
        b=0
        for a in range(0,3):
            
            if (board[b]==board[b+1]) and (board[b]==board[b+2]):#horizontal check
                return board[b]
            elif(board[a]==board[a+3]) and (board[a]==board[a+6]):#vertical check
                return board[a]
            b+=3




print("Player-1 = X\n Player-2 = O")
player = 1
turn = 1
while True:
    show_board()#to print board
    if turn==10:#to end the game
        print("Game over")
        break
    print("Player", player, "Enter your box number")
    box_num = int(input())-1

    if box_num<1 and box_num>9:#to handel exception
        print("Enter number from 1 to 9")
        continue
    elif board[box_num]=="X" or board[box_num]=="O":
        print("Already occupide")
        continue
    
    if player==1:#to print X and O in board and to check winner
        board[box_num]="X"
    else:
        board[box_num]="O"
        player=0
    winr=check_winner()
    if winr!=None:
        show_board()
        print("winner is player:",player)
        break
    player+=1
    turn = turn + 1