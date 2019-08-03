#Jason Jiang 7/14/19 #6
#goal: make a rand number generation and guessing game and learn basic random methods in class random
import sys
from random import randint
y = 0 
while y < 20:
    y+=1
    print(randint(1, 10))
while True:
    x = input("type -1 to start the game")
    print(x)
    if x == '-1':
        break
    else:
        continue


print('Lets Play')
print('Im going to pick a number from 1-10 and u have to guess it')
print('ready...go!!')

x = randint(1, 10)

while True:
    y = input('what is your guess')
    try:
        int(y)
    except:
        print('input must be a int')
        continue
    if int(y) > 0:
        y = int(y)
        if y < x:
            print("too low")
            continue

        elif y > x:
            print("too high")
            continue
        elif y == x:
            break

        else:
            print("algorithom broken, exiting program")
            sys.exit()
    else:
        print('input must be positive')
        continue
x = input('You did it!!! type -1 to exit')

while True:
    if x == "-1":
        sys.exit()
    else:
        continue
#what i learned:
#sys must be imported before using sys.exit
#the t in while True must be capitalized
#use try and except if there is possibility for error
#try will run the code untill it hits a error
#input is string so make sure when doing  == to put '' or "" for the value that u need after
#randint() starting and ending para are inclusive
