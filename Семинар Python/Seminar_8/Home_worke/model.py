import view as v
import json
import csv
import logging


def import_file(path):
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        return list(reader)

def add_an_employee(): # добавить сотрудника
    x, y = '', []
    while x != 'Нет':
        x = input('\nДобавить нового сотрудника? Да/Нет\n')
        if x == 'Да' or x == 'да':
            y.append(v.get_add_data())
            print()
        elif x == 'нет':
            break
        else:
            print(f'\nВы ввели {x}, повторите попытку и ответьте только Да или Нет.\n')
            logging.info(f'Ответ {x}')
    return y

def exp_list_of_employees(x): # экспорт бд
    with open('employees.txt', 'w') as data:
        return [data.write(','.join(x[i])) for i in range(len(x))]

def imp_list_of_employees(): # импорт бд
    x = []
    with open('employees.txt', 'r') as data:
        for line in data:
            x.append([line])
        return x

def search_employee(x):
    n, e, y = 0, 0, input('Введите ключевое слово для поиска струдника: \n')
    for i in range(len(x)):
        for j in x[i]:
            if y in j:
                print(f'№ {i} - {j}')
                e = i
                n += 1
    print(f'Найдено соотвестсвий: {n}\n')
    logging.info(f'Найдено соотвестсвий: {n}')
    return e

def delete_employee(x):
    print('Необходимо найти сотрудника и узнаеть его номер.')
    i = search_employee(x)
    y = int(input('Введите № струдника на удаление: '))
    if y in range(len(x)):
        z = input(f'Вы уверены, будет удален №{y}? Да/Нет   ')
        if z == 'Да' or z == 'да':      x.pop(y)
        elif z == 'Нет' or z == 'нет':  return x
    else:       
        print('Проверььте введенные данные и при небходиости повториет попытку.')
        logging.info(f'Ответ {z}')
    return x

def change_data_employee(x):
    print('Необходимо найти сотрудника и узнаеть его номер.')
    i = search_employee(x)
    y = int(input('Введите № струдника для изменения: '))
    if y in range(len(x)):
        x[i] = v.get_add_data()

def exp_json(x):
    y = [v.list_items(), x]
    with open('employees.json', 'w') as data:
        data.write(json.dumps(y))
    print('Сохранено в файл employees.json')

def exp_csv(x):
    with open('employee.csv', 'w') as data:
        writer = csv.writer(data)
        for i in x:
            writer.writerow(i) 
            print(i)
    print('Сохранено в файл employees.csv')