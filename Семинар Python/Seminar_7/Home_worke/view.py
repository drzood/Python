def ref_book_list():
    return ['Фамилия','Имя','Телефон','Описание']

def get_add_data():
    data = ['','','','']
    print('\nЗаполните даные')
    for i in range(4):
        data[i] = input(f'{ref_book_list()[i]}: ')
        if data[i] == '' or data[i] == ' ': data[i] = ' - '
    data[3] += '\n'
    return data
