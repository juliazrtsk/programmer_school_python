# До этого момента мы писали только простые условия
# В них содержался только один оператор сравнения
# Однако, разные условия можно комбинировать между собой

# Для этого у нас есть две связки: or и and
# or переводится с английского как "или"
# and переводится с английского как "и"

# Именно с помощью этих слов мы сочетаем условия
# В случае, когда нам нужно, чтобы два условия выполнялись ОДНОВРЕМЕННО, мы используем И (and)

# Например, нужно проверить, что число положительное и чётное
number1 = 24
if number1 > 0 and number1 % 2 == 0:
    print('Число положительное и чётное')
# Условие, проверяющее, что число положительное: number > 0
# Условие, проверяющее, что число чётное: number % 2 == 0
# А т.к. условия должны быть выполнены ОБА в ОДНО ВРЕМЯ, связывем их словом and

# В случае, если нам нужно, чтобы выполнилось ХОТЯ БЫ ОДНО из двух условий, мы используем ИЛИ (or)
# Пример: нужно проверить, что число делится либо на 2, либо на 5
number2 = 8
if number2 % 2 == 0 or number2 % 5 == 0:
    print('Число делится на 2 или на 5')

# Теперь вспомним тип данных boolean
# Его значения можно представить в виде чисел
# True = 1
# False = 0
# А связки or и and можно представить в виде арифметических операций
# or = + сложение
# and = * умножение

# Получаем следующее:
# True and True = 1 * 1 = 1 = True
# True and False = 1 * 0 = 0 = False
# False and False = 0 * 0 = 0 = False

# True or True = 1 + 1 = 1 = True (тут просто запомните, что мы в алгебре логики не можем получить больше 1)
# True or False = 1 + 0 = 1 = True
# False or False = 0 + 0 = 0 = False

# Таким образом считаются результаты всех сравнений
# Разберём примеры:
# 1. number2 % 2 == 0 or number2 % 5 == 0
# Вычислим результат каждого маленького условия отдельно
# Зададим значение переменной: number2 = 8
# number2 % 2 == 0 --> 8 % 2 == 0 --> 0 == 0 --> True
# number2 % 5 == 0 --> 8 % 5 == 0 --> 3 == 0 --> False
# А теперь подставим результаты обратно в условие
# True or False
# Преобразовываем к числовому виду
# 1 + 0 = 1 = True
# То есть, для чила 8 наше большое условие ВЫПОЛНЯЕТСЯ, оно истинно.
# Посчитаете результат самостоятельно для чисел 10 и 15

# 2. number1 > 0 and number1 % 2 == 0
# Зададим значение переменной: number1 = 13
# number1 > 0 --> 13 > 0 --> True
# number1 % 2 == 0 --> 13 % 2 == 0 --> 1 == 0 --> False
# Получили: True and False
# Преобразовываем к числовому виду
# 1 * 0 = 0 = False
# Значит, это условие не выполняется для числа 13.
# Действительно, число 13 больше нуля, НО при этом не чётное.
# Подсчитайте резульат самостоятельно для чисел -4 и 68


# ОЧЕНЬ ВАЖНАЯ ДЕТАЛЬ
# Вспомните, как в математике вычисляются следующие выражения
# 10 * 3 + 4
# 10 * (3 + 4)
# У умножения приоритет всегда выше, оно выполняется в первую очередь
# Но это только если не стоят скобки. Они могут менять порядок выполнения действий

# С нашими условиями всё работает точно так же
# Давайте решим такую задачу.
# Если число отрицательное и делится на 3 или на 7, вывести на экран слово YES.
# Иначе вывести слово NO

# Пишем условия:
# n < 10
# n % 3 == 0
# n % 7 == 0
# Теперь соединяем их в одно
n = 14
if n < 10 and n % 3 == 0 or n % 7 == 0:
    print('YES')
else:
    print('NO')
# Если мы запустим этот код, то при n = 14 получим ответ YES
# Но это неверно. Читаем внимательно условие
# Вывести YES нужно в том случае, когда число отрицательное И ПРИ ЭТОМ делится на 3 или 7.
# Т.е. для всех чисел, которые больше нуля, мы должны получать ответ NO
# Но этого не происходит
# Всё дело как раз в том, что мы не расставили скобки
# В алгебре логики связка and ведёт себя как умножение, а связка or как сложение
# Поэтому, чтобы не нарушить логику решения, нам нужно поставить скобки
n = 14
if n < 10 and (n % 3 == 0 or n % 7 == 0):
    print('YES')
else:
    print('NO')
# Теперь в первую очередь программа выяснит, делится ли число n на 3 или 7.
# А после этого проверит, положительное это число или отрицательное
