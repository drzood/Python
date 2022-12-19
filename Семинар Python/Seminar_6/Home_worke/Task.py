# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, 
# enumerate, list comprehension(4 задачи из прошлых 
# семинаров переделать с использованием этих функций)

# 1.
# Примеры:
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('N = '))
# print([i for i in range(-abs(n), abs(n) + 1, 1)]) # list comprehension

# 2.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# n = int(input('Num = '))   # ввод  
# x = lambda x: 5 < x < 8    # lambda
# print(x(n))

