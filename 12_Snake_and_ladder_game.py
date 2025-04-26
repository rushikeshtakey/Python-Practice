from random import randint

     
players_num=int(input("How many  players are playing:"))
i=1
ls=[]
while(i<=players_num):
    print("Enter name of player",i,":",end="")
    name=input()
    ls.append(name)
    i+=1
players={}
players=players.fromkeys(ls,0)

def ladder(score):
        if score==1:
            score=38
            print("You got Ladder!!!!")
        elif score==4:
            score=14
            print("You got Ladder!!!!")
        elif score==8:
            score=30
            print("You got Ladder!!!!")
        elif score==21:
            score=42
            print("You got Ladder!!!!")
        elif score==28:
            score=76
            print("You got Ladder!!!!")
        elif score==50:
            score=67
            print("You got Ladder!!!!")
        elif score==71:
            score=92
            print("You got Ladder!!!!")
        elif score==88:
            score=99
            print("You got Ladder!!!!")
        return score

def roll_dice(p,name):
        print(name,"press enter to roll the dice:")
        input()
        dice=randint(1,6)
        print(dice)
        p+=dice
        return p

def snake(score):
        if score==32:
            score=10
            print("You got the snake")
        elif score==36:
            score=6
            print("You got the snake")
        elif score==48:
            score=26
            print("You got the snake")
        elif score==62:
            score=18
            print("You got the snake")
        elif score==88:
            score=24
            print("You got the snake")
        elif score==95:
            score=56
            print("You got the snake")
        elif score==97:
            score=78
            print("You got the snake")

        return score

     
winner_ls=[]
who_won=0
while True:
    for player in players:
        if players[player]<100:
            oldscr=players[player]
            players[player]=roll_dice(players[player],player)
            players[player]=ladder(players[player])          
            players[player]=snake(players[player])

            if players[player]==100:
                winner_ls.append(player)
                print("You win")
                who_won=len(winner_ls)
            elif int(players[player])>100:
                players[player]=oldscr
            print("You are at:",players[player])
    if players_num==who_won:
        break


i=1
for player in winner_ls:
    if i==1:
        print(player,"is:",i,"st")
    elif i==2 or i==3:
        print(player,"is:",i,"ed")
    else:
        print(player,"is:",i,"th")
    i+=1