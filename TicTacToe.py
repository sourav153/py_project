def sum(a,b,c):
    return(a+b+c)
def printBoard(xstate,zstate):
    zero='X' if xstate[0] else('O'if zstate[0] else 0)
    one='X' if xstate[1] else('O'if zstate[1] else 1)
    two='X' if xstate[2] else('O'if zstate[2] else 2)
    three='X' if xstate[3] else('O'if zstate[3] else 3)
    four='X' if xstate[4] else('O'if zstate[4] else 4)
    five='X' if xstate[5] else('O'if zstate[5] else 5)
    six='X' if xstate[6] else('O'if zstate[6] else 6)
    seven='X' if xstate[7] else('O'if zstate[7] else 7)
    eight='X' if xstate[8] else('O'if zstate[8] else 8)
    print(f"{zero}|{one}|{two}")
    print(f"-|-|-")
    print(f"{three}|{four}|{five}")
    print(f"-|-|-")
    print(f"{six}|{seven}|{eight}")

def wincheck(xstate,zstate):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win:
        if(sum(xstate[i[0]],xstate[i[1]],xstate[i[2]])==3):
            print("X won the match")
            return 1
        if(sum(zstate[i[0]],zstate[i[1]],zstate[i[2]])==3):
            print("O won the match")
            return 0
    return -1

xstate=[0,0,0,0,0,0,0,0,0]
zstate=[0,0,0,0,0,0,0,0,0]
turn=1 #1 for X & 0 for O
print("welcome to tictactoe")
while(True):
    printBoard(xstate,zstate)
    if(turn==1):
        print("X's chance")
        val=int(input("enter a value: "))
        xstate[val]=1
    else:
        print("O's chance")
        val=int(input("enter a value: "))
        zstate[val]=1
    winner=wincheck(xstate,zstate)
    if(winner!=-1):
        print("match over\nThanx for playing\n")
        break
    turn=1-turn
