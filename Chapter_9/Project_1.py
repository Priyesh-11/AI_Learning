import random

possible_num = [-1, 0, 1]
computer = random.choice(possible_num)

choice = input("Enter our Choice s-> Stone, p-> Paper, c-> scissor : ")
yourchoice = { "s" :-1, "p" : 0, "c" : 1 }

you = yourchoice[choice]

if computer == you :
    print("draw", + computer)

elif computer==-1 and you==0:
    print("u won", + computer) 

elif computer==-1 and you==1:
    print("compuert won", + computer)

elif computer==0 and you==-1:
    print("compuert won", + computer)

elif computer==0 and you==1:
    print("u won", + computer)

elif computer==1 and you==-1:
    print("u won", + computer)

elif computer==1 and you==0:
    print("u won", + computer)

else:
    print(f"Invalid Input : {you}")

