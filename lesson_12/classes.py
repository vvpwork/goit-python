from collections import UserDict
from datetime import datetime, timedelta
from re import match

phone_regex = r"[0]{1}\d{9}"
end_message = ['good by', 'exit', 'close']


class Field:
    def __init__(self, value=''):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class AddressBook(UserDict, Field):
    def add_record(self, record):
        self.data[record.name] = record

    def add_save_data(self, data):
        self.data = data

    def iterator(self):
        pass


class Name(Field):
    pass


class Birthday(Field):
    @property
    def value(self):
        return self._value

    def valid(self, value):
        date = datetime.strptime(value, '%Y-%m-%d')
        date_now = datetime.now()
        if date > date_now:
            raise ValueError
        return date

    @value.setter
    def value(self, value):
        self._value = self.valid(value)


class Phone(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.valid(value)

    def valid(self, value):
        if match(phone_regex, value) and len(value) == 10:
            return value
        raise ValueError


class Record():

    def __init__(self, name, phone='', date=''):
        self._name = Name(name)
        if phone:
            newPhone = Phone()
            newPhone.value = phone

        self.phones = [newPhone] if phone else []

        if date:
            birthday = Birthday()
            birthday.value = date
            self._date = date
        else:
            self._date = ''

    @property
    def name(self):
        return self._name.value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        birthday = Birthday()
        birthday.value = date
        self._date = birthday

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
            return f' {phone} was deleted'
        else:
            raise KeyError

    def days_to_birthday(self):
        if not self._date:
            return f' You should add date of birthday for {self._name.value}'
        date_now = datetime.now()
        year_now = date_now.strftime('%Y')
        month, date = self._date.value.strftime('%m-%d').split('-')
        u_birth = datetime.strptime(f'{year_now}-{month}-{date}', '%Y-%m-%d')
        delta = u_birth - date_now
        return str(delta.days)

    def show_phones(self):
        return ', '.join([i.value for i in self.phones])
