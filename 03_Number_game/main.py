import random
def game():
  score=random.randint(1,100)

  with open("Number_game/hi_score.txt") as f:
    hiscore=f.read()
    if(hiscore!=""):
      hiscore=int(hiscore)
    else:
      hiscore=0
    print(f"Your score is {score}")
    if(score>hiscore):
      with open("Number_game/hi_score.txt","w") as f:
        f.write(str(score))

    return score

game()