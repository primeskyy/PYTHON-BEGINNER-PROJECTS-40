import random as r
n = str(input("PLEASE ENTER YOUR NAME : "))
print(f"\n==== WELCOME {n} TO ROCK-PAPER-SCISSIOR GAME ====\n RULES : ENTER THE NUMBER IN FRONT OF CHOICES \n")
print("CHOICES :- \nRock - [1] \nPaper - [2] \nScissor - [3]\n")
c = r.choice(['1','2','3'])
p = str(input("ENTER YOUR INPUT HERE : "))
inputs = [p,c]
prob = [['1','1'],['1','2'],['1','3'],['2','1'],['2','2'],['2','3'],['3','1'],['3','2'],['3','3']]
if prob.index(inputs) in [2,3,7]:
    print("YOU WON ! HERE IS WHAT YOU AND I CHOSEN\n")

    if prob.index(inputs) in [2]:
        print("YOUR CHOICE - ROCK  \n MY CHOICE - SCISSOR")
    elif prob.index(inputs) in [3]:
        print("YOUR CHOICE - PAPER  \n MY CHOICE - ROCK")
    elif prob.index(inputs) in [7]:
        print("YOUR CHOICE - SCISSOR  \n MY CHOICE - PAPER")

elif prob.index(inputs) in [1,5,6]:
    print("YOU LOOSE ! HERE IS WHAT YOU AND I CHOSEN\n")

    if prob.index(inputs) in [1]:
        print("YOUR CHOICE - ROCK  \n MY CHOICE - PAPER")
    elif prob.index(inputs) in [5]:
        print("YOUR CHOICE - PAPER  \n MY CHOICE - SCISSOR ")
    elif prob.index(inputs) in [6]:
        print("YOUR CHOICE - SCISSOR  \n MY CHOICE - ROCK ")
elif prob.index(inputs) in [0,4,8]:
    print("THIS IS A TIE ! AS YOU HAVE ENTERED THE SAME CHOICE AS ME.\n")
    print(f"YOUR CHOICE - {p} \n MY CHOICE - {p}")

print(f"\n\n THANKS {n} FOR PLAYING ! ")
