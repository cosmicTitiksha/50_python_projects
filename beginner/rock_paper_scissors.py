# This program demonstrates playing Rock, Paper, Scissors with the computer
import random


scores = 0
count = 0
query = True
while query:
  computer = random.choice(['rock', 'paper', 'scissors'])
  player = input("Enter your choice (Rock/Paper/Scissors/exit): ").lower()
  
  if player == 'exit':
    query = False

  else:
    count += 1
    if computer == player:
      output = "It's a tie!"
    elif computer == 'rock':
      if player == 'paper':
        output = "You won!"
        scores += 1
      elif player == 'scissors':
        output = "You lost!"
      else:
        output = "Invalid Entry..Try again"
    elif computer == 'paper':
      if player == 'rock':
        output = 'You lost!'
      elif player == 'scissors':
        output = "You won!"
        scores += 1
      else:
        output = "Invalid Entry..Try again"
    elif computer == 'scissors':
      if player == 'rock':
        output = 'You won!'
        scores += 1
      elif player == "paper":
        output = 'You lost!'
      else:
        output = "Invalid Entry..Try again"
    
    print(f"You entered {player}, computer entered {computer}, {output}")

print(f"{scores}/{count}")