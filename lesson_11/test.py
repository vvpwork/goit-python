from datetime import datetime, timedelta

mock_day = '2009-07-25'


def days(day):
    u_date = datetime.strptime(day, '%Y-%m-%d')
    date_now = datetime.now()
    year_now = date_now.strftime('%Y')
    month, date = u_date.strftime('%m-%d').split('-')
    u_birth = datetime.strptime(f'{year_now}-{month}-{date}' ,'%Y-%m-%d')
    delta = u_birth - date_now
    print(delta.days)


if __name__ == "__main__":
    days(mock_day)
