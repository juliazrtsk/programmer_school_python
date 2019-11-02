import turtle

type = input("Какую фигуру хочешь нарисовать? ")

if type == "круг":
    radius = int(input("Введи радиус: "))
    t = turtle.Pen()
    t.circle(radius)
elif type == "квадрат":
    print("Ого")
elif type == "треугольник":
    print("Вау")
else:
    print("Я такую не знаю")