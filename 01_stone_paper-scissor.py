import random

def play_game(computer,you):
  if(computer==-1):
    if(you==1):
      print("You lose and computer won!!")
    elif(you==0):
      print("You won and computer lost")
  elif(computer==0):
    if(you==-1):
      print("You lose and Computer won")
    elif(you==1):
      print("You won and Computer lost")
  elif(computer==1):
    if(you==-1):
      print("You won and Computer lost")
    elif(you==0):
      print("You lose and Computer won")

computer=random.choice([-1,0,1])
your_choice=input("Enter your choice: ")
choices={"stone":-1,"paper":0,"scissor":1}
dict={-1:"Stone",0:"Paper",1:"Scissor"}
you=choices[your_choice]

print(f"You chose {dict[you]}\nComputer chose {dict[computer]}")

if(computer==you):
  print("It's draw")
else:
  play_game(computer,you)


  



