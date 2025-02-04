from random import *

p1point=0
p2point=0
while True :
    print("player 1 press d:")
    pl1=input()
    if (pl1=='d'):
        p1 = randint(1,6)
        print(p1)
        if (p1==6):
            p1point+=1
            pl1==0
            print("Player 1 second chance press d:")
            pl1=input()
            if pl1=='d':
                p1 = randint(1,6)
                print(p1)
                if p1==6:
                    p1point+=1
                    if p1point==2:
                        print("Player 1 win")
                        break
                else:
                    p1point=0
    
    print("player 2 press d:")
    pl2=input()
    if(pl2=='d'):
        p2 = randint(1,6)
        print(p2)
        if (p2==6):
            p2point+=1
            pl2==0
            print("Player 2 second chance press d:")
            pl1=input()
            if pl1=='d':
                p2 = randint(1,6)
                print(p2)
                if p2==6:
                    p2point+=1
                    if p2point==2:
                        print("Player 2 win")
                        break
                else:
                    p2point=0
