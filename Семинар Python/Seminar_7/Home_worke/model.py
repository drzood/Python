import view as v

def add_list():
    x, y = '', []
    while x != 'Нет':
        x = input('\nДобавить новый контакт? Да/Нет\n')
        if x == 'Да' or x == 'да':
            y.append(v.get_add_data())
            print()
        elif x == 'нет':
            break
        else:
            print(f'\nВы ввели {x}, повторите попытку и ответьте только Да или Нет.\n')
    return y

def exp_txt(x):
    with open('directory.txt', 'a') as data:
        [data.write(','.join(x[i])) for i in range(len(x))]

def exp_csv(x):
    with open('directory.csv', 'a') as data:
        [data.write(','.join(x[i])) for i in range(len(x))]

def imp_txt():
    x = []
    with open('directory.txt', 'r') as data:
        for line in data:
            x.append([line])
        return x

def imp_csv():
    x = []
    with open('directory.csv', 'r') as data:
        for line in data:
            x.append([line])
        return x

