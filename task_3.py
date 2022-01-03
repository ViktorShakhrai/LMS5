# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

# Вилучення чисел.
# Створіть список, який містить усі цілі числа від 1 до 100, потім знайдіть зі списку всі цілі числа,
# які діляться на 7, але не кратні 5, і збережіть їх в окремому списку. Нарешті, роздрукуйте список.
# Обмеження: використовуйте лише цикл while для ітерації
import random

needed_nums = []
numbers = []
i = 0
while i < 101:
    i += 1
    numbers.append(i)
while len(numbers) != 0:
    i = numbers.pop(0)
    if i % 7 == 0 and i % 5 != 0:
        needed_nums.append(i)
del numbers
print(needed_nums)
