import random
#  Rock, paper and scissor GAME
def gameWin(comp,you):
    if comp == you:
        return None
    # check all possibilities for r
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    # check all possibilities for p
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    # check all possibilities for s
    elif comp == 's':
        if you == 'r':
            return False
        elif you == 'p':
            return True
        
print("comp turn's:Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "s"
       
you = input("Rock(r) Paper(p) scissor(s)?")
a = gameWin(comp,you)
print(f'Comp choose {comp}')
print(f'you choose {you}')
if a == None:
    print("Game is tie")
elif a == False:
    print("you lose")
else:
    print("you Win")