from datetime import datetime, timedelta
from collections import defaultdict

test_dict = [{
    'name': 'John',
    'birthday': datetime(year=2021, month=3, day=19)
}, {
    'name': 'Greg',
    'birthday': datetime(year=2021, month=3, day=15)
}, {
    'name': 'Red',
    'birthday': datetime(year=2021, month=3, day=16)
}, {
    'name': 'Wer',
    'birthday': datetime(year=2021, month=3, day=13)
}
]

week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Monday', 'Monday']


def find_date_gap():
    date = datetime.now()
    days = 5 + (6 - int(date.weekday()))
    next_week_finish = timedelta(days=days) + date
    next_week_start = next_week_finish - timedelta(days=6)
    return [next_week_start, next_week_finish]


def isNextWeek(date_user, grap):
    if grap[0].day <= date_user.day <= grap[1].day:
        return f'{date_user.weekday()}'
    else:
        return False


def congratulate(users):
    try:
        result = defaultdict(list)
        grap = find_date_gap()
        for i in users:
            name = i['name']
            birthsday = i['birthday']
            isNext = isNextWeek(birthsday, grap)
            if isNext:
                result[week_days[int(isNext)]].append(name)
        for key, value in result.items():
            print(f'{key}: {",".join(value)}')
        return result
    except ValueError:
        print('Your date is not datetime entity.')


if __name__ == '__main__':
    congratulate(test_dict)
