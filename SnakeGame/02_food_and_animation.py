import turtle
# Импорт библиотеки для работы со случайными числами
import random
# Импорт библиотеки для работы со временем и задержками
import time

# Теперь константные значения мы пишем капсом - это общее правило для программистов
STEP = 20
DELAY = 0.1

win = turtle.Screen()
win.title("Игра Змейка")
win.setup(width=600, height=600)
win.bgcolor("pink")
# С помощью команды ниже мы отключаем любую внутреннюю анимацию библиотеки черепашки
# Благодаря этому мы всю анимацию можем настроить так, как именно нам нужно
# Это для того, чтобы не было никаких сюрпризов и неожиданного поведения змейки (как в случае, когда она долго ждала, пока подвинется еда)
win.tracer(0)

# Голова змеи
head = turtle.Turtle()

head.shape("square")
head.penup()
head.setx(0)
head.sety(0)
head.direction = "stop"

# Еда змеи
food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.penup()
# Ставим её в самом начале чуть выше змейки, чтобы они не пересеклись
food.setx(0)
food.sety(100)
# Измените код так, чтобы еда появлялась в случайном месте на поле


# Доделанная функция, которая изменяет положение змеи в пространстве
def move():
    if head.direction == "up":  
        y = head.ycor()
        head.sety(y + STEP)
    if head.direction == "down":  
        y = head.ycor()
        head.sety(y - STEP)
    if head.direction == "left":  
        x = head.xcor()
        head.setx(x - STEP)
    if head.direction == "right":  
        x = head.xcor()
        head.setx(x + STEP)

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

# Мы столкнулись с тем, что управление wasd не работает, если у вас включён CapsLock или русский язык
# Подумайте, что можно сделать, чтобы программа работала и в таких случаях
win.onkeypress(go_up, "Up")
win.onkeypress(go_up, "w")

win.onkeypress(go_down, "Down")
win.onkeypress(go_down, "s")

win.onkeypress(go_left, "Left")
win.onkeypress(go_left, "a")

win.onkeypress(go_right, "Right")
win.onkeypress(go_right, "d")
win.listen()


while True:
    win.update()
    
    # Здесь мы пользуемся встроенной в черепашку функцией, которая высчитывает расстояние
    # head.distance(food) возвращает число - расстояние от черепашки head до черепашки food
    # Если оно достаточно мало (<20), то мы считаем, что змея съела еду. Поэтому еда появляется в новом месте
    if head.distance(food) < 20:
        # Здесь мы высчитываем новые координаты еды
        # Функция randint библиотеки random принимает два аргумента
        # Вместе эти два числа обозначают числовой промежуток.
        # Новое число будет именно из этого промежутка, ни больше, ни меньше
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        # Наш экран размером 600 х 600. Поэтому минимальное значение y = -300, а максимальное = 300
        # Тоже самое с x. Мы берем промежуток немного меньше, чтобы еда не попадала совсем уж на края экрана
        # У этого кода есть одна проблема: если мы поменяем размеры окна, придётся вручную высчитывать и переписывать числа здесь
        # Как этого избежать?
        food.setx(x)
        food.sety(y)
    
    move()
    
    # Эта строчка делает небольшую задержку в выполнении программы
    # Благодаря этому змейка не перемещается мгновенно в край экрана
    # После каждого шага (1 итерация цикла while = 1 шаг) мы видим задержку
    # Поэтому змейка двигается прерывистыми шагами
    time.sleep(DELAY)
