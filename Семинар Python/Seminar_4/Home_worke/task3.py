# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]


user_set = [int(i) for i in input('Введите последовательность чисел через запятую: ').split(',')] 
sl = {}                         
res_list = []                    

for el in user_set:             
    sl[el] = user_set.count(el)

for key, value in sl.items():    
    print(key, value)
    if value == 1:
        res_list.append(int(key))

print(res_list)


# a= [1,2,2,2,2,3,1,4]
# print(set(a))


from random import randint

a = randint(5, 10)
b = []
for i in range(a):
    b.append(randint(1, 9))
print(b)
c = []
for i in b:
    if b.count(i) == 1:
        c.append(i)
print(c)



digits = [1, 2, 4, 5, 3, 2, 1, 1, 2, 4, 5, 7, 8]
dct = {}
for k in set(digits):
    dct.setdefault(k, digits.count(k))
print(f'Неповторяющиеся элементы:', end=' ')
for k, v in dct.items():
    if int(v) == 1:
        print(k, end=' ')