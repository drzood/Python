# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# chislo = int(input('a = '))
# summa = 0
# while chislo > 0:
#     ostatok = chislo % 10
#     summa += ostatok
#     chislo //= 10
# print(summa)


chislo = float(input('a = '))

while chislo % 1 < 0:
    chislo *= 10

summa = 0

while chislo > 0:
    ostatok = chislo % 10
    summa += ostatok
    chislo //= 10
print(int(summa))