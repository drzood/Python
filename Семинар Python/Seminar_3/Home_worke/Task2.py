# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

# Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 5, 7]   # задаем список
sum_lst = []         # создаем пустой список
for i in range(int(round(len(lst) / 2 + .5))):  # цикл с длинной списка деленный пополам и округлением в большую сторону
    sum_lst.append(lst[i] + lst[-1-i]) # складываем ячейки списка согласно заданию
print(sum_lst)       #  выводим