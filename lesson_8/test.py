import random
from datetime import datetime


def get_days_from_today(date):
    date_arr = list(map(lambda x: int(x), date.split('-')))
    now_date = datetime.now()
    print(now_date, date_arr)
    user_date = datetime(year=date_arr[0], month=date_arr[1], day=date_arr[2])
    print(user_date)
    result = now_date - user_date
    return result.days

# print(get_days_from_today('2021-10-09'))


def random_winners(count, user_dict):
    if count > len(user_dict):
        raise ValueError('ValueError count')
    keys = list(user_dict.keys())
    random.shuffle(keys)
    return random.sample(keys, k=count)



from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    
    sum = 0
    for i in number_list:
        sum += Decimal(i)
    getcontext().prec = signs_count
    average = Decimal(sum) / Decimal((len(number_list) -1))
    return average
    
print(decimal_average([4.5788689699797,34.7576578697964,86.8877666656633,12], 3))