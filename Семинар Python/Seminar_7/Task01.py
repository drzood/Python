# 1.Напечатать сторку в одну линию - C:\WINDOWS\System32\drivers\etc\nst

print('C:\WINDOWS\System32\drivers\etc\\nst') # экранировали бэкслэш \
print(r'C:\WINDOWS\System32\drivers\etc\nst') 

# 2. a = [4, 3, -10, 1, 7, 12] a=[4, -10, 12, 3, 1, 7]

a = [4, 3, -10, 1, 7, 12]
b = sorted(a, key = lambda x: x % 2 == 0, reverse = True)
print(b)

a = [4, 3, -10, 1, 7, 12]
a.sort(key = lambda x: x % 2)
print(a)

# 3. На вход программы поступает список наименований рек, 
# записанных в одну строчку через пробел. Необходимо 
# отсортировать этот список в порядке убывания длин 
# названий. Результат вывести в одну строчку через пробел.
# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон

string = 'Лена Енисей Волга Дон'
river = string.split()
river_res = sorted(river, key = lambda x: len(x), reverse = True)
print(' '.join(river_res))

s = sorted('Лена Енисей Волга Дон'.split(), key=lambda x: len(x))[::-1]
print(*s)

# 4. Напишите программу, которая подсчитает и выведет 
# сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное 
# двузначное число, а не его квадрат.

print(sum(map(lambda x: x**2, filter(lambda x: x % 9 == 0, range(10, 100)))))
print(sum(map(lambda x: x**2, filter(lambda x: not x % 9, range(10, 100)))))

# 5. Напишите функцию triangle(a, b, c), которая принимает 
# на вход три длины отрезков и определяет, можно ли из этих 
# отрезков составить треугольник.

# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

def Triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

a = int(input('введите а: '))
b = int(input('введите b: '))
c = int(input('введите c: '))
print('Это треугольник' if Triangle(a, b, c) else "Это не треугольник")

# print((lambda a: a[0] + a[1] > a[2] )(sorted(triangle)))