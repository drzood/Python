# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.


sum = n = int(input('N = ')) # вводим две переменные, на сумму и для подсчета
l = []                       # список для ввода решения
c = 2                        # переменная для цикла
while c <= n:                # запускаем цикл
    if n % c == 0:           # если остаток от деления равен 0
        n /= c               # тогда 
        l.append(c)          # записываем результат в список
    else:
        c += 1               # ииначе счетчик + 1
print(f'{sum} = {" * ".join(map(str, l))}')
n = int(input("Введите число N: "))
i = 2
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители введенного числа указаны в списке: {list}")
