# Вы все уже познакомились с тем, как работает input()
userAddress = input("Введите, пожалуйста, ваш адрес: ")
# С его помощью можно у пользователя просить какие-то значения
# До этого момента мы всегда просили ввести только строчные значения

# Но если вам нужно, чтобы пользователь ввёл число, есть способ это сделать
# Посмотрите внимательно на следующую строчку
step = int(input("Введите количество шагов: "))
# Тут есть уже привычная конструкция: создаём переменную step, вызываем команду input(). 

# Но к этой конструкции добавилось кое-что новое: int()
# 1. int() - это тоже команда (ещё это называется "функция").
# 2. Она нужна для того, чтобы строчки преобразовывать в числа.

# Вспоминайте урок про типы данных: чем отличаются значения "50" и 50?
# Ответ: "50" - строка, 50 - число. Со строкой мы не можем производить никаких арифметических операций,
# а число не может содержать никаких символов помимо цифр.
# Так вот, функция int() получает в качестве аргумента строку и делает её числом, если это возможно.

number = int("76")
# В этом примере мы передали в функцию строку "76". В переменной number теперь лежит число 76.

# Вернёмся к примеру с переменной step.
# Вы видите, что функции int() в качестве аргумента мы передали совсем не число, а другую функцию: input()
# Остановимся на этом моменте поподробнее.

# Функции могут возвращать значения.
# Что это значит?
# Функция получила (или не получила) какие-то аргументы, что-то сделала и после себя что-то оставила.
name = input("Введите имя:" )
# В этом примере функция input() вызвалась, отработала и ВЕРНУЛА значение, которое мы "поймали" и с помощью знака = сохранили в переменную name

# Это значение можно и не ловить
input("Введите что угодно: ")
# В этом примере мы возвращённое значение никуда не сохранили. Технически, так делать можно (но не всегда нужно :))

# Что происходит в конструкции int(input("Введите шаги: "))?
# Функция input() ВОЗВРАЩАЕТ то, что ввёл пользователь - строчку
# Но это значение ЛОВИТ не переменная, а другая функция - int()
# А вот уже функция int() ВОЗВРАЩАЕТ другое значение - число
# И это число ЛОВИТ переменная step


# Весь этот пример можно было расписать длиннее. Попробуем с новой переменной
length = input("Введите длину: ") 
# Просим пользователя ввести длину. input() вызывается, отрабатывает и возвращает то, что ввёл пользователь.
#Это значение (строчка!) сохраняется в переменную 

# Эту переменную передаём в функцию int().
number_length = int(length) 
# int() вызывается с аргументом length, отрабатывает и возращает полученное число. Это новое значение сохраняется в другую переменную.
# Происходит всё то же самое, но немного длиннее и с лишней переменной.
# Чтобы не плодить кучу переменных, пользуйтесь способом int(input())