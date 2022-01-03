# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
import random

list1 = [random.randint(1, 10) for i in range(10)]
list2 = [random.randint(1, 10) for i in range(10)]
c = set(list2) & set(list1)
print(list2, list1)
print(c)
