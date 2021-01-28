import re
from transliterate import translit


def normalize_str(string):
    if type(string).__name__ != 'str':
        return ''

    translate_str = translit(string, 'ru', reversed=True)
    result_str = re.sub('[^0-9A-Za-z]', '_', translate_str)
    return result_str


if __name__ == '__main__':
    print(normalize_str("!№%:,.;()+=-\//\ Питон дз 5 "))