# Функция - это код, который мы можем вызывать в другом коде

# Как создать функцию
def function_name():
    print('Функция вызвалась')
    print('Функция выполняется')
    print('Функция завершена')

# def - ключевое слово (от англ. definition - определение)
# С его помощью сообщаем программе, что дальше мы создаём функцию

# function_name - имя функции. Придумываете сами в зависимости от того, что функция делает
# Лучше использовать в названии глаголы, т.к. функция = действие
# Например, функцию для сложения чисел можно назвать sum
# А функцию, которая выводит на экран имя пользователя, можно назвать sayHello

# Вспоминаем, что программа выполняется сверху вниз, по порядку каждое действие
# Так вот, когда вы определяете функцию, она НЕ отрабатывает. Вы просто сообщаете, что теперь с каким-то именем (function_name) будут вызываться какие-то действия

# Функция не выполнится до дех пор, пока вы явно не вызовете её


# Чтобы вызывать функцию, нужно написать её имя и добавить две скобки
function_name()
# Две скобки () - это ВСЕГДА показатель того, что вызывается какое-то действие

# Запустите этот файл и посмотрите, что получится