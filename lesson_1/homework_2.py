def enter_kof(name):
    return f"Please enter {name}: "


a = float(input(enter_kof('x')))
b = float(input(enter_kof('b')))
c = float(input(enter_kof('c')))


def calc():
    d = (b ** 2 - 4 * a * c) ** 0.5
    x_1 = (-b + d) / (2 * a)
    x_2 = (-b - d) / (2 * a)
    return [x_1, x_2]


result = calc()
print(a, b, c, result[0], result[1])
