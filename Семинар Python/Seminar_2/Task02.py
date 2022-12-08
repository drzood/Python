# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.

#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# n = int(input('N = '))
# n_list = {}
# for i in range(1, n + 1):
#     n_list[i] = i * 3 + 1
# print(n_list)

n = int(input('N = '))
# n_list = {i: 3 * i + 1 for i in range(1, n+1)}
# print(n_list)

cl = []
for i in range(n):
    cl.append(3 * (i + 1) + 1)
    print(f'{i + 1}:{cl[i]}', end=" ")