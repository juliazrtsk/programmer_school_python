# Углубляемся в тему условий и условного оператора if

# Считываем какое-нибудь число с помощью инпута
x = int(input())

# Вспоминаем, как пишется условный оператор

# if условие:
#     команды, которые выполняются, если ответ на условие "Да"
# else:
#     команды, которые выполняются, если ответ на условие "Нет"

# Например
if x > 10:
    print('Число больше 10')
else:
    print('Число меньше 10')

# Остановимся поподробнее на условиях
# Условие - это выражение, результатом которого является ответ на вопрос.
# Ответ может быть либо "Да", либо "Нет"

# Пример: x > 10 - здесь мы спрашиваем "число х больше 10?".
# В зависимости от значения переменной х ответ может быть "Да" или "Нет"

# Знак > - оператор сравнения.
# Вот все операторы сравнения, которые мы будем использовать
# > - больше
# < - меньше
# == - равно
# != - не равно
# >= - больше либо равно
# <= - меньше либо равно

# Напоминаю разницу между == и =
y = 5 # = это оператор присваивания
# С его помощью мы не сравниваем, не задаём вопрос, а записываем в переменную какое-то значение

y == 10 # == это оператор сравнения на равенство. После него переменная не меняет значение
# С его помощью мы спрашиваем, равно ли значение переменной тому, что стоит справа от оператора

# Оператор == сравнивает на равенство.
# А оператор != сравнивает на НЕравенство

# 6 == 6 ДА (шесть равно шести?)
# 6 == 10 НЕТ (шесть равно десяти?)

# 6 != 6 НЕТ (шесть не равно шести?)
# 6 != 10 ДА (шесть не равно десяти?)


# Теперь про операторы >= и <=
# Какой ответ будет при следующем сравнении?
# 5 > 5
# Ответ: нет, число 5 НЕ БОЛЬШЕ 5. Т.к. оно равно 5, не больше, не меньше.

# А теперь спросим по-другому: 5 >= 5
# Читаться это будет так: число пять больше ЛИБО равно числу пять?
# Теперь ответ будет ДА, т.к. в данном случае 5 равно 5.

# 4 >= 5 НЕТ
# 5 >= 5 ДА
# 10 >= 5 ДА

# Аналогично с оператором <= (меньше либо равно).
# 4 <= 5 ДА
# 5 <= 5 ДА
# 10 <= 5 НЕТ