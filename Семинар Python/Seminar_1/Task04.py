# Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.

# Примеры:
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

num = (input('num = '))
for i in range(len(num)):
    if num[i] == ".":
        print(num[i + 1])
        break