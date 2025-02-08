from random import *

n=int(input("Enter number of players: "))
plyr=1
while True :
    print("player",plyr,"press enter to roll",end=" ")
    input()
    dice = randint(1,6)
    print(dice)
    if dice==6:
        print ("Player",plyr,"got second chance,press enter to roll again:",input(),end=" ")
        dice=randint(1,6)
        print(dice)
        if dice==6:
            print("Player",plyr,"WIN!!!!!!!")
            break
    plyr+=1
    if(plyr>n):
        plyr=1
