import datetime
from src.ContactHelper.utils import validate_phone_number, validate_email
from colorama import init, Fore


class Field:
    '''Базовий клас для всіх полів контакту'''
    def __init__(self, value):
        self.value = value.strip()


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(validate_phone_number(value))

    def change_phone(self, value: str):
        self.value = validate_phone_number(value)


class Birthday(Field):
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError(f"Invalid date format ({value}). Use DD.MM.YYYY")

    def __str__(self) -> str | None:
        '''Повертає дату народження у форматі DD.MM.YYYY
        Returns:
            str: дата народження у форматі DD.MM.YYYY
        '''
        if not self.value:
            return None
        init(autoreset=True)
        return f"{Fore.YELLOW}{self.value.strftime('%d.%m.%Y')}{Fore.RESET}"


class Address(Field):
    def __init__(self, value: str):
        super().__init__(value)


class Email(Field):
    def __init__(self, value: str):
        super().__init__(validate_email(value))

    def change_email(self, value: str):
        self.value = validate_email(value)
