from action import action_user, show_all, show_phone, delete_phone,  error_handler, end, add_date, days_to_birhday, sarch_user, read_book


command_dict = {
    'hello': lambda x: 'Hi, how can i help you?',
    'add': action_user('add'),
    'change': action_user('change'),
    'phone': show_phone,
    'show': show_all,
    'delete': delete_phone,
    'date': add_date,
    'days': days_to_birhday,
    'search': sarch_user
}


@error_handler
def main(command):
    command_list = command.lower().split(' ')
    base_command = command_list[0]
    command_keys = command_dict.keys()
    print(command_dict[base_command](
        command_list)) if base_command in command_keys else print(end(command_list))


if __name__ == '__main__':
    read_book()
    while True:
        userCommand = input()
        main(userCommand)
