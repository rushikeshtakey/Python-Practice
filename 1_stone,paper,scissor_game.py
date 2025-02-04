
#Rules:
print("Select option:")
print("Enter-1 for stone")
print("Enter-2 for paper\nEnter-3 for scissor")

#Taking inputs: 
print("\nPlayer-1, select your option:")
p1= int(input())
print("Player-2, select your option:")
p2=int(input())

# if both player give same input
if p1==p2:
    print("Same input")
else:

    if p1==1 and p2==2:
        print("p1=stone and p2=paper,so p2 win")
    if p1==1 and p2==3:
        print("p1=stone and p2=scissor,so p1 win")
    if p1==2:
        if p2==1:
            print("p1 is paper and p2 is stone, so p1 win")
        else:
            print("p1 is paper and p2 is scissor, so p2 win")
    else:
        if p2==1:
            print("p1 is scissor and p2 is stone, so p2 win")
        if p2==2:
            print("p1 is scissor and p2 is paper, so p1 win")