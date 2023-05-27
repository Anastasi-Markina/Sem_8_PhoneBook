from model import PhoneBook, parse_contact
from view import PhoneBookViewer


class PhoneBookController:
    def __init__(self, book=None, viewer=None):
        if book is None:
            book = PhoneBook()
        if viewer is None:
            viewer = PhoneBookViewer()
        self.book = book
        self.viewer = viewer
        self.commands = {
            '1': [self.add_contact, self.viewer.value_request('1')],
            '2': [self.remove_contact_by_name, self.viewer.value_request('2')],
            '3': [self.remove_contact_by_number, self.viewer.value_request('3')],
            '4': [self.viewer.print_contacts, self.book.get_contacts]
        }

    def run(self):
        self.viewer.greetings(self.book.get_owner())
        while True:
            command = self.viewer.menu()
            if command not in self.commands.keys():
                break
            self.process_command(command)
        self.viewer.goodbye(self.book.get_owner())

    def add_contact(self, contact):
        name, phone_number = parse_contact(contact)
        contacts = self.book.get_contacts()
        contacts[phone_number] = name
        self.book.set_contacts(contacts)

    def remove_contact_by_number(self, number):
        if number in self.book.contacts.keys():
            del self.book.contacts[number]
            self.book.update_data()

    def remove_contact_by_name(self, name):
        for number in self.book.contacts.keys():
            if self.book.contacts[number] == name:
                del self.book.contacts[number]
                break

    def process_command(self, command):
        args = self.commands[command][1]()
        self.commands[command][0](args)