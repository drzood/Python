# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

lst = []

def binari(num):
    if num == 0:
        return 1
    bin = num % 2
    lst.append(bin)
    binari(num // 2)

num = int(input('num = '))
binari(num)
lst.reverse()
print(lst)