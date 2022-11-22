a = int(input("a = "))
b = int(input("b = "))
if a == b**2 or b == a**2:
    print(f'{a} является квадратом числа {b}')
elif b == a**2:
    print(f'{b} является квадратом числа {a}')
else:
    print('Повторите попытку')
# print(a == b**2 or b == a**2)


