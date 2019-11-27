import turtle

turtle_color = input("Введите цвет для черепашки: ")
turtle_step = 50
turtle_angle = 90

t = turtle.Turtle()
if turtle_color == "yellow":
    t.color(turtle_color)

t.forward(turtle_step)
t.left(turtle_angle)
t.forward(turtle_step)
t.left(turtle_angle)
t.forward(turtle_step)
t.left(turtle_angle)
t.forward(turtle_step)
t.left(turtle_angle)


# Это пример того, как вы можете использовать переменные и условный оператор в ваших программах сейчас.
# Разберите его самостоятельно и задайте вопросы, если что-то непонятно