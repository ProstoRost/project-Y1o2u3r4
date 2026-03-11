from .fields import Email, Phone, Birthday, Address
from src.ContactHelper.utils import validate_phone_number, validate_email


class Contact:

    def __init__(self, name: str):
        self._name = name.strip()
        self._phones: list[Phone] = []
        self._birthday: Birthday = None
        self._address: Address = None
        self._email: Email = None

    @property
    def name(self) -> str:
        """Повертає ім'я контакту"""
        return self._name

    @property
    def birthday(self) -> str | None:
        """Повертає дату народження контакту в форматі YYYY-MM-DD
        або None, якщо дата народження не встановлена"""
        return self._birthday

    @birthday.setter
    def update_birthday(self, date: str) -> bool:
        '''Встановлює дату народження для контакту
        Args:
            date (str): дата народження у форматі DD.MM.YYYY
        Returns:
            bool: True, якщо дата народження оновлена успішно
        '''
        if not date:
            return False
        if self._birthday:
            if self._birthday.value == date:
                return False
        self._birthday = Birthday(date)

    @property
    def address(self) -> Address | None:
        """Повертає адресу контакту або None, якщо адреса не встановлена"""
        return self._address

    @address.setter
    def address(self, value: str) -> bool:
        """Встановлює адресу контакту
        Args:
            value (str): адреса для встановлення
        """
        if not value or self._address.value == value:
            return False
        if self._address:
            if self._address.value == value:
                return False
        self._address = Address(value)
        return True

    @property
    def phones(self) -> list[Phone] | None:
        """Повертає список телефонних номерів контакту або порожній список,
        якщо телефонні номери не встановлені"""
        return self._phones

    def find_phone(self, phone: str) -> Phone | None:
        """
        Пошук телефону в записі.
        Args:
            phone: Номер телефону для пошуку
        Returns:
            Знайдений об'єкт Phone або None, якщо не знайдено
        """
        try:
            phone: str = validate_phone_number(phone)
            for p in self.phones:
                if p.value == phone:
                    return p
        except:
            return None

    def remove_phone(self, phone: str) -> bool:
        '''Видаляє телефонний номер з контакту
        Args:
            phone (str): телефонний номер для видалення
        Returns:
            bool: True, якщо телефонний номер видалено, False в іншому випадку
        '''
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            return True
        return False

    def change_phone(self, new_phone: str, phone: str = None) -> bool:
        '''Додає або оновлює телефонний номер для контакту
        Args:
            new_phone (str): новий телефонний номер
            для додавання у форматі +380XXXXXXXXX
            phone (str): телефонний номер для заміни у форматі +380XXXXXXXXX
        Returns:
            bool: True, якщо телефонний номер додано, False в іншому випадку
        Raises:
            ValueError: якщо телефонний номер не
            відповідає формату +380XXXXXXXXX
        '''
        new_phone = validate_phone_number(new_phone)
        if not new_phone:
            raise ValueError(f'Invalid phone number format: {new_phone}')

        if phone:
            phone = validate_phone_number(phone)
            if not phone:
                raise ValueError(f'Invalid phone number format: {phone}')

            for p in self._phones:
                if p.value == phone:
                    p.change_phone(new_phone)
                    return True
            return False
        self._phones.append(Phone(new_phone))
        return True

    @property
    def email(self) -> Email:
        """Повертає електронну пошту контакту або None,
        якщо електронна пошта не встановлена"""
        return self._email

    @email.setter
    def email(self, value: str):
        '''Встановлює електронну пошту контакту
        Args:
            email (str): нова електронна пошта
            для додавання у форматі user@example.com
        Returns:
            bool: True, якщо електронна пошта оновлена успішно
        Raises:
            ValueError: якщо електронна пошта
            не відповідає формату user@example.com
        '''
        email = validate_email(value)
        if not email:
            raise ValueError(f'Invalid email format: {email}')
        if self._email == email:
            return False
        self._email = email
        return True
