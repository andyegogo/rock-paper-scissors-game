rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

while True:
  userchoice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  if userchoice == "0" or userchoice == "1" or userchoice == "2":
    if userchoice == "0":
      print("Your pick:\n", rock)
    elif userchoice == "1":
      print("Your pick:\n", paper)
    elif userchoice == "2":
      print("Your pick:\n", scissors)
    choices = ["0", "1", "2"]
    computers_choice = random.choice(choices)
    
    if computers_choice == "0":
      print("The computer picked:\n", rock)
    elif computers_choice == "1":
      print("The computer picked:\n", paper)
    elif computers_choice == "2":
      print("The computer picked:\n", scissors)
  
    combo = userchoice + computers_choice
    if combo in ["02", "21", "10"]:
      print("You are a R.P.S. Legend.")
      break
    elif combo in ["20", "12", "01"]:
      print("⚠️ Sorry Blood!!! You've been defeated.")
      break
    else:
      print("Ouch🤕!!! Its a draw.\nGo Again\n.\n.\n.\n.\n.\n")
  
  
  
  else:
    print("⚠️ stick to the range specified⚠️... Go Again!!!\n.\n.\n.\n.\n.\n")


