import sys

from controller import PhoneBookController, PhoneBook, PhoneBookViewer


def main():
    sys.path.append('..')
    book = PhoneBook()
    viewer = PhoneBookViewer()
    controller = PhoneBookController(book, viewer)
    controller.run()


if __name__ == '__main__':
    main()