import random as rn

com=rn.randint(1,100)
p= int(input("Guess the number from 1 to 100:"))
guess=1

while(com!=p):
    if p<1 or p>100:
        p=int(input("Guess from 1 to 100: "))
        guess+=1
    elif p>com :
        p=int(input("Guess is larger: "))
        guess+=1
    else:
        p= int(input("Guess is smaller: "))
        guess+=1
       

print("Number of guesses :",guess)
    