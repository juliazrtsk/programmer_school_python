# Теперь важная деталь о счётчике цикла.
# Он нужен не просто так, мы можем к нему обращаться и использовать внутри команд.
# Всё как с обычными переменными, за исключением того, что лучше не менять значение у счётчика.
# За нас это автоматически сделает цикл

for i in range(1, 11):
    print(i)

# Это программа, которая выводит на экран все значения, которые принимает переменная i на каждом шаге цикла.

print('-----------') # Это просто вывод на экран разделител, чтобы при запуске программы было лучше видно, где какой цикл что вывел

# С переменной i можно взаимодействовать как с обычным числом: прибавлять её к чему-нибудь, умножать или делить на неё и т.д.
for i in range (1, 11):
    number = 5 * i
    print(number)
# Цикл сверху вывел на экран таблицу умножения на 5
# Мы завели переменную, в которой храним результат умножения числа 5 на значение переменной i
# i принимает значения от 1 до 10
# На каждой итерации меняется i, а значит меняется и number

print('-----------') 

for i in range(1, 11):
    square = i * i
    print(square)
# А это решение задачки с занятия: вывести с помощью цикла на экран квадраты числа i
# Квадрат числа = это результат умножения числа на само себя, если не помните

print('-----------') 

# Теперь давайте попробуем найти сумму всех чисел от 10 до 100
sum = 0 # Переменную, где будет хранится сумма, заводим вне цикла
for i in range (10, 101): # Да, начинать промежуток можно не только с 1
    sum = sum + i   # Здесь мы берём текущее значение переменной sum, прибавляем к нему значение i
    # А потом сохраняем полученное число снова в sum. То есть, перезаписываем переменную
print(sum) # Значение суммы выводим один раз - после цикла (обратите внимание на отступы)



# А это просто очень красивый пример того, как циклы можно использовать с черепашкой
# Запустите, посмотрите, что получилось. Разберите пример самостоятельно
import turtle
t = turtle.Turtle()

for i in range (1, 300):
    t.forward(i)
    t.left(59)
