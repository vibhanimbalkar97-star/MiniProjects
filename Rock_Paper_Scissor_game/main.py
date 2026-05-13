"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally) use randome for this to get random value
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""
import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter user choice: Rock, Paper, Scissor =")
comp_choice = random.choice(item_list)

print(f"User Choice =  {user_choice} Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both choice same = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper covers the rock = Comp win")
    else:
        print("Rock smashes scissor = You win")

elif user_choice == "paper":
    if comp_choice == "Rock":
        print("paper covers rock = You win")
    else:
        print("Scissor cut paper =  ")