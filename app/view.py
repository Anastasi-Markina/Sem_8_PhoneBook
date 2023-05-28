class PhoneBookViewer:

    def __init__(self):

        self.value_requests = {
            '1': lambda: input('Введите контакт в формате "Имя Номер"\n'),
            '2': lambda: input('Введите Имя\n'),
            '3': lambda: input('Введите Номер\n')
        }

    def greetings(self, owner):
        print(f'Приветствуем тебя, {owner}')

    def goodbye(self, owner):
        print(f'Да пребудет с тобой Сила, {owner}!')

    def menu(self):
        print('\n\nВыберете действие:\n'
              '1: добавить контакт\n'
              '2: удалить контакт по имени\n'
              '3: удалить контакт по номеру\n'
              '4: вывести все контакты\n'
              'другое: выйти из меню\n')
        
        return input()

    def value_request(self, command):
        return self.value_requests[command]

    def print_contacts(self, contacts):
        print('Все контакты:')
        for number in contacts.keys():
            
            print(contacts[number], number)