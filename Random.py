
import random

def random_walk(n):

    x, y = 0, 0

    for i in range(n):

        (dx,dy)= random.choice([(0,1),(0,-1),(1,0),(-1,0)])

        x += dx
        y += dy

    return (x,y)

for i in range(25):

    walk=random_walk(20)

    print(walk,"Distance from home = ",
          abs(walk[0])+abs(walk[1]))
newinput = input("Please enter an integer :  ")

if len(newinput) < 6:
    print("Your string is too short ")

    print( "Please enter a string with least 6 characters.")

else:
    print('You are the bitch!')




