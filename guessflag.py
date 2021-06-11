import turtle
import random

bob = turtle.Turtle()

points = 0
life = 3

def lithuania():

    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.hideturtle()

def luxemburg():

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("light blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.hideturtle()

def netherlands():

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.hideturtle()

def estonia():

    bob.fillcolor("blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("black")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.hideturtle()

def bulgaria():

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.hideturtle()


flags = [lithuania, luxemburg, netherlands, estonia, bulgaria]

while life > 0 and len(flags) > 0:
    bob.reset()
    bob.speed(100)
    flag = random.choice(flags)
    flag()
    answer = input("Which country is this flag?")

    if answer == flag.__name__:
        print("Bravo!")
        points += 1
        print ("Your points:", points)
        print ("Your lives:", life)
        flags.remove(flag)

    else:
        print("Nope, try again!")
        if points > 0:
            points -= 1
        else:
            points = 0
        life -= 1
        print("Your points:", points)
        print ("Your lives:", life)
turtle.done()







