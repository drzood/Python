# Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N

# Примеры:
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

n = int(input('N = '))
# nums = []
for i in range(-abs(n), abs(n) + 1, 1):
    # nums.append(i)
    print(i, end = ' ')
# print(nums)5
