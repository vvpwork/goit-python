import re
dict_comment = {
    "<comment> This place was amazing </comment>": 12,
    "<comment> Thisxsxs  </comment>": 30,
    "<comment> This place dwodow </comment>": 59,
    "<comment> This place dhwdhjwdjw </comment>": 10,
    "<comment> This  </comment>": 2,
    "<comment> This placexsxsx </comment>": 1999,
    "<comment> This place </comment>": 23,
}

# 5


def test(red):
    ''' 
    parameters: 
        red: string
    '''
    return red


def comments_to_show(comment_dict={}):
    result = ''
    list_comment_sorted = sorted(
        comment_dict.items(), key=lambda item: item[1], reverse=True)
    for i, value in enumerate(list_comment_sorted):
        if i < 3:
            string = value[0].removeprefix('<comment>').removesuffix(
                '</comment>').strip().replace('\t', '')
            result += (string + '\n') if i < 2 else string
        else:
            break
    return result


# 6
def translate_surnames(surnames=['бек', 'ронк']):
    letters = 'абеикорнтсл'
    lettars_en = 'abeikorntsl'
    map = {ord(val): lettars_en[i] for i, val in enumerate(letters)}
    result = [i.lower().translate(map).capitalize() for i in surnames]
    return result

# 7


def formatted_comments(comments_dict=dict_comment):
    return ['{:^20} {:>20}'.format(key, value)
            for key, value in comments_dict.items()]


# 8
def fix_rate(rate):
    try:
        return "{:b}".format(rate)
    except ValueError:
        return "{:0.3}".format(rate)

# print(fix_rate(5))
# print(fix_rate(3.233232))


# 9


def structure_recipe(recipe):
    start = re.sub(r'\d', '', recipe)
    finish = re.sub(r';', '\n', start)
    return finish


# 10


def total_price(order):
    numbers = re.findall('\d+', order)
    summ = 0
    for i in numbers:
        summ += int(i)
    return summ
# 11


def find_password(passwords):
    find = re.search(r'[\d]{5}[a-zA-Z]{5}', passwords)
    return find.group()


print(find_password('me1458kitol18293mat176498Merea1984maTias19587'))

test(732884)
