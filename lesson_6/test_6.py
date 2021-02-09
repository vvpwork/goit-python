
# bodule 6 2
def write_employees(employee_list, path):
    file = open(path, 'w+')
    for i in employee_list:
        file.write('\n'.join(i)+'\n')
    file.close()
    n_file = open(path, 'r')
    data = n_file.readlines()
    n_file.close()
    return data

# def write_employees(employee_list, path):
#     file = open(path, 'w')
#     for i in employee_list:
#         for j in i:
#             file.write(j+ '\n')
#     file.close()
#     n_file = open(path, 'r')
#     data = n_file.readlines()
#     n_file.close()
#     return data


list_ = [['Robert Stivenson, 28 years', 'Alex Denver, 30 years'], [
    'Drake Mikelsson, 19 years', 'Drake Mikelsson, 19 years', 'Drake Mikelsson, 19 years']]


# 5
def get_ingredients(path, position_name):
    with open(path, 'r') as file:
        data = None
        for line in file:
            print(line)
            if position_name in line:
                ing = line.replace(position_name + ':', '')
                data = ing.replace('\n', '').split(',')
                break
    return data


print(get_ingredients('lesson_6/list.txt', "Big chicken"))
