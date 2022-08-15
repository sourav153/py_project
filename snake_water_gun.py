from operator import truediv
import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
print("comp turn : Snake(s)water(w) or gun(g)?")
randno=random.randint(1,3)
print("comp choosed")
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

you=input("your turn: Snake(s)water(w) or gun(g)?")
a=gamewin(comp,you)
print(f"comp chose {comp}")
print(f"you chose {you}")
if a==None:
    print("tie")
elif a==True:
    print("you win")
else:
    print("you lose")