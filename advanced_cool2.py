import turtle
colors = ["red","blue","green","orange","purple","pink"]
trtl=turtle.Turtle()
screen=turtle.Screen()

screen.setup(620,620)
screen.bgcolor('black')
trtl.pensize(3)
trtl.speed(50)
n=-1
for times in range (5):
    x=0
    for angle in range(x,360,15):
        n=n+1
        if n==5:
            n=-1
        trtl.color(colors[n])
        trtl.seth(angle)
        trtl.circle(100)
        x+=100
trtl.penup()
trtl.setpos(150,-270)
trtl.pendown()
trtl.pencolor('olive')

trtl.ht()