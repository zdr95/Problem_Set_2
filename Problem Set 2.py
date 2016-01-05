import random
x = random.randint(0, 100)
y= input("Choose a number between 0 and 100: ")
if y<x:
    print("Too Low")
if y>x:
    print("Too High")
if y==x:
    print("You got the number right")
while y!=x:
    y= input("Choose another number between 0 and 100: ")
    if y<x:
        print("Too Low")
    if y>x:
        print("Too High")
    if y==x:
        print("You got the number right")