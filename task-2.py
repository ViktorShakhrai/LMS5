# Преобразование типов и слайсы.
# Превратите полученную от пользователя строку в тапл. Выведите строку содержащую только буквы на четных позициях.
#
# exmpl = "Привіт"
# # ваш код
# # var1 = .....
# assert var1 == "Пиі"

user_tuple_word = tuple(input('Enter the word: '))
new_str = list.append(user_tuple_word[0::2])
print(new_str)
