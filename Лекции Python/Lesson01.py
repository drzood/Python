# int - целое число
# float - вещественное число, дроби

# type - показывает тип данных

# # value = None # Пустая переменная
# a = 123
# b = 1.23
# # print(type(a)) #Показывает тип данных переменной
# # print(b)
# value = 12334
# # print(value)
# s = 'hello \nworld' # апостроф \
# print(s)
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s)) # В фигурных можно вводить индекс перемменной из обычных скобок 0,1,2
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}') # Интерполяция

# f = True # или Fals
# print(f)

# list = [] # список, массив 
# print(list)

# print('Введите а')
# a = input()
# print('Введите 2')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите а')
# a = input()
# print('Введите 2')
# b = input()
# print(a, '+', b, '=', a+b) # 10 + 20 = 1020

# print('Введите а')
# a = int(input())
# print('Введите 2')
# b = int(input())
# print(a, '+', b, '=', a+b) # 10 + 20 = 30

# print('Введите а')
# a = float(input())
# print('Введите 2')
# b = float(input())
# print(a, '+', b, '=', a+b) # 1.2 + 2.3 = 3.5


# Арифмметичесие операции
# +, -, *, /, %, //, **
# **, плюс в кружкке, минус в кружке, *, /, //, %, +, -
# (), Сокращенные операции
# a = +123 # унарный плюс, положительное число, может не использоваться
# b = -321 # отрицателное число
# c = a + b
# c = a / b # 2 / 8 = 1.5
# c = a // b # 2 // 8 = 1 - целочиссленное деление
# c = a % b # 12 % 8 = 4
# c = a ** b # возведение в сетпень 2**8 = 2 в 8 степени
# c = a * b # 1,3 * 3 = 3,9000004
# c = round(a * b, 3) # 1,3 * 3 = 3.9 (тройка в скобках означает необходимое кол-во символов на выводе)

# a = 3 #
# a = a + 5 #или а += 5 сокращенная операция

# print(c)



# Логические операции

# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^

# is, is not, in, not in

# a = 1 > 4 # fals
# a = 1 < 4 # true
# a = 1 < 4 and 5 > 2 # true
# a = 1 == 2 # fals
# a = 1 != 2 # true

# a = 1 < 3 < 5 < 10 # true
# a = 1 > 2 or 4 < 6 # true

# a = 'ads'
# b = 'ads'
# print(a == b) # true

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b) # true

# a = [1,2,3,4]
# print(2 in f) # Проверит наличие числа 2 и выведет true
# print(not 2 in f) # проверит отсутствие 2 и выведет fals

# is_odd = f[0] % 2 == 0 
# # или так is_odd = not f[0] % 2 # false
# print(is_odd)


# Управляющие конструкторы: if, if-else, elif(иначе если тоже что и else if)
# while, while else, for

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# while a < b:
#     print(a)
# else:
#     print(b)

# for i in 1,2,3,4:
#     print(i**2)

# r = range(10) # от 0 до 9
# # r = range(1, 5) # от 1 до 4
# # r = range(1, 10, 2) # от 1 до 9 по 2 = 1, 3, 5, 7, 9
# for i in r:
#     print(i)

# for i in 'qwer':
#     print(i) # в столбик q w e r


# Строки

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True 
# print(text.isdigit()) # False строки из чисел?
# print(text.islower()) # True строки нижнего регистра?
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#   print(c)


# Срезы
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ..


# help(функция) # помошник


# Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#   i *= 2
#   print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#   print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


# Функции
# Это фрагмент программы, используемый 
# многократно

# def f(x):
#     return x**2
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
