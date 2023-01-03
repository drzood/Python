import model as m


def controller():

    bd = m.imp_list_of_employees()
    while True:
        x = input('''\nSelect the required actions:
    1. Добавить сотрудника;                 +
    2. Удалить сотрудника;                  +
    3. Найти сотрудника;                    +
    4. Обновить данные сотрудника;          +   
    5. Экспортировать данные в формате json;
    6. Экспортировать данные в формате cmv;
    7. Закончить работу.

Answer(1-7): ''')
        if x == '1':        bd += m.add_an_employee()
        elif x == '2':      bd = m.delete_employee(bd)
        elif x == '3':      m.search_employee(bd)
        elif x == '4':      m.change_data_employee(bd)
        elif x == '5':      m.exp_json(bd)
        elif x == '6':      m.exp_csv(bd)
        elif x == '7':
            print(bd)
            m.exp_list_of_employees(bd)
            break
        else:              print(f'{x} - Invalid value, please try again.')