from random import *

i=1;player=0;CPU=0;draw=0
while i<=5:
    c = randint(1,3)
    print("Enter 1,2,or 3 for stone,paper,scissor respectively.")
    p= int(input())
    if (p==1 and c==3) or (p==2 and c==1) or (p==3 and c==2):
        print("Player:",p,"CPU:",c,"so,Player wins")
        player +=1
    elif (p==1 and c==2) or (p==2 and c==3) or (p==3 and c==1):
        print("Player:",p,"CPU:",c,"so,CPU wins")
        CPU+=1
    elif p==c :
        print ("Player:",p,"CPU:",c,"so,Draw")
        draw+=1
    else :
        print("player's invalid input")
    i+=1


if player>CPU:
    print("\n\nPlayer points:",player,"\nCPU points:",CPU,"\nNo. of draws:",draw,"\nso, Player wins")
elif CPU>player:
    print("\n\nPlayer points:",player,"\nCPU points:",CPU,"\nNo. of draws:",draw,"\nso, CPU wins")
else :
    print("\n\nPlayer points:",player,"\nCPU points:",CPU,"\nNo. of draws:",draw,"\nso, Draw")
