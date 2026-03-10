'''
ToDo:
- додайте функцію валідації телефонного номера, яка буде перевіряти чи номер
телефону відповідає формату +380XXXXXXXXX, де X - це цифра від 0 до 9. Якщо
номер телефону не відповідає цьому формату, функція повинна виводити
повідомлення про помилку.
- додайте функцію валідації електронної пошти, яка буде перевіряти чи
електронна пошта відповідає формату user@example.com
'''


def validate_phone_number(phone_number: str) -> str:
    """Повертає телефонний номер, якщо його можна вважати валідним або
    повертає помилку
    Args:
    phone_number (str): телефонний номер у форматі +380XXXXXXXXX
    Returns:
        str: телефонний номер, якщо він валідний
    Raises:
        ValueError: якщо телефонний номер не відповідає формату +380XXXXXXXXX
    """
    if not isinstance(phone_number, str):
        raise ValueError("Phone number must be a string")

    if len(phone_number) != 13:
        raise ValueError("Phone number must be in format +380XXXXXXXXX")

    if not phone_number.startswith("+380"):
        raise ValueError("Phone number must be in format +380XXXXXXXXX")

    if not phone_number[1:].isdigit():
        raise ValueError("Phone number must be in format +380XXXXXXXXX")

    return phone_number


def validate_email(email: str) -> str:
    """Повертає електронну пошту, якщо її можна вважати валідною або
    повертає помилку
    Args:
    email (str): електронна пошта у форматі user@example.com
    Returns:
        str: електронна пошта, якщо вона валідна
    Raises:
        ValueError: якщо електронна пошта не відповідає формату
        user@example.com
    """
    if not isinstance(email, str):
        raise ValueError("Email must be a string")

    if "@" not in email or email.count("@") != 1:
        raise ValueError("Email must be in format user@example.com")

    user, domain = email.split("@")
    if not user or not domain:
        raise ValueError("Email must be in format user@example.com")

    if "." not in domain:
        raise ValueError("Email must be in format user@example.com")

    return email
    