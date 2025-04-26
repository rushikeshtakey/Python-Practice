import random

def show_list(x):
    for ch in x:
        print(ch, end=" ")

words = ["powerful", "success", "virtual", "demonstration",
         "university", "overflow", "microwave"]
word = random.choice(words)
list1 = ["_"] * len(word)
guess = 1
while guess<=6:
    if guess==6:
        show_list(list1)
        print("\nlast chance press # to guess the word:")
    else:
        print("Guess the word, you have",7-guess,"guess remaining")
        show_list(list1)
        print("\nEnter letter or press # if you got the word")
    letter = input()
    if letter == "#":
        print("Enter the word")
        ans = input()
        if ans == word:
            print("Correct Guess....")
            break
        elif guess==6 and ans!=word:
            print("GAME OVER!!!!")
            print("Correct word was:",word)
        else:
            print("Wrong Guess..")
    else:
        i=0
        if letter in word :
            for a in word:
                if a==letter:
                    list1[i]=a
                i+=1


    guess = guess + 1

