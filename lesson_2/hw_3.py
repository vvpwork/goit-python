data = []
operators = '+-/*='
result = 0

def isFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

while True:
    try:
        user_command = input('Enter your number or operation:  ')
        isOperetor = user_command in operators

        if user_command == '=':
            print(f"result: {result}")
            break

        if not isOperetor and not isFloat(user_command):
            print('Please enter valid value')
            continue

        if isOperetor and len(data) < 1:
            print('Sorry but you should enter number first')
            continue

        if isOperetor and not isFloat(data[-1]):
            print('Enter number please')
            continue

        if len(data) and (isFloat(user_command) and isFloat(data[-1])):
            print('Enter operator please')
            continue

        data.append(user_command)

        if len(data) == 3:
            try:
                if "-" in data:
                    result = float(data[0]) - float(data[2])
                if "+" in data:
                    result = float(data[0]) + float(data[2])
                if "*" in data:
                    result = float(data[0]) * float(data[2])
                if "/" in data:
                    result = float(data[0]) / float(data[2])
            except ZeroDivisionError:
                print('Error ZeroDivisionError try again ')
                continue
            data = [result] if result else []

    except ValueError:
        print('value error')
        continue
