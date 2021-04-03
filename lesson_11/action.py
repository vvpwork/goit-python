import os
import pickle
from collections import defaultdict
from datetime import datetime
from classes import AddressBook, Record


db = AddressBook()
end_message = ['good by', 'exit', 'close']
file_path = os.path.dirname(__file__) + '/dump.bytes'
color = '\033[95m'
color_end = '\033[0m'


def error_handler(func):
    def wrapper(*args, **kvargs):
        try:
            func(*args, **kvargs)
        except ValueError:
            print('Give me valid name or phone or date of birthday please')
        except KeyError:
            print("User or phone not found ")
        except IndexError:
            print('Command wrong or something else...')
        except SystemExit:
            save_book(db)
            print('Good by')
            exit()
    return wrapper


def action_user(variant):
    def user_action(user_arr):
        valid = True
        if len(user_arr) < 2:
            valid = False
        if not valid:
            raise ValueError
        if user_arr[1] in db and variant == 'add':
            return f' This user is already exists'
        else:
            name = user_arr[1]
            phone = user_arr[2] if len(user_arr) > 2 else ''
            date = user_arr[3] if len(user_arr) > 3 else ''
            db.add_record(Record(name, phone, date)
                          ) if variant == 'add' else db[name].add_phone(phone)
            return f' User:{color} {name.capitalize()} {color_end} { f"and phone: " + phone if phone else ""}  was {"added" if variant == "add" else "changed"}'
    return user_action


def show_phone(user_arr):
    valid = True
    if len(user_arr) < 2:
        valid = False
    if not valid:
        raise KeyError
    else:
        name = user_arr[1]
        return f' Phones: {db[name].show_phones()}'


def delete_phone(user_arr):
    valid = True
    if len(user_arr) < 2:
        valid = False
    if not valid:
        raise KeyError
    else:
        name = user_arr[1]
        phone = user_arr[2]
        return db[name].delete_phone(phone)


def show_all(user_arr):
    valid = True

    if len(user_arr) < 2:
        valid = False

    if user_arr[1] not in ['all', 'user']:
        valid = False
        return ' Maybe your want to write "show all" or "show user" '

    if not valid:
        raise IndexError

    if user_arr[1] == 'user':
        name = user_arr[2]
        return f' Name: {color} {db[name].name.capitalize()} {color_end}, \nPhones: {color} {db[name].show_phones()} {color_end} \nBirthday:{color} {db[name].date} {color_end}'

    if user_arr[1] == 'all':
        result = ''
        if len(db):
            for val in db:
                result += (
                    f' User name: {color}{db[val].name.capitalize()}{color_end}, \n Phones:{color} {db[val].show_phones()}{color_end} {color_end} \n Birthday:{color} {db[val].date} {color_end} \n')
            return result
        else:
            return " I don't have any saved users"


def add_date(user_arr):
    valid = True
    if len(user_arr) < 3:
        valid = False
    if not valid:
        raise IndexError
    name = user_arr[1]
    date = user_arr[2]
    if db[name].date:
        return ' The date is already exist'
    db[name].date = date
    return f' The date of birthday for {color}{name.capitalize()}{color_end} was added'


def days_to_birhday(user_arr):
    valid = True
    if len(user_arr) < 2:
        valid = False
    if not valid:
        raise IndexError
    name = user_arr[1]
    days = db[name].days_to_birthday()
    return f" {color}{days}{color_end} left days until the birthday" if len(days) < 4 else days


def wrapper_filter(serch):
    def filter_user(val):
        user = db[val]
        name = user.name
        phones = user.phones
        has_phone = False
        for phone in phones:
            if serch in phone.value:
                has_phone = True
        if serch in name or has_phone:
            return True
        else:
            return False
    return filter_user


def sarch_user(user_arr):
    valid = True
    if len(user_arr) < 2:
        valid = False
    if not valid:
        raise IndexError
    serch = user_arr[1]
    result_list = list(filter(wrapper_filter(serch), db))
    result_str = ''
    if len(result_list) < 1:
        result_str = 'Users not found'
    else:
        for val in result_list:
            user = db[val]
            result_str += f'Name {color} {user.name.capitalize()}{color_end} phones: {color} {user.show_phones()} {color_end}\n'
    return result_str


def save_book(book):
    with open(file_path, 'wb') as file:
        pickle.dump(book, file)
    print('address book was saved')


def read_book():
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            db.add_save_data(data)
    except FileNotFoundError:
        print('Its first start your cli programm')


def end(user_arr):
    user_str = ' '.join(user_arr)
    if user_str in end_message:
        raise SystemExit
    else:
        return " I don't know this command"
