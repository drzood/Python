# Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

sum = 1                     # переменная для подсчетов
data = open('file.txt', 'r')# открываем файл для чтения
for line in data:           # запускаем цикл использую строки файла
    sum *= int(line)        # ищем произведение
    print(sum, end=' ')     # выводим произведение каждого числа
data.close()                # на сколько понял, это закрытие файла

# n = int(input('n = '))

# list_n = []
# for i in range(-abs(n), abs(n) + 1):
#     list_n.append(i)
# print(list_n)

# prod = 1
# path = 'file.txt'
# with open(path, 'r') as data:
#     for line in data:
#         prod *= list_n[int(line)]
#     print(prod)
