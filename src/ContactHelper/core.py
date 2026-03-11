from collections import UserDict
from src.ContactHelper.models.contact import Contact


class AddressBook(UserDict):
    '''Клас для роботи з контактами'''
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return f'AddressBook with {len(self.data)} contacts'

    def add_contact(self, contact: Contact) -> bool:
        '''Додає контакт до адресної книги
        Args:
            contact (Contact): контакт для додавання
        Raises:
            ValueError: якщо контакт з таким ім'ям вже існує
        Returns:
            bool: True, якщо контакт додано, False в іншому випадку'''
        pass

    def get_contact(self, name: str) -> Contact:
        '''Повертає контакт за ім'ям
        Args:
            name (str): ім'я контакту для пошуку
        Returns:
            Contact: контакт з вказаним ім'ям або
            None, якщо контакт не знайдено'''
        pass

    def delete_contact(self, name: str) -> bool:
        '''Видаляє контакт за ім'ям
        Args:
            name (str): ім'я контакту для видалення
        Returns:
            bool: True, якщо контакт видалено,
            False в іншому випадку'''
        pass

    def setbirthday(self, name: str, date: str) -> bool:
        '''Встановлює дату народження для контакту
        Args:
            name (str): ім'я контакту для якого потрібно встановити дату народження
            date (str): дата народження для встановлення у форматі YYYY-MM-DD
        Raises:
            ValueError: якщо контакт з вказаним ім'ям не знайдено або якщо дата народження не відповідає формату YYYY-MM-DD
        Returns:
            bool: True, якщо дата народження встановлена, False в іншому випадку'''
        pass

    def updatephone(self, name: str, new_phone: str, phone: str = None) -> bool:
        '''Додає або оновлює телефонний номер для контакту
        Args:
            name (str): ім'я контакту для якого потрібно додати телефонний номер
            new_phone (str): новий телефонний номер для дoдавання у форматі +380XXXXXXXXX
            phone (str): телефонний номер для заміни у форматі +380XXXXXXXXX
        Raises:
            ValueError: якщо контакт з вказаним ім'ям не знайдено або якщо телефонний номер не відповідає формату +380XXXXXXXXX
        Returns:
            bool: True, якщо телефонний номер додано, False в іншому випадку'''
        pass
