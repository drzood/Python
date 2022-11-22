# Дроби

num = (input('num = '))
for i in range(len(num)):
    if num[i] == ".":
        print(num[i + 1])
        break