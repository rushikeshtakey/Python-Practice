from random import *

ans=str(randint(1000,9999))
while True:#this while loop to generate 4 degit number with all degits being different
    i=0
    for a in range(0,4):
        j=0
        for a in range(0,4):
            if ((ans[i]==ans[j]) and (i!=j)):
                ans=str(randint(1000,9999))
                i=0;j=0
                continue
            j+=1
        i+=1
    if i==4 and j==4 :
        break
print("Generated random 4 degit number with each degit being different:")


while True:
    print("Guess a 4 degit number:")
    ug=str(input())
    i=0
    cow=0
    bull=0
    for a in range(0,4):
        j=0
        for a in range(0,4):
            if(ans[i]==ug[j]):
                cow+=1
                if i==j:
                    cow-=1
                    bull+=1
            j+=1
        i+=1
    if bull==4:
        break
    print("Correct degits but at wrong place:",cow)
    print("correct degits and at right place:",bull)

print("correct guess:",ug)