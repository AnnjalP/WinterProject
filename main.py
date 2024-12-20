import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

def initiate(t2, x, y, colore):
    t2.penup()
    t2.goto(x,y)
    t2.fillcolor(colore)
    t2.setheading(0)
    t2.color(colore)

#snow pellets
initiate(t,-200,75,"white")
t.pensize(5)
for i in range(100):
    x = random.randrange(-1000,1000)
    y = random.randrange(-100,1000)
    t.penup()
    t.goto(x,y)
    t.dot()

#snow
initiate(t,-1000,-100,"white")
t.begin_fill()
for i in range(2):
    t.forward(2000)
    t.right(90)
    t.forward(900)
    t.right(90)
t.end_fill()


#tree stem
initiate(t,-25,0,"saddlebrown")
t.begin_fill()
for i in range(2):
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

#tree
initiate(t,-100,0,"darkolivegreen")
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()

initiate(t,-100,50,"darkolivegreen")
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()

initiate(t,-75,150,"darkolivegreen")
t.begin_fill()
for i in range(3):
    t.forward(150)
    t.left(120)
t.end_fill()

#triangle outline
# t.pensize(2)
# t.goto(-100,0)
# t.pendown()
# t.goto(100,0)
# t.goto(0,250)
# t.goto(-100,0)

#each square
# t.pencolor("blue")
# t.goto(-100,50)
# t.goto(100,50) #x
# t.goto(100,0)

# t.penup()
# t.goto(-75,50)
# t.pendown()
# t.goto(-75,100)
# t.goto(75,100) #x
# t.goto(75,50)

# t.penup()
# t.goto(-60,100)
# t.pendown()
# t.goto(-60,150) #x
# t.goto(60,150)
# t.goto(60,100)

# t.penup()
# t.goto(-45,150)
# t.pendown()
# t.goto(-45,200) #x
# t.goto(45,200)
# t.goto(45,150)

# t.penup()
# t.goto(-25,200)
# t.pendown() #x
# t.goto(-25,250)
# t.goto(25,250) #x
# t.goto(25,200)

colors = ("blue", "red", "purple", "orange", "pink", "yellow")
for i in range(10):
    y_cord = random.randrange(0,50)
    x_cord = random.randrange(-100,100)
    size = random.randrange(10,15)
    color = random.choice(colors)
    initiate(t, x_cord, y_cord, color)
    t.pensize(size)
    t.dot()

for i in range(5):
    y_cord = random.randrange(50,100)
    x_cord = random.randrange(-75,75)
    size = random.randrange(10,15)
    color = random.choice(colors)
    initiate(t, x_cord, y_cord, color)
    t.pensize(size)
    t.dot()

for i in range(5):
    y_cord = random.randrange(100,150)
    x_cord = random.randrange(-60,60)
    size = random.randrange(10,15)
    color = random.choice(colors)
    initiate(t, x_cord, y_cord, color)
    t.pensize(size)
    t.dot()

for i in range(5):
    y_cord = random.randrange(150,200)
    x_cord = random.randrange(-45,45)
    size = random.randrange(10,15)
    color = random.choice(colors)
    initiate(t, x_cord, y_cord, color)
    t.pensize(size)
    t.dot()

for i in range(2):
    y_cord = random.randrange(200,250)
    x_cord = random.randrange(-25,25)
    size = random.randrange(10,15)
    color = random.choice(colors)
    initiate(t, x_cord, y_cord, color)
    t.pensize(size)
    t.dot()

#snowman
initiate(t,-200,-100,"white")
t.begin_fill()
t.circle(50)
t.end_fill()

initiate(t,-200,-10,"white")
t.begin_fill()
t.circle(35)
t.end_fill()

initiate(t,-200,50,"white")
t.begin_fill()
t.circle(25)
t.end_fill()

#snow hat
initiate(t,-237.5,90,"darkgray")
t.begin_fill()
t.pendown()
t.pensize(1)
t.pencolor("white")
for i in range(2):
    t.forward(75)
    t.left(90)
    t.forward(10)
    t.left(90)
t.end_fill()

initiate(t,-225,100,"darkgray")
t.pendown()
t.pensize(1)
t.pencolor("white")
t.begin_fill()
for i in range(2):
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

#snowman eyes
initiate(t,-210,80,"black")
t.pensize(5)
t.dot()

initiate(t,-190,80,"black")
t.dot()

#snowman dots
shift = 0
for i in range(3):
    initiate(t,-200,50+shift,"black")
    t.pensize(6)
    t.dot()
    shift = shift-50

initiate(t,-200,75,"orange")
#attempted triangle
t.begin_fill()
t.goto(-200,60)
t.goto(-250,67.5)
t.goto(-200,75)
t.end_fill()

#pond
tilt = 0
initiate(t,-900,-400,"lightblue")
for i in range(50):
    t.goto(-900+tilt, -400)
    t.begin_fill()
    t.circle(125)
    t.end_fill()
    tilt = tilt +50


#present
initiate(t,200,-100,"red")
t.begin_fill()
for i in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

initiate(t,216.666,-100,"white")
t.begin_fill()
for i in range(2):
    t.forward(16.66666666)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()


initiate(t,216.66666,-50,"white")
t.pendown()
t.pencolor("white")
t.pensize(3)
t.circle(10)

initiate(t,233.3333333333,-50,"white")
t.pendown()
t.pencolor("white")
t.pensize(3)
t.circle(10)


shift_x = 0
shift_y = 70
#star
t.pensize(1)
initiate(t,-30,220,"gold1")
t.pencolor("goldenrod3")
t.penup()
t.begin_fill()
t.goto(-30+shift_x,220+shift_y)
t.pendown()
t.goto(30+shift_x,220+shift_y)
t.goto(-20+shift_x,190+shift_y)
t.goto(0+shift_x,240+shift_y)
t.goto(20+shift_x,190+shift_y)
t.goto(-30+shift_x,220+shift_y)
t.end_fill()

initiate(t,-30,220,"gold1")
t.pencolor("goldenrod3")
t.begin_fill()
t.goto(0+shift_x,202+shift_y)
t.pendown()
t.goto(-12.25806+shift_x,209.35484+shift_y)
t.goto(-8+shift_x,220+shift_y)
t.goto(8+shift_x,220+shift_y)
t.goto(12.25806+shift_x,209.35484+shift_y)
t.goto(0+shift_x,202+shift_y)
t.end_fill()

#moon
initiate(t,-500,220,"gray")
t.begin_fill()
t.circle(100)
t.end_fill()

initiate(t,0,400,"white")
t.write("Merry Christmas!", align = "center", font = ("Roboto", 20, "bold"))

enter = input("hi")
