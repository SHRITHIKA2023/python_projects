# Snake water game with simple if ,elif and else conditions

players_choice = input("Enter what move you want to play: ")
print(f"Players choice is {players_choice}")

import random

computer_choice = random.choice(["snake", "water", "gun"])
print(computer_choice)

if players_choice == computer_choice:
  print("It's a tie!")
elif players_choice == "snake" and computer_choice == "water":
  print("You win!")
elif players_choice == "water" and computer_choice == "gun":
  print("You win!")
elif players_choice == "gun" and computer_choice == "snake":
  print("You win!")
elif computer_choice == "snake" and players_choice == "water":
  print("Computer_wins")
elif computer_choice == "water" and players_choice == "gun":
  print("Computers_wins")
elif computer_choice == "gun" and players_choice == "snake":
  print("Computers_wins")
else:
  print("Try again!!")
