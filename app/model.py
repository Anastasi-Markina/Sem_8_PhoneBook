def parse_contact(contact):
    contact_as_list = contact.split()
    return ' '.join(contact_as_list[:-1]), contact_as_list[-1]


class PhoneBook:
    def __init__(self, data_path = 'data/contacts.txt', owner ='Самодуров Данил'):
        contacts = {}
        with open(data_path, 'r', encoding='utf8') as f:
            while True:
                contact = f.readline()
                if not contact:
                    break
                name, phone_number = parse_contact(contact)
                contacts[phone_number] = name
        self.owner = owner
        self.data_path = data_path
        self.contacts = contacts

    def get_owner(self):
        return self.owner

    def set_owner(self, name):
        self.owner = name

    def get_contacts(self):
        return self.contacts.copy()

    def set_contacts(self, contacts):
        self.contacts = contacts
        self.update_data()

    def get_data_path(self):
        return self.data_path

    def set_data_path(self, path):
        self.data_path = path
        self.update_data()

    def update_data(self):
        with open(self.data_path, 'w', encoding='utf8') as f:
            for number in self.contacts.keys():
                name = self.contacts[number]
                f.write(f'{name} {number}\n')
