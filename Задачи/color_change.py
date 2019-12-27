import turtle
colors=['red', 'yellow', 'blue', 'orange', 'green', 'purple']

t=turtle.Turtle()
turtle.bgcolor('black')
t.speed(100)

for x in range(270):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(60)