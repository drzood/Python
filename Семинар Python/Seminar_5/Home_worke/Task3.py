# Создайте программу для игры в ""Крестики-нолики"".


print('Игра в крестики-нолики\n\nВводите цифру из '
      'поля для заполнения Х/О\n\n1 2 3\n4 5 6\n7 8 9')

f = ['\n', '1', '2', '3', 
     '\n', '4', '5', '6', 
     '\n', '7', '8', '9']
#      0    1    2    3     4    5    6    7     8    9   10   11
for i in range(1, 10, 2):
    p1 = input('\nХод первого игрока (X): ')
    f = [i.replace(p1, 'X') for i in f]
    print("".join(f))

    p2 = input('\nХод второго игрока (O): ')
    f = [i.replace(p2, 'O') for i in f]
    print("".join(f))

    if   f[1] == 'X' and f[5] == 'X' and f[9] == 'X':   print('Первый игрок победил!')
    elif f[2] == 'X' and f[6] == 'X' and f[10] == 'X':  print('Первый игрок победил!')
    elif f[3] == 'X' and f[7] == 'X' and f[11] == 'X':  print('Первый игрок победил!')
    elif f[2] == 'X' and f[6] == 'X' and f[10] == 'X':  print('Первый игрок победил!')
    elif f[1] == 'X' and f[2] == 'X' and f[3] == 'X':   print('Первый игрок победил!')
    elif f[5] == 'X' and f[6] == 'X' and f[7] == 'X':   print('Первый игрок победил!')
    elif f[9] == 'X' and f[10] == 'X' and f[11] == 'X': print('Первый игрок победил!')
    elif f[1] == 'X' and f[6] == 'X' and f[11] == 'X':  print('Первый игрок победил!')
    elif f[3] == 'X' and f[6] == 'X' and f[9] == 'X':   print('Первый игрок победил!')
 
    elif f[1] == 'O' and f[5] == 'O' and f[9] == 'O':   print('Первый игрок победил!')
    elif f[2] == 'O' and f[6] == 'O' and f[10] == 'O':  print('Первый игрок победил!')
    elif f[3] == 'O' and f[7] == 'O' and f[11] == 'O':  print('Первый игрок победил!')
    elif f[2] == 'O' and f[6] == 'O' and f[10] == 'O':  print('Первый игрок победил!')
    elif f[1] == 'O' and f[2] == 'O' and f[3] == 'O':   print('Первый игрок победил!')
    elif f[5] == 'O' and f[6] == 'O' and f[7] == 'O':   print('Первый игрок победил!')
    elif f[9] == 'O' and f[10] == 'O' and f[11] == 'O': print('Первый игрок победил!')
    elif f[1] == 'O' and f[6] == 'O' and f[11] == 'O':  print('Первый игрок победил!')
    elif f[3] == 'O' and f[6] == 'O' and f[9] == 'O':   print('Первый игрок победил!')


