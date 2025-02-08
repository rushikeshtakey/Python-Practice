import random as rand

end=int(input ("Enter the sum to reach: "))
p1scor=0
p2scor=0
plr=1

while (p1scor!=end) and (p2scor!=end):
    print("Player",plr,"Press enter to roll the dice:")
    input()
    dice=rand.randint(1,6)
    if(plr==1):
        p1scor+=dice
    else:
        p2scor+=dice

    if p1scor>end:
        p1scor-=dice
    elif p2scor>end:
        p2scor-=dice

    if (plr==1):
        print("Player",plr,"dice number",dice,"total score:",p1scor)
        plr+=1
    else:
        print("Player",plr,"dice number",dice,"total score:",p2scor)
        plr=1

print("Player",plr,"lost")