# # 1. Анонимные, Lambda

# # def f(x):
# #     x**2

# # # print(type(f)) # class function
# # g = f
# # print(f(1)) # None
# # print(g(1)) # работают одинаково


# # def f(x):
# #     return x**2

# # g = f

# # print(type(f)) # class function
# # print(type(g)) # class function

# ############

# # def  calc1(x):
# #     return x + 10

# # # print(calc1(10))

# # def  calc2(x):
# #     return x * 10

# # # print(calc2(10)) 

# # def  math(op, x):
# #     print(op(x))

# # math(calc2, 10) # 100
# # math(calc1, 10) # 20

# ############

# # def su(x, y):
# #     return x + y

# # f = sum
# # sum = lambda x, y,:x + y

# # def mylt(x, y):
# #     return x * y
    
# # def calc(op, a, b):
# #     print(op(a, b))
# #     # return(op(a, b))

# # # calc(mylt, 4, 5) 
# # # calc(sum, 4, 5) 
# # calc(lambda x, y,:x + y, 4, 5) 


# # List Coprehension

# # [exp for item in iterable]
# # [exp for item in iterable(if conditional)]
# # [exp <if conditional> for item in iterable (if conditional)]

# # list = []

# # for i in range(1, 101):
# #     if(i % 2 == 0):
# #         list.append(i)

# # print(list)


# # list = [i for i in range(1, 11) if i % 2 == 0] # задаввать переменную
# # list = [(i, i) for i in range(1, 11) if i % 2 == 0] # задавать картеж

# # def f(x): # функция
# #     return x ** 3

# # list = [f(i) for i in range(1, 11) if i % 2 == 0]
# # list = [(i, f(i)) for i in range(1, 11) if i % 2 == 0]


# # В файле хранятся числа, нужно выбрать четные и 
# # составить список пар (число; квадрат числа). 
# # Пример:
# # 1 2 3 5 8 15 23 38
# # Получить:
# # [(2, 4), (8, 64), (38, 1444)]

# # list = [1, 2, 3, 5, 8, 15, 23, 38]
# # def f(x):
# #     return x ** 2
# # l = [(list[i], f(list[i])) for i in range(0, len(list)) if list[i] % 2 == 0]
# # print(l)

# # path = 'Путь к файлу' # путь к файлу
# f = open('f.txt', 'r') # связваем файловую переменную с нашей переменной
# data = f.read() + ' ' # считваем  все что есть и добавляем туда пробел
# f.close() # закрваем файл

# numbers = []

# while data != '': # пока моя строка не пустая
#     space_pos = data.index(' ') # найти первую позицию пробела
#     numbers.append(int(data[:space_pos])) # взять все что находится от первой позиции до пробела, превратить в число и добавить в новый списоок
#     data = data[space_pos+1:] # обновить строку

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]

# def wher(f, col):
#     return [x for x in col if f(x)]

# res = select(int, data)
# res = wher(lambda x: not x % 2, res)
# res = select(lambda x: (x, x ** 2), res)
# print(res)

# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))


# # Функция map
# # Функция map() применяет указанную функцию к 
# # каждому элементу итерируемого объекта и 
# # возвращает итератор с новыми объектами.
# # f(x) ⇒ x + 10 
# # map(f, [ 1, 2, 3, 4, 5])
# #  ↓ ↓ ↓ ↓ ↓
# #  [ 11, 12, 13, 14, 15]
# # Нельзя пройтись дважды


# li = [x for x in range(1, 20)] # создаем список
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)


# Функция filter
# Функция filter() применяет указанную функцию к 
# каждому элементу итерируемого объекта и 
# возвращает итератор с теми объектами, для 
# которых функция вернула True.
# f(x) ⇒ x - чётное 
# filter(f, [ 1, 2, 3, 4,5])
#  ↓ 
#  [ 2, 4 ]
# Нельзя пройтись дважды

# data = '1 2 3 5 8 15 23 38'.split()
# data = map(int, data)
# data = filter(lambda e: not e % 2, data)
# data = list(map(lambda e: (e, e**2), data))
# print(data)


# Функция zip() применяется к набору итерируемых 
# объектов и возвращает итератор с кортежами из 
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора 
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7] # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# salary = [111, 222, 333] # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# data = list(zip(users, ids,salary))
# print(data)


# Функция enumerate 
# Функция enumerate() применяется к итерируемому 
# объекту и возвращает новый итератор с кортежами 
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

users = ['user1', 'user2', 'user3', 'user4', 'user5']

data = list(enumerate(users)) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]
print(data)

