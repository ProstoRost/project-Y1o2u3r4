from .fields import Phone, Birthday, Address


class Contact:

    def __init__(self, name: str):
        self.name = name
        self.phones: list[Phone] = []
        self.birthday: Birthday = None
        self.address: Address = None

    def change_phone(self, new_phone:str, phone: str = None) -> bool:
        pass

    def update_birthday(self, date: str) -> bool:
        pass

    def update_address(self, address: str) -> bool:
        pass