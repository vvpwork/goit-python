import re
from collections import defaultdict

db = {}
run_while = True
phone_regex = r"[0]{1}\d{9}"
end_message = ['good by', 'exit', 'close']


def error_handler(func):
    def wrapper(*args, **kvargs):
        try:
            func(*args, **kvargs)
        except ValueError:
            print('Give me valid name and phone please')
        except KeyError:
            print("User not found")
        except IndexError:
            print('Command wrong')
    return wrapper


def action_user(variant):
    def user_action(user_arr):
        valid = True
        if len(user_arr) < 3:
            valid = False
        if not re.search(phone_regex, user_arr[2]):
            valid = False
        if not valid:
            raise ValueError
        else:
            name = user_arr[1]
            phone = user_arr[2]
            db[name] = {
                'phone': phone
            }

            return f'User: {name} and phone: {db[name]["phone"]} was {"added" if variant == "add" else "changed"}'
    return user_action


def show_phone(user_arr):
    valid = True
    if len(user_arr) < 2:
        valid = False
    if not valid:
        raise KeyError
    else:
        name = user_arr[1]
        return f'Phone: {db[name]["phone"]}'


def show_all(user_arr):
    valid = True
    if len(user_arr) < 2:
        valid = False
    if user_arr[1] != 'all':
        valid = False
        return 'Maybe your want to write "show all"'
    if not valid:
        raise IndexError
    else:
        keys = db.keys()
        result = ''
        if len(keys):
            for key in keys:
                result += (f'User name: {key}, phone: {db[key]["phone"]} \n')
            return result
        else:
            return 'I dont have any saved users'


def end(user_arr):
    user_str = ' '.join(user_arr)
    if user_str in end_message:
        global run_while
        run_while = False
        return 'Good by'
    else:
        return "I don't know this command"


command_dict = {
    'hello': lambda x: 'Hi, how can i help you?',
    'add': action_user('add'),
    'change': action_user('change'),
    'phone': show_phone,
    'show': show_all
}


@error_handler
def main(command):
    command_list = command.lower().split(' ')
    base_command = command_list[0]
    command_keys = command_dict.keys()
    print(command_dict[base_command](
        command_list)) if base_command in command_keys else print(end(command_list))


if __name__ == '__main__':
    while run_while:
        userCommand = input()
        main(userCommand)
