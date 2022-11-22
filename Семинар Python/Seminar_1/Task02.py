lst = [1, 9, 5, 6, 8]
max = lst[0]
for i in range(0, len(lst)):
    if lst[i] > max:
        max = lst[i]
print(f'{max}')