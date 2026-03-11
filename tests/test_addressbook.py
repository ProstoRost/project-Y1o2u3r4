from ContactHelper.core import AddressBook
from ContactHelper.models.contact import Contact


def test_add_contact():
    book: AddressBook = AddressBook()
    book.add_contact(name="John")

    assert "john" in book.data
    assert book.find("John").name == "John"


def test_find_contact():
    book: AddressBook = AddressBook()
    book.add_contact(name="Anna")

    found: Contact = book.find("Anna")

    assert found is not None
    assert found.name == "Anna"


def test_delete_contact():
    book: AddressBook = AddressBook()
    book.add_contact(name="Mike")

    assert book.delete_contact("Mike") is True
    assert "mike" not in book.data


def test_add_phone():
    contact: Contact = Contact("Kate")
    contact.change_phone("123456789")

    assert len(contact.phones) == 1
    assert contact.phones[0].value == "+380123456789"
