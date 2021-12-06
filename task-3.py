# Рандом и расширение списка.
# Заполните лист 10ю рандомными значениями в промежутке 1-100. (Испольуя метод randint модуля random)
# Пока длинна листа меньше 10ти добавляйте к листу элемент.
# Пройдитесь циклом и найдите минимальное и максимальное значение Не используя встроенные методы.
# Выведете минимальное и максимальное значение списка используя встроенные методы.
import random

my_list = []
while len(my_list) < 10:
    my_list.append(random.randint(1, 100))
print(my_list)


def max_in_list(any_list):
    i = 0
    for number in any_list:
        if number > i:
            i = number
    return i


def min_in_list(any_list):
    max = max_in_list(my_list)
    for min in any_list:
        if min < max:
            max = min
    return max


print("Max in list is: ", max(my_list))
print(max_in_list(my_list))
print("Min in list is: ", min(my_list))
print(min_in_list(my_list))
