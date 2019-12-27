import turtle

t = turtle.Turtle()

figure = input("Какую фигуру нарисовать?: ")

if (figure == "квадрат"):
    step = int(input("Введите величину стороны квадрата: "))
    angle = 90
    t.forward(step)
    t.left(angle)
    t.forward(step)
    t.left(angle)
    t.forward(step)
    t.left(angle)
    t.forward(step)
    t.left(angle)
elif (figure == "треугольник"):
    step = int(input("Введите величину стороны треугольника: "))
    angle = 120
    t.forward(step)
    t.left(angle)
    t.forward(step)
    t.left(angle)
    t.forward(step)
    t.left(angle)
elif (figure == "круг"):
    radius = int(input("Введите радиус круга: "))
    t.circle(radius)
else:
    print("Я такой фигуры не знаю")
