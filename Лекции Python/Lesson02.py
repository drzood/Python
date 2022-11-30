# Моды:
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # указываем путь к файлу и мод с которым будем работать
# data.writelines(colors) # разделителей не будет redgreenblue
# data.close()

# exit() # дальше эксита кот не будет  читаться


# # 1. Вариант

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # указываем путь к файлу и мод с которым будем работать
# data.write('LINE 1\n')
# data.write('LINE 2\n')
# data.close()

# # 2. Вариант

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close() 

# import hello # вызов файла hello
# print(hello.F(1))

# import hello as h # синоним для файла, используя который мы будем оращаться к файлу хелло
# print(h.F(1))

# Функции

# def f(x):
#  return x**2
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType


# new file function_file.py
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# file hello.py
# import function_file 
# print(function_file.f(1)) # Целое
# print(function_file.f(2.3)) # 23
# print(function_file.f(28)) # None


# new file function_file.py
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# file hello.py
# import function_file as ff
# print(ff.f(1)) # Целое
# print(ff.f(2.3)) # 23
# print(ff.f(28)) # None


# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...


# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12


# def concatenatio(*params):
#     res: str = "" # в случае с работами с числами res = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...


# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# Кортежи


# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')


# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support 
# item assignment


# t = tuple(['red', 'green', 'blue']) # двoйное
# red, green, blue = t # преобразование, из кортежа создаем переменные
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue


# Словари

# Неупорядоченные коллекции произвольных 
# объектов с доступом по ключу


# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться


# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: 
# # for (k,v) in dictionary.items():
#   print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →


# Множества

# Неупорядоченная совокупность элементов


# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set


# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}


# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') 
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # добавить
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # Удалить
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok # удалить значение
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } # очистить ножество
# print(colors) # set()


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} # создание копии
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} # объединение множеств
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}

# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13)

# s = frozenset(a) # замроженные множества, неизменяемые



# Неизменяемое множество

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


# Списки

# list1[0] = 123
# list2[1] = 333

# list1 = [1,2,3,4,5]
# list2 = list1
# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# print(list1.pop()) # удаление последнего элемента из списка
# print(len(list1)) # проверяем длинну списка


