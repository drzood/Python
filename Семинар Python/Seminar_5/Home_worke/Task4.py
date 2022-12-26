# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# import re

# s = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# rle = []
# count = 0

# for i in range(0, len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     elif s[i] != s[i + 1]:
#         count += 1
#         rle.append(count)
#         rle.append(s[i])
#         count = 0
#     if i == (len(s) - 2) and s[-2] != s[-1]:
#         rle.append(1)
#         rle.append(s[i])
#     elif i == (len(s) - 2) and s[-2] == s[-1]:
#         count += 1
#         rle.append(count)
#         rle.append(s[i])

# st = ''
# for el in rle:
#     st += str(el)

# print('Текст после кодировки:', st)

# with open('for_task_4.txt', 'w') as file:
#     file.write(st)


# # 2 часть задачи:
# with open('for_task_4.txt') as file:
#     part_2 = file.read()

# sp2 = []
# for i in range(len(part_2)):
#     if part_2[i].isalpha():
#         sp2.append(part_2[i])

# rep = re.compile("[^0-9,\d]")
# part_2 = rep.sub(" ", part_2)
# sp1 = part_2.split()

# res = ''
# for i in range(len(sp1)):
#     res += sp2[i] * int(sp1[i])

# print('Текст после дешифровки:', res)

# with open('for_task_4_2.txt', 'w') as file:
#     file.write(res)

# if s == res:
#     print(True)
# else:
#     print(False)

file5 = open('file5.txt', 'w')
ex5 = 'AdddLLkkKKfffffffKKDDnnRR'
file5.write(ex5)
file5.close()

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
                count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    num = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            num += txt[i]
        else:
            res = res + txt[i] * int(num)
            num = ''
    return res

pol6 = open('file6.txt', 'w')
coding (ex5)
pol6.write(coding(ex5))

print(coding(ex5))
print(decoding(coding(ex5)))
pol6.close()