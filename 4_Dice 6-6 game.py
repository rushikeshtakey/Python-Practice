from random import *

p1point=0
p2point=0
while True :
    pl1=input()
    print("player 1 press Enter to roll the dice:",pl1,end=" ")
    if (pl1==''):
        p1 = randint(1,6)
        print(p1)
        if (p1==6):
            p1point+=1
            pl1==0
            pl1=input()
            print("Player 1 second chance press  Enter to roll the dice:",pl1,end=" ")
            if pl1=='':
                p1 = randint(1,6)
                print(p1)
                if p1==6:
                    p1point+=1
                    if p1point==2:
                        print("Player 1 win")
                        break
                else:
                    p1point=0
    
    pl2=input()
    print("player 2 press Enter to roll the dice:",pl2,end=' ')
    if(pl2==''):
        p2 = randint(1,6)
        print(p2)
        if (p2==6):
            p2point+=1
            pl2==0
            pl2=input()
            print("Player 2 second chance press Enter to roll the dice:",pl2,end=' ')
            if pl2=='':
                p2 = randint(1,6)
                print(p2)
                if p2==6:
                    p2point+=1
                    if p2point==2:
                        print("Player 2 win")
                        break
                else:
                    p2point=0
