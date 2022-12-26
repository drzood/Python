import model as m

def main_metod():
    x, list = '', []
    while x != 7:
        x = input("""
1. Создать новую запись
2. Вывести в терминал
3. Экспорт txt
4. Экспорт csv
5. Импорт txt
6. Импорт csv
7. Выйти из программы
Введите от 1 до 7: """)
        if x == '1':    
            list = m.add_list()
            [print(' '.join(i)) for i in x]
        elif x == '2':  [print(' '.join(i)) for i in list]
        elif x == '3':  m.exp_txt(list)
        elif x == '4':  m.exp_csv(list)
        elif x == '5':  list = m.imp_txt()
        elif x == '6':  list = m.imp_csv()
        elif x == '7':  break
        else:           print(f'Вы ввели недопустимое значение {x}, повторите попытку.')
