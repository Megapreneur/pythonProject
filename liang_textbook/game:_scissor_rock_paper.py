# (Game: scissor, rock, paper) Write a program that plays the popular scissor-rock-
# paper game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
# wrap a rock.) The program randomly generates a number 0 , 1 , or 2 representing
# scissor, rock, and paper. The program prompts the user to enter a number 0 , 1 , or
# 2 and displays a message indicating whether the user or the computer wins, loses,
# or draws. Here are sample runs:
import random

print("Welcome to the game: 0 for Scissors, 1 for Rock and 2 for paper")
user_choice = int(input("Enter your coice from 0 to 2"))



computer_choice = random.randint(0, 3)

