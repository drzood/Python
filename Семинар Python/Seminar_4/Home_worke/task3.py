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