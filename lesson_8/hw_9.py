from datetime import datetime, timedelta


test_dict = [{
    'name': 'John',
    'birthday': datetime(year=2021, month=3, day=19)
}, {
    'name': 'Greg',
    'birthday': datetime(year=2021, month=3, day=17)
}, {
    'name': 'Red',
    'birthday': datetime(year=2021, month=3, day=15)
}, {
    'name': 'Wer',
    'birthday': datetime(year=2021, month=3, day=13)
}
]

week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday']


def find_date_gap():
    date = datetime.now()
    days = 5 + (6 - int(date.weekday()))
    next_week_finish = timedelta(days=days) + date
    next_week_start = next_week_finish - timedelta(days=6)
    return [next_week_start, next_week_finish]


def isNextWeek(date_user, gap):
    try:
        if gap[0].day <= date_user.day <= gap[1].day:
            return f'{date_user.weekday()}'
        else:
            return False
    except ValueError:
        print("Your date is not datetime")


def congratulate(users):
    result = {}
    for i in week_days:
        result[i] = []
    gap = find_date_gap()
    for i in users:
        name = i['name']
        birthsday = i['birthday']
        isNext = isNextWeek(birthsday, gap)
        index = int(isNext)
        if isNext:
            result[week_days[index if index < 5 else 0]].append(name)
    for key, value in result.items():
        if len(value):
            print(f'{key}: { ",".join(value)}')
    return result


if __name__ == '__main__':
    congratulate(test_dict)
