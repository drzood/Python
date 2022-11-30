# Напишите программу, в которой пользователь будет задавать 
# две строки, а программа - определять количество вхождений о
# дной строки в другой.

str1 = input('Первая строка: ')
str2 = input('Вторая строка: ')

# str1_arr = str1.split()
# count = 0
# for i in str1_arr:
#     if i.lower() == str2.lower():
#         count += 1
# print(count)

print(str1.count(str2))
