from collections import UserDict


class Field:
    pass


class AddressBook(UserDict, Field):
    def add_record(self, record):
        self.data[record.name] = record


class Name:
    def __init__(self, name):
        self.value = name


class Phone:
    def __init__(self, phone):
        self.value = phone


class Record():
    def __init__(self, name, phone=None):
        self._name = Name(name)
        self.phones = [Phone(phone)] if phone else []

    @property
    def name(self):
        return self._name.value

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        is_phone = False
        for i, v in enumerate(self.phones):
            value = v.value
            if value == phone:
                is_phone = True
                del self.phones[i]

        if is_phone:
            return f'{phone} was deleted'
        else:
            raise KeyError

    def show_phones(self):
        return ', '.join([i.value for i in self.phones])
