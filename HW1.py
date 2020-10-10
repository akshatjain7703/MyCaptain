import random

print("ROCK PAPER SCISSORS")
choices = ['r','p','s']
computer_wins = "The Computer Wins. Better Luck Next Time."
user_wins = "Woahhh, You Win."
draw = "Game Draw."

n='y'
while n=='y':
  user= input("\nEnter R for Rock, P for Paper, S for Scissors: ").casefold()
  if user != choices[0] and user != choices[1] and user != choices[2]:
    print("PLEASE Enter a valid choice")
    continue
  computer = random.choice(choices)
  print("USER: ",user)
  print("Computer: ",computer)

  if user == 'r':
    if computer == 's':
      print(user_wins)
    elif computer == 'p':
      print(computer_wins)
    else:
      print(draw)

  elif user == 's':
    if computer == 'p':
      print(user_wins)
    elif computer == 'r':
      print(computer_wins)
    else:
      print(draw)

  elif user == 'p':
    if computer == 'r':
      print(user_wins)
    elif computer == 's':
      print(computer_wins)
    else:
      print(draw)
  
  n = input("\nEnter Y to play again: ").casefold()


print("Come back soon!")

  
      
