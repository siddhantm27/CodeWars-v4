import random
import math

name = "scriptblue"

def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    ne = pirate.investigate_ne()
    nw = pirate.investigate_nw()
    se = pirate.investigate_se()
    sw = pirate.investigate_sw()
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum

def moveAway(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return random.randint(1, 4)
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial="abc", clockwise=True):
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if initial != "abc":
            return moveTo(initial[0], initial[1], Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return moveAway(x, y, Pirate)
        else:
            return moveTo(x, y, Pirate)
    else:
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate,
        )
    
def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
   
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 , y == 0):
        return random.randint(1,4)
    
    if(sorted_dict[list(sorted_dict())[3]] == 0 ):
        return random.randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)
    
b=[[]]
i=0
reached=[0 for i in range(300)]

def checkIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    if (up[0:-1] == "island" or down[0:-1] == "island") and (left[0:-1] == "island" or right[0:-1] == "island"):
        if up[0:-1] == "island":
            return up
        if down[0:-1] == "island":
            return down
        if right[0:-1] == "island":
            return right
        if left[0:-1] == "island":
            return left 
    else:
        return False

def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1


def ActPirate(pirate):
    global i
    global b
    Choices=[1,2,3,4]
    b.append([])
    b[i]=[0.25,0.25,0.25,0.25]
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    x_start,y_start = pirate.getDeployPoint()
    if "myCaptured" not in s[0:3]:
        if x_start == 0 and y_start == 0:
            b[i][0]=0.15
            b[i][1]=0.35
            b[i][2]=0.35
            b[i][3]=0.15
        if x_start == 0 and y_start == 39:
            b[i][0]=0.35
            b[i][1]=0.35
            b[i][2]=0.15
            b[i][3]=0.15
        if x_start == 39 and y_start == 0:
            b[i][0]=0.15
            b[i][1]=0.15
            b[i][2]=0.35
            b[i][3]=0.35
        if x_start == 39 and y_start == 39:
            b[i][3]=0.35
            b[i][2]=0.15
            b[i][1]=0.15
            b[i][0]=0.35
        i+=1
    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 1)
        pirate.setSignal(s)

    if (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 1) + "," + str(y)
        pirate.setSignal(s)

    if (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 1)
        pirate.setSignal(s)

    if (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 1) + "," + str(y)
        pirate.setSignal(s)

    p = pirate.trackPlayers()

    if x_start == 0 and y_start == 0:
        if int(pirate.getID()) in [1,3,5,7,9,11,13]:
            n=int(pirate.getID())
            if pirate.getPosition() == (39,(n // 2)*3+1):
                reached[n]=10
            if reached[n] == 10:
                return moveTo(x_start,y_start,pirate)
            if pirate.getPosition() == (x_start,y_start):
                reached[n] == 0
            if reached[n] == 0:
                return moveTo(39,(n // 2)*3+1,pirate)
        elif int(pirate.getID()) in [2,4,6,8,10,12,14]:
            n=int(pirate.getID())
            if pirate.getPosition() == ((n // 2)*3-2,39):
                reached[n]=10
            if reached[n] == 10:
                return moveTo(x_start,y_start,pirate)
            if pirate.getPosition() == (x_start,y_start):
                reached[n] == 0
            if reached[n] == 0:
                return moveTo((n // 2)*3-2,39,pirate)
    if x_start == 0 and y_start == 39:
        if int(pirate.getID()) in [1,3,5,7,9,11,13]:
            n=int(pirate.getID())
            if pirate.getPosition() == ((n // 2)*3+1,0):
                reached[n]=10
            if reached[n] == 10:
                return moveTo(x_start,y_start,pirate)
            if pirate.getPosition() == (x_start,y_start):
                reached[n] == 0
            if reached[n] == 0:
                return moveTo((n // 2)*3+1,0,pirate)
        elif int(pirate.getID()) in [2,4,6,8,10,12,14]:
            n=int(pirate.getID())
            if pirate.getPosition() == (39,42-(n // 2)*3):
                reached[n]=10
            if reached[n] == 10:
                return moveTo(x_start,y_start,pirate)
            if pirate.getPosition() == (x_start,y_start):
                reached[n] == 0
            if reached[n] == 0:
                return moveTo(39,42-(n // 2)*3,pirate)
    if x_start == 39 and y_start == 0:
        if int(pirate.getID()) in [1,3,5,7,9,11,13]:
            n=int(pirate.getID())
            if pirate.getPosition() == (0,(n // 2)*3+1):
                reached[n]=10
            if reached[n] == 10:
                return moveTo(x_start,y_start,pirate)
            if pirate.getPosition() == (x_start, y_start):
                reached[n] == 0
            if reached[n] == 0:
                return moveTo(0,(n // 2)*3+1,pirate)
        elif int(pirate.getID()) in [2,4,6,8,10,12,14]:
            n=int(pirate.getID())
            if pirate.getPosition() == (42-(n // 2)*3,39):
                reached[n]=10
            if reached[n] == 10:
                return moveTo(x_start,y_start,pirate)
            if pirate.getPosition() == (x_start, y_start):
                reached[n] == 0
            if reached[n] == 0:
                return moveTo(42-(n // 2)*3,39,pirate)
    if x_start == 39 and y_start == 39:
        if int(pirate.getID()) in [1,3,5,7,9,11,13]:
            n=int(pirate.getID())
            if pirate.getPosition() == (0,38-(n // 2)*3):
                reached[n]=10
            if reached[n]==10:
                return moveTo(x_start,y_start,pirate)
            if pirate.getPosition() == (x_start, y_start):
                reached[n] == 0
            if reached[n] == 0:
                return moveTo(0,38-(n // 2)*3,pirate)
        elif int(pirate.getID()) in [2,4,6,8,10,12,14]:
            n=int(pirate.getID())
            if pirate.getPosition() == (42-(n // 2)*3,0):
                reached[n]=10
            if reached[n] == 10:
                return moveTo(x_start,y_start,pirate)
            if pirate.getPosition() == (x_start, y_start):
                reached[n] == 0
            if reached[n] == 0:
                return moveTo(42-(n // 2)*3,0,pirate)

    if checkIsland(pirate):
        # print(checkIsland(pirate))
        n=int(checkIsland(pirate)[-1])
        # print(n)
        # print(p)
        # print(p[n-1] == "myCaptured")
        # print(pirate.friend_present(pirate._Pirate__myTeam._Team__myGame._Game__island1,0) == False)
        if n==1:
            if pirate.friend_present(pirate._Pirate__myTeam._Team__myGame._Game__island1,0) == False and p[n-1] == "myCaptured":
                return 0
        if n==2:    
            if pirate.friend_present(pirate._Pirate__myTeam._Team__myGame._Game__island2,0) == False and p[n-1] == "myCaptured":
                return 0
        if n==3:
            if pirate.friend_present(pirate._Pirate__myTeam._Team__myGame._Game__island3,0) == False and p[n-1] == "myCaptured":
                return 0
            
    
    if pirate.getSignal() != "":
        s = pirate.getSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
        pirate.setSignal("")
    
        return moveTo(x, y, pirate)

    else:
        if "myCaptured" not in p[0:3]:
            random_number=random.choices(Choices, weights=b[0], k=1)[0]
            return random_number
        else:
            return random.randint(1,4)

def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)
    # print(team.getTeamSignal())
    # print(team.trackPlayers())
    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
