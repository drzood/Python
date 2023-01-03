
def list_items():
    return ['Name', 'Last name', 'Position', 'Salary']
    

def get_add_data():
    data = ['','','','']
    print('\nЗаполните даные')
    for i in range(4):
        data[i] = input(f'{list_items()[i]}: ')
    data[3] += '\n'
    return data
