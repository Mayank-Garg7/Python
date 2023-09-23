import random
def  game(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "g":
            return True
        elif you == "w":
            return False
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp == "g":
        if you == "w":
            return True
        elif you == "s":
            return False
print("Computer's Turn : Snake(s), Water(w) and Gun(g)? ")
print("")
randno = random.randint(1,3)
if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
elif randno == 3:
    comp = "g"

you = input("Your's turn : Snake(s), Water(w) and Gun(g)? ")
a = game(comp,you)
print(f"You chose {you} ")
print(f"Computer chose {comp} ")
if a == None:
    print("This Game is tie...........")
elif a == True:
    print("Congrats!, You win this Game")
elif a == False:
    print("Ooops!, You lose the Game...")
