import turtle,time
gordon = turtle.Pen()
gordon.shape("turtle")
gordon.speed(0)
for i in range(70):
    gordon.circle(i*3)
    gordon.left(10)
time.sleep(100)