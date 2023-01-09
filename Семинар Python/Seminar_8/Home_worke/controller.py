import model as m
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    encoding='UTF-8')

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
        if x == '1':        
            logging.info('Выбран пункт меню: 1')
            bd += m.add_an_employee()
            logging.info('Отлично сработано!')
        elif x == '2':      
            logging.info('Выбран пункт меню: 2')
            bd = m.delete_employee(bd)
            logging.info('Отлично сработано!')
        elif x == '3':      
            logging.info('Выбран пункт меню: 3')
            m.search_employee(bd)
            logging.info('Отлично сработано!')
        elif x == '4':      
            logging.info('Выбран пункт меню: 4')
            m.change_data_employee(bd)
            logging.info('Отлично сработано!')
        elif x == '5':      
            logging.info('Выбран пункт меню: 5')
            m.exp_json(bd)
            logging.info('Отлично сработано!')
        elif x == '6':      
            logging.info('Выбран пункт меню: 6')
            m.exp_csv(bd)
            logging.info('Отлично сработано!')
        elif x == '7':
            logging.info('Выбран пункт меню: 7')
            print(bd)
            m.exp_list_of_employees(bd)
            logging.info('Отлично сработано!')
            break
        else:              
            logging.info(f'Выбран неизвестный пункт меню: {x}')
            print(f'{x} - Invalid value, please try again.')