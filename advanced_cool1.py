# Multiple Squares

import turtle,time,random

msquare=turtle.Turtle()
msquare.speed(100)

def Multiple_Squares(length, colour):
    msquare.pencolor(colour)
    msquare.pensize(4)
    msquare.forward(length)
    msquare.right(90)
    msquare.forward(length)
    msquare.right(90)
    msquare.forward(length)
    msquare.right(90)
    msquare.forward(length)
    msquare.right(90)
    msquare.setheading(360)
    msquare.ht()

for i in range(10,400,10):
    colors = ["red","blue","green","orange","purple","pink"]
    Multiple_Squares(i,random.choice(colors))

time.sleep(100)
